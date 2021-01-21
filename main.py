import itertools
import json
import os
import re
import sqlite3
import subprocess
import tempfile
from contextlib import closing

import urllib3
from packaging.version import InvalidVersion, Version
from tqdm import tqdm
from wheel_filename import InvalidFilenameError, parse_wheel_filename

base_dir = os.path.dirname((os.path.abspath(__file__)))
http = urllib3.PoolManager(
    headers=urllib3.util.make_headers(
        keep_alive=True,
        accept_encoding=True,
        user_agent="sethmlarson/pypi-data",
    ),
    retries=urllib3.util.Retry(status=10, backoff_factor=3),
)
wheel_re = re.compile(r"-([^\-]+-[^\-]+-[^\-]+)\.whl$")

tmp_dir = tempfile.mkdtemp()
os.system(f"virtualenv {tmp_dir}/venv > /dev/null")
venv_python = os.path.join(tmp_dir, "venv/bin/python")

pypi_deps_db = os.path.join(base_dir, "pypi.db")


db = sqlite3.connect(os.path.join(base_dir, "pypi.db"))
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
    PRIMARY KEY (name, version)
  );
"""
)
db.execute(
    """
  CREATE TABLE IF NOT EXISTS deps (
    dependent_name STRING,
    dependent_version STRING,
    dependency_name STRING,
    dependency_specifier STRING,
    extra STRING DEFAULT NULL,
    PRIMARY KEY (dependent_name, dependent_version, dependency_name, dependency_specifier)
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
db.commit()


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
    package_str = f'"{package}"'
    try:
        package_metadata = json.loads(
            subprocess.check_output(
                f"{venv_python} -c 'import json; from importlib_metadata import requires, metadata; "
                f'package={package_str}; print(json.dumps({{"requires_dist": requires(package), "requires_python": metadata(package).get("Requires-Python", "")}}))\'',
                shell=True,
            )
        )
    except subprocess.SubprocessError:
        return resp

    resp = resp.copy()
    resp["info"]["requires_dist"] = package_metadata["requires_dist"]
    resp["info"]["requires_python"] = package_metadata["requires_python"]
    return resp


def update_data_from_pypi():
    for package in tqdm(packages, unit="packages"):
        resp = http.request("GET", f"https://pypi.org/pypi/{package}/json")

        if resp.status != 200:
            continue
        try:
            resp = json.loads(resp.data.decode("utf-8"))
        except Exception:
            continue
        try:
            version = Version(resp["info"]["version"])
        except InvalidVersion:  # The latest release has an invalid version, skip
            continue
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

        # Check to see if we already have this version or not
        with closing(db.cursor()) as cur:
            cur.execute(
                """
              SELECT name FROM packages WHERE name = ? AND version = ?;
            """,
                (package, str_version),
            )
            if cur.fetchone():
                continue

        # If we don't have 'requires_dist' information install
        # locally and investigate the installed package
        if False and resp["info"]["requires_dist"] is None:  # XXX: Disabled for now!
            new_resp = get_metadata_by_install(package, resp)
            if new_resp is not None:
                resp = new_resp

        requires_python = resp["info"]["requires_python"] or ""
        urequires_dist = [
            normalize_requires_dist(x) for x in resp["info"]["requires_dist"] or []
        ]
        urequires_dist = sorted(urequires_dist, key=requires_dist_sort_key)

        requires_dist = {"specifiers": [], "dists": []}
        requires_extras = {}
        yanked = []

        releases = resp["releases"][str_version]
        uploaded_at = min(x["uplaoded_at"] for x in releases)
        wheel_filenames = [
            x["filename"] for x in releases if x["filename"].endswith(".whl")
        ]
        has_binary_wheel = False

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

        db.execute(
            """
          INSERT OR IGNORE INTO packages (
            name, version, requires_python, has_binary_wheel, uploaded_at
          ) VALUES (?, ?, ?, ?, ?);
        """,
            (package, str_version, requires_python, has_binary_wheel, uploaded_at),
        )
        db.commit()

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
                          dependent_name,
                          dependent_version,
                          dependency_name,
                          dependency_specifier,
                          extra
                        ) VALUES (?, ?, ?, ?, ?);
                    """,
                        (package, str_version, req_no_specifiers, specifier, extra),
                    )
            else:
                db.execute(
                    """
                    INSERT OR IGNORE INTO deps (
                      dependent_name,
                      dependent_version,
                      dependency_name,
                      dependency_specifier
                    ) VALUES (?, ?, ?, ?);
                """,
                    (package, str_version, req_no_specifiers, specifier),
                )

        requires_dist["dists"] = sorted(set(requires_dist["dists"]))
        for extra, extra_info in list(requires_extras.items()):
            requires_extras[extra]["dists"] = sorted(set(extra_info["dists"]))

        for relv, downloads in resp["releases"].items():
            for download in downloads:
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


update_data_from_pypi()
