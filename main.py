from __future__ import annotations
import contextlib
import itertools
import json
import os
import re
import sqlite3
import subprocess
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing

import psl
import urllib3
from packaging.version import InvalidVersion, Version
from tqdm import tqdm
from urllib3.util import parse_url
from wheel_filename import InvalidFilenameError, parse_wheel_filename

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

MAX_WORKERS = 16
GOOGLE_ASSURED_OSS_PACKAGES = set()
DOWNLOADS_URL = "https://raw.githubusercontent.com/hugovk/top-pypi-packages/main/top-pypi-packages-30-days.min.json"

@contextlib.contextmanager
def locked_db():
    with db_lock:
        yield _DB
        _DB.commit()


def get_all_package_names():
    resp = http.request("GET", "https://pypi.org/simple")
    return sorted(
        [item.decode() for item in re.findall(b'href="/simple/([^/]+)/', resp.data)]
    )


def get_extras(req):
    return tuple(sorted(set(re.findall(r"extra=='([^']+)'", req))))


def dist_from_requires_dist(req):
    return re.match(r"^([A-Za-z0-9_.\-]+)", req).group(1)


def specifier_from_requires_dist(req):
    return re.sub(r"\(([^)]+)\)", r"\1", req, 1)


def normalize_requires_dist(req):
    return re.sub(
        r"\s*,\s*",
        ",",
        re.sub(
            r"\s*([!><=~]{1,2})\s*",
            r"\1",
            re.sub(r"\s*;\s*", r"; ", req.replace('"', "'")),
        ),
    ).lower()


def requires_dist_sort_key(req):
    return (
        get_extras(req),
        re.match(r"^([a-zA-Z0-9_.\-\[\]]+)", req).group(1).lower(),
        req,
    )


def to_versions(items):
    vers = []
    for item in items:
        try:
            vers.append(Version(item))
        except InvalidVersion:
            continue
    return vers


def sorted_versions(items):
    vers = []
    for item in items:
        try:
            vers.append((Version(item), item))
        except InvalidVersion:
            continue
    return [
        x
        for _, x in sorted(
            vers,
        )
    ]


def get_metadata_by_install(package, resp):
    if (
        os.system(
            f"{venv_python} -m pip install --disable-pip-version-check {package} importlib-metadata > /dev/null"
        )
        != 0
    ):
        return None

    print(f"building {package!r} from source!")
    popen = subprocess.Popen(
        f"{venv_python} -c 'import json; from importlib_metadata import Distribution; "
        f'd=Distribution.from_name("{package}"); print(json.dumps({{"requires_dist": d.requires(package), "requires_python": d.metadata.get("Requires-Python", ""), "wheel_data": dist.read_text("WHEEL") or ""}}))\'',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )

    # Run the install for no more than 20 seconds
    start_time = time.time()
    while time.time() - start_time < 20 and popen.poll() is None:
        time.sleep(0.5)

    if popen.returncode != 0:
        return resp
    package_metadata = json.loads(popen.stdout.read())

    resp = resp.copy()
    resp["info"]["requires_dist"] = package_metadata["requires_dist"]
    resp["info"]["requires_python"] = package_metadata["requires_python"]
    return resp


def get_maintainers_from_pypi(package: str):
    for _ in range(5):
        resp = http.request("GET", f"https://pypi.org/project/{package}/")
        if resp.status == 404:
            return set()
        elif resp.status != 200:
            continue
        return set(
            re.findall(
                r"<a href=\"/user/([^/]+)/\" aria-label=", resp.data.decode("utf-8")
            )
        )
    return set()


def fetch_checks_for_package(package_name):
    resp = http.request("GET", f"https://deps.dev/_/s/pypi/p/{package_name}/v/")
    if resp.status != 200:
        return {}
    data = json.loads(resp.data)

    checks = {}
    try:
        for project in data["version"]["projects"]:
            if scorecard := project.get("scorecardV2"):
                for check in scorecard.get("check", None) or ():
                    check_name = check["name"]
                    check_score = check["score"]

                    # This is how deps.dev denotes a missing score in the API.
                    if check_score < 0:
                        continue
                    # The score is already set and larger than this project value.
                    if (checks.get(check_name, 0.0) or 0.0) > check_score:
                        continue

                    checks[check_name] = check_score

                checks["Overall"] = scorecard["score"]
                break

    except (KeyError, IndexError):
        return {}
    return checks


def get_project_urls(info: dict) -> list[tuple[str, str, str]]:
    names_urls = [
        ("docs_url", info.get("docs_url")),
        ("Downloads", info.get("download_url")),
        ("Homepage", info.get("home_page")),
    ]

    if info.get("project_urls"):
        for name, url in info.get("project_urls").items() or ():
            names_urls.append((name, url))

    names_urls_hosts = []
    for project_name, project_url in names_urls:
        parsed = parse_project_url(project_url)
        if not parsed:
            continue
        host = psl.domain_suffixes(parsed.host).private
        names_urls_hosts.append((project_name, str(parsed), host))

    return names_urls_hosts


def update_data_for_package(package: str) -> None:
    global downloads, db_lock, GOOGLE_ASSURED_OSS_PACKAGES

    resp = http.request("GET", f"https://pypi.org/pypi/{package}/json")

    if resp.status != 200:
        return
    try:
        resp = json.loads(resp.data.decode("utf-8"))
    except Exception:
        return
    try:
        version = Version(resp["info"]["version"])
    except InvalidVersion:  # The latest release has an invalid version, skip
        return
    latest_version = max(to_versions(resp["releases"].keys()))

    # Favor pre-releases over non-pre-releases
    if version < latest_version:
        new_resp = http.request(
            "GET", f"https://pypi.org/pypi/{package}/{latest_version}/json"
        )
        if new_resp.status != 200:
            version = latest_version

    # Get the exact string for the version that we found
    for strv in resp.get("releases", ()):
        try:
            if Version(strv) == version:
                str_version = strv
                break
        except InvalidVersion:
            continue
    else:
        # Skip this package
        return

    scorecard_checks = fetch_checks_for_package(package)
    scorecard_overall = scorecard_checks.pop("Overall", None)

    maintainers = get_maintainers_from_pypi(package)

    requires_python = resp["info"]["requires_python"] or ""
    urequires_dist = [
        normalize_requires_dist(x) for x in resp["info"]["requires_dist"] or []
    ]
    urequires_dist = sorted(urequires_dist, key=requires_dist_sort_key)

    requires_dist = {"specifiers": [], "dists": []}
    requires_extras = {}
    yanked = []

    releases = resp["releases"][str_version]
    first_uploaded_at = None if not releases else min(x["upload_time"] for x in releases)
    last_uploaded_at = None if not releases else max(x["upload_time"] for x in releases)
    wheel_data = [
        (x["filename"], x["url"], x["upload_time"]) for x in releases if x["filename"].endswith(".whl")
    ]
    has_binary_wheel = False

    for filename, _, uploaded_at in wheel_data:
        try:
            whl = parse_wheel_filename(filename)
        except InvalidFilenameError:
            continue
        python_tags, abi_tags, platform_tags = (
            whl.python_tags,
            whl.abi_tags,
            whl.platform_tags,
        )
        for wheel_data in itertools.product(python_tags, abi_tags, platform_tags):
            py, abi, plat = wheel_data
            with locked_db() as db:
                db.execute(
                    """
                    INSERT INTO wheels (
                    package_name, filename, build, python, abi, platform, uploaded_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                    (package, filename, whl.build, py, abi, plat, uploaded_at),
                )

        if abi_tags == ["none"] and platform_tags == ["any"]:
            continue

        has_binary_wheel = True

    # Check if the package has any known vulnerabilities.
    has_vulnerabilities = bool(resp.get("vulnerabilities", []))

    package_downloads = downloads.get(package, 0)
    with locked_db() as db:
        db.execute(
            """
            INSERT OR IGNORE INTO packages (
            name, version, requires_python, has_binary_wheel, has_vulnerabilities, first_uploaded_at, last_uploaded_at, downloads, scorecard_overall, in_google_assured_oss
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
            (
                package,
                str_version,
                requires_python,
                has_binary_wheel,
                has_vulnerabilities,
                first_uploaded_at,
                last_uploaded_at,
                package_downloads,
                scorecard_overall,
                package.lower() in GOOGLE_ASSURED_OSS_PACKAGES
            ),
        )

        project_urls = get_project_urls(resp["info"])

        for name, url, host in project_urls:
            db.execute(
                """
                INSERT OR IGNORE INTO package_urls (package_name, name, url, public_suffix) VALUES (?, ?, ?, ?);
            """,
                (package, name, url, host),
            )

        for maintainer in maintainers:
            db.execute(
                """
                INSERT OR IGNORE INTO maintainers (name, package_name) VALUES (?, ?);
            """,
                (maintainer, package),
            )

        for req in urequires_dist:
            extras = get_extras(req)
            req_no_specifiers = dist_from_requires_dist(req)
            specifier = specifier_from_requires_dist(req).replace(
                req_no_specifiers + " ", "", 1
            )
            if extras:
                for extra in extras:
                    db.execute(
                        """
                        INSERT OR IGNORE INTO deps (
                            package_name,
                            dep_name,
                            dep_specifier,
                            extra
                        ) VALUES (?, ?, ?, ?);
                    """,
                        (package, req_no_specifiers, specifier, extra),
                    )
            else:
                db.execute(
                    """
                    INSERT OR IGNORE INTO deps (
                        package_name,
                        dep_name,
                        dep_specifier
                    ) VALUES (?, ?, ?);
                """,
                    (package, req_no_specifiers, specifier),
                )

        requires_dist["dists"] = sorted(set(requires_dist["dists"]))
        for extra, extra_info in list(requires_extras.items()):
            requires_extras[extra]["dists"] = sorted(set(extra_info["dists"]))

        for relv, dls in resp["releases"].items():
            for download in dls:
                if download["yanked"]:
                    yanked.append(relv)
                    break

        yanked = sorted_versions(set(yanked))
        if yanked:
            db.execute(
                "UPDATE packages SET yanked=1 WHERE name=? AND version=?;",
                (package, str_version),
            )

        for check_name, check_score in scorecard_checks.items():
            db.execute(
                """
                INSERT OR IGNORE INTO scorecard_checks (
                    package_name,
                    name,
                    score
                ) VALUES (?, ?, ?);
            """,
                (package, check_name, check_score),
            )

    return package


def filter_packages(pkgs):
    # Check to see if we already have this package or not.
    packages_to_process = []
    with locked_db() as db:
        with closing(db.cursor()) as cur:
            for pkg in pkgs:
                cur.execute(
                    "SELECT name FROM packages WHERE name = ? LIMIT 1;",
                    (pkg,),
                )
                if cur.fetchone():
                    continue
                packages_to_process.append(pkg)
    return packages_to_process


def parse_project_url(url):
    try:
        parsed = parse_url(url)
        if not parsed.host or parsed.host == "pypi.org":
            return None
        if not str(parsed).startswith("http"):
            return None
        return parsed
    except Exception:
        return None


def update_data_from_pypi():
    filtered = filter_packages(packages)
    results = pool.map(update_data_for_package, filtered)
    for _ in tqdm(results, total=len(filtered), unit="packages"):
        pass


def get_google_assured_oss_packages(http: urllib3.PoolManager) -> set[str]:
    resp = http.request("GET", "https://cloud.google.com/assured-open-source-software/docs/supported-packages")
    data = resp.data.decode("utf-8")

    # Start after the Python heading, then look for first list.
    data = data[data.find("<h2 id=\"python\""):]
    start = data.find("<ul>")
    end = data.find("</ul>")
    return {x.lower() for x in re.findall(r"<li>([^<]+)</li>", data[start:end])}


if __name__ == "__main__":
    base_dir = os.path.dirname((os.path.abspath(__file__)))
    http = urllib3.PoolManager(
        block=True,
        strict=True,
        maxsize=MAX_WORKERS,
        headers=urllib3.util.make_headers(
            keep_alive=True,
            accept_encoding=True,
            user_agent="sethmlarson/pypi-data",
        ),
        retries=urllib3.util.Retry(
            status=10, backoff_factor=0.5, status_forcelist=list(range(500, 600))
        ),
    )
    wheel_re = re.compile(r"-([^\-]+-[^\-]+-[^\-]+)\.whl$")

    GOOGLE_ASSURED_OSS_PACKAGES = get_google_assured_oss_packages(http)

    tmp_dir = tempfile.mkdtemp()
    os.system(f"virtualenv {tmp_dir}/venv > /dev/null")
    venv_python = os.path.join(tmp_dir, "venv/bin/python")

    pypi_deps_db = os.path.join(base_dir, "pypi.db")

    downloads = {}
    resp = http.request("GET", DOWNLOADS_URL)
    assert resp.status == 200
    for row in resp.json()["rows"]:
        downloads[row["project"]] = row["download_count"]

    _DB = sqlite3.connect(os.path.join(base_dir, "pypi.db"), check_same_thread=False)
    _DB.execute(
        """
      CREATE TABLE IF NOT EXISTS packages (
        name TEXT,
        version TEXT,
        requires_python TEXT,
        yanked BOOLEAN DEFAULT 0,
        has_binary_wheel BOOLEAN,
        has_vulnerabilities BOOLEAN,
        first_uploaded_at TIMESTAMP,
        last_uploaded_at TIMESTAMP,
        recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        downloads INTEGER,
        scorecard_overall FLOAT,
        in_google_assured_oss BOOLEAN,
        PRIMARY KEY (name)
      );
    """
    )
    _DB.execute(
        """
      CREATE TABLE IF NOT EXISTS deps (
        package_name TEXT,
        version TEXT,
        dep_name TEXT,
        dep_specifier TEXT,
        extra TEXT DEFAULT NULL,
        PRIMARY KEY (package_name, version, dep_name, dep_specifier),
        FOREIGN KEY (package_name) REFERENCES packages(name),
        FOREIGN KEY (dep_name) REFERENCES packages(name)
      );
    """
    )
    _DB.execute(
        """
      CREATE TABLE IF NOT EXISTS wheels (
        package_name TEXT,
        version TEXT,
        filename TEXT,
        build TEXT,
        python TEXT,
        abi TEXT,
        platform TEXT,
        uploaded_at TIMESTAMP,
        FOREIGN KEY (package_name) REFERENCES packages(name)
      );
    """
    )
    _DB.execute(
        """
        CREATE TABLE IF NOT EXISTS maintainers (
            name TEXT,
            package_name TEXT,
            PRIMARY KEY (name, package_name),
            FOREIGN KEY (package_name) REFERENCES packages(name)
        );
    """
    )
    _DB.execute(
        """
        CREATE TABLE IF NOT EXISTS package_urls (
            package_name TEXT,
            name TEXT,
            url TEXT,
            public_suffix TEXT,
            PRIMARY KEY (package_name, url),
            FOREIGN KEY (package_name) REFERENCES packages(name)
        );
        """
    )
    _DB.execute(
        """
        CREATE TABLE IF NOT EXISTS scorecard_checks (
            package_name TEXT,
            name TEXT,
            score INTEGER,
            PRIMARY KEY (package_name, name),
            FOREIGN KEY (package_name) REFERENCES packages(name)
        );
        """
    )
    _DB.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_packages_name ON packages (name);
        """
    )
    _DB.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_packages_urls_public_suffix ON package_urls (public_suffix);
        """
    )
    _DB.commit()
    db_lock = threading.Lock()
    pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    packages = get_all_package_names()

    update_data_from_pypi()
