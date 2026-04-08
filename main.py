from __future__ import annotations
import argparse
import itertools
import json
import os
import re
import sqlite3
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import psl
import urllib3
from packaging.version import InvalidVersion, Version
from tqdm import tqdm
from urllib3.util import parse_url
from wheel_filename import InvalidFilenameError, parse_wheel_filename

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

MAX_WORKERS = 64
WRITE_BATCH_SIZE = 100
GOOGLE_ASSURED_OSS_PACKAGES = set()
DOWNLOADS_URL = "https://raw.githubusercontent.com/hugovk/top-pypi-packages/main/top-pypi-packages.min.json"


def flush_batch(batch):
    """Write a batch of package results to the DB in a single transaction."""
    _DB.execute("BEGIN")
    for data in batch:
        _DB.executemany(
            "INSERT INTO wheels (package_name, filename, build, python, abi, platform, uploaded_at) VALUES (?, ?, ?, ?, ?, ?, ?);",
            data["wheel_rows"],
        )
        _DB.execute(
            "INSERT OR IGNORE INTO packages (name, version, requires_python, has_binary_wheel, has_vulnerabilities, first_uploaded_at, last_uploaded_at, downloads, scorecard_overall, in_google_assured_oss) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            data["package_row"],
        )
        _DB.executemany(
            "INSERT OR IGNORE INTO package_urls (package_name, name, url, public_suffix) VALUES (?, ?, ?, ?);",
            data["url_rows"],
        )
        _DB.executemany(
            "INSERT OR IGNORE INTO maintainers (name, package_name) VALUES (?, ?);",
            data["maintainer_rows"],
        )
        _DB.executemany(
            "INSERT OR IGNORE INTO deps (package_name, dep_name, dep_specifier, extra) VALUES (?, ?, ?, ?);",
            data["dep_rows"],
        )
        if data["yanked_update"]:
            _DB.execute(
                "UPDATE packages SET yanked=1 WHERE name=? AND version=?;",
                data["yanked_update"],
            )
        _DB.executemany(
            "INSERT OR IGNORE INTO scorecard_checks (package_name, name, score) VALUES (?, ?, ?);",
            data["scorecard_rows"],
        )
        _DB.executemany(
            "INSERT OR IGNORE INTO classifiers (package_name, name) VALUES (?, ?);",
            data["classifier_rows"],
        )
    _DB.execute("COMMIT")


def get_all_package_names(index_url: str) -> list[str]:
    resp = http.request(
        "GET", f"{index_url}/simple",
        headers={"Accept": "application/vnd.pypi.simple.v1+json"}
    )
    return sorted([item['name'] for item in json.loads(resp.data)['projects']])


def get_extras(req):
    return tuple(sorted(set(re.findall(r"extra=='([^']+)'", req))))


def dist_from_requires_dist(req):
    return re.match(r"^([A-Za-z0-9_.\-]+)", req).group(1)


def specifier_from_requires_dist(req):
    return re.sub(r"\(([^)]+)\)", r"\1", req, count=1)


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


def get_project_urls(info: dict, exclude_host: str | None = None) -> list[tuple[str, str, str]]:
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
        parsed = parse_project_url(project_url, exclude_host=exclude_host)
        if not parsed:
            continue
        host = psl.domain_suffixes(parsed.host).private
        names_urls_hosts.append((project_name, str(parsed), host))

    return names_urls_hosts


def update_data_for_package(package: str, index_url: str, exclude_host: str | None = None) -> dict | None:
    global downloads, GOOGLE_ASSURED_OSS_PACKAGES

    resp = http.request("GET", f"{index_url}/pypi/{package}/json")

    if resp.status != 200:
        return
    try:
        pkg_data = json.loads(resp.data.decode("utf-8"))
    except Exception:
        return
    try:
        version = Version(pkg_data["info"]["version"])
    except InvalidVersion:  # The latest release has an invalid version, skip
        return
    latest_version = max(to_versions(pkg_data["releases"].keys()))

    # Favor pre-releases over non-pre-releases
    if version < latest_version:
        new_resp = http.request(
            "GET", f"{index_url}/pypi/{package}/{latest_version}/json"
        )
        if new_resp.status != 200:
            version = latest_version

    # Get the exact string for the version that we found
    for strv in pkg_data.get("releases", ()):
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

    maintainers = {r["user"] for r in pkg_data.get("ownership", {}).get("roles", [])}

    requires_python = pkg_data["info"]["requires_python"] or ""
    urequires_dist = [
        normalize_requires_dist(x) for x in pkg_data["info"]["requires_dist"] or []
    ]
    urequires_dist = sorted(urequires_dist, key=requires_dist_sort_key)

    yanked = []

    releases = pkg_data["releases"][str_version]
    first_uploaded_at = None if not releases else min(x["upload_time"] for x in releases)
    last_uploaded_at = None if not releases else max(x["upload_time"] for x in releases)
    wheel_data = [
        (x["filename"], x["url"], x["upload_time"]) for x in releases if x["filename"].endswith(".whl")
    ]
    has_binary_wheel = False
    wheel_rows = []

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
        for py, abi, plat in itertools.product(python_tags, abi_tags, platform_tags):
            wheel_rows.append((package, filename, whl.build, py, abi, plat, uploaded_at))

        if abi_tags == ["none"] and platform_tags == ["any"]:
            continue

        has_binary_wheel = True

    # Check if the package has any known vulnerabilities.
    has_vulnerabilities = bool(pkg_data.get("vulnerabilities", []))

    # Prepare all data outside the lock to minimize lock hold time
    package_downloads = downloads.get(package, 0)
    project_urls = get_project_urls(pkg_data["info"], exclude_host=exclude_host)

    dep_rows = []
    for req in urequires_dist:
        extras = get_extras(req)
        req_no_specifiers = dist_from_requires_dist(req)
        specifier = specifier_from_requires_dist(req).replace(
            req_no_specifiers + " ", "", 1
        )
        if extras:
            for extra in extras:
                dep_rows.append((package, req_no_specifiers, specifier, extra))
        else:
            dep_rows.append((package, req_no_specifiers, specifier, None))

    for relv, dls in pkg_data["releases"].items():
        for download in dls:
            if download["yanked"]:
                yanked.append(relv)
                break
    yanked = sorted_versions(set(yanked))

    classifiers = pkg_data["info"].get("classifiers") or []

    return {
        "wheel_rows": wheel_rows,
        "package_row": (
            package,
            str_version,
            requires_python,
            has_binary_wheel,
            has_vulnerabilities,
            first_uploaded_at,
            last_uploaded_at,
            package_downloads,
            scorecard_overall,
            package.lower() in GOOGLE_ASSURED_OSS_PACKAGES,
        ),
        "url_rows": [(package, name, url, host) for name, url, host in project_urls],
        "maintainer_rows": [(m, package) for m in maintainers],
        "dep_rows": dep_rows,
        "yanked_update": (package, str_version) if yanked else None,
        "scorecard_rows": [(package, cn, cs) for cn, cs in scorecard_checks.items()],
        "classifier_rows": [(package, c) for c in classifiers],
    }


def filter_packages(pkgs):
    # Check to see if we already have this package or not.
    existing = {row[0] for row in _DB.execute("SELECT name FROM packages").fetchall()}
    return [pkg for pkg in pkgs if pkg not in existing]


def parse_project_url(url: str | None, exclude_host: str | None = None):
    try:
        parsed = parse_url(url)
        if not parsed.host:
            return None
        if exclude_host and parsed.host == exclude_host:
            return None
        if not str(parsed).startswith("http"):
            return None
        return parsed
    except Exception:
        return None


def update_data_from_pypi(index_url: str, exclude_host: str | None = None) -> None:
    filtered = filter_packages(packages)
    futures = [pool.submit(update_data_for_package, pkg, index_url, exclude_host) for pkg in filtered]
    batch = []
    for future in tqdm(as_completed(futures), total=len(filtered), unit="packages"):
        result = future.result()
        if result is None:
            continue
        batch.append(result)
        if len(batch) >= WRITE_BATCH_SIZE:
            flush_batch(batch)
            batch = []
    if batch:
        flush_batch(batch)


def get_google_assured_oss_packages(http: urllib3.PoolManager) -> set[str]:
    resp = http.request("GET", "https://cloud.google.com/assured-open-source-software/docs/supported-packages")
    data = resp.data.decode("utf-8")

    # Start after the Python heading, then look for first list.
    data = data[data.find("<h2 id=\"python\""):]
    start = data.find("<ul>")
    end = data.find("</ul>")
    return {x.lower() for x in re.findall(r"<li>([^<]+)</li>", data[start:end])}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch PyPI package metadata into a SQLite database.")
    parser.add_argument(
        "--index",
        choices=["pypi", "testpypi"],
        default="pypi",
        help="Which PyPI index to use (default: pypi)",
    )
    args = parser.parse_args()

    INDEX_URLS = {
        "pypi": "https://pypi.org",
        "testpypi": "https://test.pypi.org",
    }
    DB_NAMES = {
        "pypi": "pypi.db",
        "testpypi": "test.pypi.db",
    }
    # Exclude noise URLs from project_urls
    EXCLUDE_HOSTS = {
        "pypi": "test.pypi.org",
        "testpypi": None,
    }

    index_url = INDEX_URLS[args.index]
    db_name = DB_NAMES[args.index]
    exclude_host = EXCLUDE_HOSTS[args.index]

    base_dir = os.path.dirname(os.path.abspath(__file__))
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
    os.system(f"python -m venv {tmp_dir}/venv > /dev/null")
    venv_python = os.path.join(tmp_dir, "venv/bin/python")

    pypi_deps_db = os.path.join(base_dir, db_name)

    downloads = {}
    resp = http.request("GET", DOWNLOADS_URL)
    assert resp.status == 200
    for row in json.loads(resp.data)["rows"]:
        downloads[row["project"]] = row["download_count"]

    _DB = sqlite3.connect(pypi_deps_db, check_same_thread=False, isolation_level=None)
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
        CREATE TABLE IF NOT EXISTS classifiers (
            package_name TEXT,
            name TEXT,
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
    _DB.execute("PRAGMA journal_mode = WAL")
    _DB.commit()
    pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    packages = get_all_package_names(index_url)

    update_data_from_pypi(index_url, exclude_host=exclude_host)
