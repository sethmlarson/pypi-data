import itertools
import json
import os
import re
import sqlite3
import subprocess
import tempfile
import time
import csv
from contextlib import closing
from concurrent.futures import ThreadPoolExecutor

import urllib3
from urllib3.util import parse_url
import threading
from packaging.version import InvalidVersion, Version
from tqdm import tqdm
from wheel_filename import InvalidFilenameError, parse_wheel_filename
import psl

import logging

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

base_dir = os.path.dirname((os.path.abspath(__file__)))
http = urllib3.PoolManager(
    headers=urllib3.util.make_headers(
        keep_alive=True,
        accept_encoding=True,
        user_agent="sethmlarson/pypi-data",
    ),
    retries=urllib3.util.Retry(status=10, backoff_factor=0.5),
)
wheel_re = re.compile(r"-([^\-]+-[^\-]+-[^\-]+)\.whl$")

tmp_dir = tempfile.mkdtemp()
os.system(f"virtualenv {tmp_dir}/venv > /dev/null")
venv_python = os.path.join(tmp_dir, "venv/bin/python")

pypi_deps_db = os.path.join(base_dir, "pypi.db")

downloads = {}
with open(os.path.join(base_dir, "downloads.csv")) as f:
    for project, dls in csv.reader(f):
        downloads[project] = int(dls)

db = sqlite3.connect(os.path.join(base_dir, "pypi.db"), check_same_thread=False)
db.execute(
    """
  CREATE TABLE IF NOT EXISTS packages (
    name STRING,
    version STRING,
    requires_python STRING,
    yanked BOOLEAN DEFAULT FALSE,
    has_binary_wheel BOOLEAN,
    uploaded_at TIMESTAMP,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    downloads INTEGER,
    PRIMARY KEY (name, version)
  );
"""
)
db.execute(
    """
  CREATE TABLE IF NOT EXISTS deps (
    name STRING,
    version STRING,
    dep_name STRING,
    dep_specifier STRING,
    extra STRING DEFAULT NULL,
    PRIMARY KEY (name, version, dep_name, dep_specifier)
  );
"""
)
db.execute(
    """
  CREATE TABLE IF NOT EXISTS wheels (
    name STRING,
    version STRING,
    filename STRING,
    python STRING,
    abi STRING,
    platform STRING
  );
"""
)
db.execute(
    """
    CREATE TABLE IF NOT EXISTS maintainers (
        name STRING,
        package_name STRING
    );
"""
)
db.execute(
    """
    CREATE TABLE IF NOT EXISTS package_urls (
        package_name STRING,
        url STRING,
        public_suffix STRING
    );
    """
)

db.execute(
    """
    CREATE UNIQUE INDEX IF NOT EXISTS idx_packages_name_version ON packages (name, version);
    """
)
db.execute(
    """
    CREATE INDEX IF NOT EXISTS idx_packages_name ON packages (name);
    """
)
db.execute(
    """
    CREATE INDEX IF NOT EXISTS idx_packages_urls_public_suffix ON package_urls (public_suffix);
    """
)
db.commit()
db_lock = threading.Lock()
pool = ThreadPoolExecutor()


def get_all_package_names():
    resp = http.request("GET", "https://pypi.org/simple", preload_content=False)

    packages = set()
    old_data = b""
    for new_data in resp.stream():
        old_data += new_data
        matches = re.findall(b'href="/simple/([^/]+)/', old_data)
        packages.update([item.decode() for item in matches])
        if matches:
            old_data = old_data[old_data.rfind(matches[-1]) - 1 :]

    resp.close()
    return sorted(packages)


packages = get_all_package_names()


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
        f"{venv_python} -c 'import json; from importlib_metadata import requires, metadata; "
        f'package="{package}"; print(json.dumps({{"requires_dist": requires(package), "requires_python": metadata(package).get("Requires-Python", "")}}))\'',
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
        resp = http.request("GET", f"https://pypi.org/project/{package}")
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


def update_data_for_package(package: str) -> None:
    global downloads, db_lock

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
        version = latest_version
        new_resp = http.request(
            "GET", f"https://pypi.org/pypi/{package}/{latest_version}/json"
        )
        if new_resp.status == 200:
            resp = json.loads(new_resp.data.decode("utf-8"))

    # Get the exact string for the version that we found
    for strv in resp["releases"]:
        try:
            if Version(strv) == version:
                str_version = strv
                break
        except InvalidVersion:
            continue
    else:
        raise ValueError("???")

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
    uploaded_at = None if not releases else min(x["upload_time"] for x in releases)
    wheel_filenames = [
        x["filename"] for x in releases if x["filename"].endswith(".whl")
    ]
    has_binary_wheel = False

    with db_lock:
        for filename in wheel_filenames:
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
                db.execute(
                    """
                    INSERT INTO wheels (
                    name, version, filename, python, abi, platform
                    ) VALUES (?, ?, ?, ?, ?, ?);
                """,
                    (package, str_version, filename, py, abi, plat),
                )

            if abi_tags == ["none"] and platform_tags == ["any"]:
                continue

            has_binary_wheel = True

        package_downloads = downloads.get(package, 0)
        db.execute(
            """
            INSERT OR IGNORE INTO packages (
            name, version, requires_python, has_binary_wheel, uploaded_at, downloads
            ) VALUES (?, ?, ?, ?, ?, ?);
        """,
            (
                package,
                str_version,
                requires_python,
                has_binary_wheel,
                uploaded_at,
                package_downloads,
            ),
        )

        project_urls = [
            resp["info"].get("bugtrack_url"),
            resp["info"].get("docs_url"),
            resp["info"].get("download_url"),
            resp["info"].get("home_page"),
            resp["info"].get("project_url"),
        ]
        for project_url in resp["info"].get("project_urls") or ():
            project_urls.append(project_url)
        for project_url in project_urls:
            parsed = parse_project_url(project_url)
            if not parsed:
                continue
            host = psl.domain_suffixes(parsed.host).private
            db.execute(
                """
                INSERT OR IGNORE INTO package_urls (package_name, url, public_suffix) VALUES (?, ?, ?);
            """,
                (package, str(parsed), host),
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
                            name,
                            version,
                            dep_name,
                            dep_specifier,
                            extra
                        ) VALUES (?, ?, ?, ?, ?);
                    """,
                        (package, str_version, req_no_specifiers, specifier, extra),
                    )
            else:
                db.execute(
                    """
                    INSERT OR IGNORE INTO deps (
                        name,
                        version,
                        dep_name,
                        dep_specifier
                    ) VALUES (?, ?, ?, ?);
                """,
                    (package, str_version, req_no_specifiers, specifier),
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

        db.commit()

    return package


def filter_packages(pkgs):
    # Check to see if we already have this package or not.
    packages_to_process = []
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


if __name__ == "__main__":
    update_data_from_pypi()
