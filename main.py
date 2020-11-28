import datetime
import os
import json
import re
import subprocess
import tempfile
from tqdm import tqdm
import urllib3
from packaging.version import Version, InvalidVersion


base_dir = os.path.dirname((os.path.abspath(__file__)))
package_data_dir = os.path.join(base_dir, "package-data")
http = urllib3.PoolManager(
    headers=urllib3.util.make_headers(
        keep_alive=True,
        accept_encoding=True,
        user_agent="sethmlarson/pypi-seismometer",
    ),
    retries=urllib3.util.Retry(status=10, backoff_factor=0.5),
)
wheel_re = re.compile(r"-([^\-]+-[^\-]+-[^\-]+)\.whl$")

tmp_dir = tempfile.mkdtemp()
os.system(f"virtualenv {tmp_dir}/venv > /dev/null")
venv_python = os.path.join(tmp_dir, "venv/bin/python")


def get_extras(req):
    return tuple(sorted(set(re.findall(r"extra=='([^']+)'", req))))


def dist_from_requires_dist(req):
    return re.match(r"^([A-Za-z0-9_.\-]+)", req).group(1)


def normalize_requires_dist(req):
    return re.sub(
        r"\s*,\s*",
        ",",
        re.sub(
            r"\s*([><=~]{1,2})\s*",
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


def bad_versions_from_dist(req):
    return re.findall(r"!=([0-9][0-9.\-_a-zA-Z]*[0-9a-zA-Z])", req)


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
            f"{venv_python} -m pip install {package} importlib-metadata > /dev/null"
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


with open(os.path.join(package_data_dir, "deleted.json")) as f:
    deleted_data = json.loads(f.read())


with open("packages.txt") as f:
    packages = [x for x in f.read().split() if x.strip()]
    publisher_data = {}
    bad_versions_data = {}
    yanked_data = {}

    for package in tqdm(packages, unit="packages"):
        resp = http.request("GET", f"https://pypi.org/pypi/{package}/json")

        if resp.status != 200:
            # If a package is deleted it'll start 404-ing
            if resp.status == 404:
                deleted_data.setdefault(
                    package, {"deleted_at": datetime.date.today().isoformat()}
                )
            else:
                print("%r returned non-2XX status code: %d" % (package, resp.status))
            continue

        resp = json.loads(resp.data.decode("utf-8"))
        version = Version(resp["info"]["version"])
        latest_version = max(to_versions(resp["releases"].keys()))

        # Favor pre-releases over non-pre-releases
        if version < latest_version:
            version = latest_version
            resp = http.request(
                "GET", f"https://pypi.org/pypi/{package}/{latest_version}/json"
            )
            resp = json.loads(resp.data.decode("utf-8"))

        # If the previous version had requires_dist info
        # but the new version for some reason doesn't
        # consider building a wheel locally.
        if resp["info"]["requires_dist"] is None:
            old_info_path = os.path.join(
                package_data_dir, package[0], f"{package}.json"
            )
            if os.path.isfile(old_info_path):
                with open(old_info_path) as f:
                    old_info = json.loads(f.read())
                if old_info["requires_dist"]["dists"] or old_info["requires_extras"]:
                    new_resp = get_metadata_by_install(package, resp)
                    if new_resp is not None:
                        resp = new_resp

        for strv in resp["releases"]:
            try:
                if Version(strv) == version:
                    str_version = strv
                    break
            except InvalidVersion:
                continue
        else:
            raise ValueError("???")

        urequires_dist = [
            normalize_requires_dist(x) for x in resp["info"]["requires_dist"] or []
        ]
        urequires_dist = sorted(urequires_dist, key=requires_dist_sort_key)

        requires_dist = {"specifiers": [], "dists": []}
        requires_extras = {}
        yanked = []

        for req in urequires_dist:
            extras = get_extras(req)
            req_no_specifiers = dist_from_requires_dist(req)
            if extras:
                for extra in extras:
                    if extra in (
                        "test",
                        "tests",
                        "dev",
                        "devel",
                        "doc",
                        "docs",
                        "testing",
                        "all",
                    ):
                        continue
                    requires_extras.setdefault(extra, {"specifiers": [], "dists": []})
                    requires_extras[extra]["specifiers"].append(req)
                    requires_extras[extra]["dists"].append(req_no_specifiers)
            else:
                requires_dist["specifiers"].append(req)
                requires_dist["dists"].append(req_no_specifiers)

            bad_versions = bad_versions_from_dist(req)
            if bad_versions:
                bad_versions_data.setdefault(req_no_specifiers, []).extend(bad_versions)

        requires_dist["dists"] = sorted(set(requires_dist["dists"]))
        for extra, extra_info in list(requires_extras.items()):
            requires_extras[extra]["dists"] = sorted(set(extra_info["dists"]))

        requires_python = resp["info"]["requires_python"] or ""

        for relv, downloads in resp["releases"].items():
            for download in downloads:
                if download["yanked"]:
                    yanked.append(relv)
                    break

        yanked = sorted_versions(set(yanked))
        if yanked:
            yanked_data[package] = yanked

        resp = http.request("GET", f"https://pypi.org/project/{package}")
        publishers = sorted(
            set(
                re.findall(r"<a href=\"/user/([^/\"]+)[/\"]", resp.data.decode("utf-8"))
            ),
            key=str.lower,
        )
        for publisher in publishers:
            publisher_data.setdefault(publisher, []).append(package)

        os.makedirs(os.path.join(package_data_dir, package[0]), exist_ok=True)
        with open(
            os.path.join(package_data_dir, package[0], f"{package}.json"), "w"
        ) as f:
            f.truncate()
            f.write(
                json.dumps(
                    {
                        "requires_dist": requires_dist,
                        "requires_extras": requires_extras,
                        "requires_python": requires_python,
                        "publishers": publishers,
                        "yanked": yanked,
                    },
                    indent=2,
                    sort_keys=True,
                )
            )

    # Write publishers.json data
    with open(os.path.join(package_data_dir, "publishers.json"), "w") as f:
        f.truncate()
        f.write(
            json.dumps(
                {k: sorted(v) for k, v in publisher_data.items()},
                indent=2,
                sort_keys=True,
            )
        )

    # Write yanked-versions.json data
    with open(os.path.join(package_data_dir, "yanked-versions.json"), "w") as f:
        f.truncate()
        f.write(
            json.dumps(
                yanked_data,
                indent=2,
                sort_keys=True,
            )
        )

    # Remove entries from 'bad_version_data' if they are yanked
    bad_versions_data = {
        k: sorted_versions({x for x in v if x not in yanked_data.get(k, ())})
        for k, v in bad_versions_data.items()
    }
    bad_versions_data = {k: v for k, v in bad_versions_data.items() if v}

    # Write bad-versions.json data
    with open(os.path.join(package_data_dir, "bad-versions.json"), "w") as f:
        f.truncate()
        f.write(
            json.dumps(
                bad_versions_data,
                indent=2,
                sort_keys=True,
            )
        )

    # Write deleted.json data
    with open(os.path.join(package_data_dir, "deleted.json"), "w") as f:
        f.truncate()
        f.write(
            json.dumps(
                deleted_data,
                indent=2,
                sort_keys=True,
            )
        )
