import os
import json
import re
from tqdm import tqdm
import urllib3
from packaging.version import Version, InvalidVersion


base_dir = os.path.dirname((os.path.abspath(__file__)))
package_data_dir = os.path.join(base_dir, "package-data")
http = urllib3.PoolManager(
    headers=urllib3.util.make_headers(
        keep_alive=True,
        accept_encoding=True,
        user_agent="sethmlarson/pypi-deps-tracker",
    ),
    retries=urllib3.util.Retry(status=10, backoff_factor=0.5),
)
wheel_re = re.compile(r"-([^\-]+-[^\-]+-[^\-]+)\.whl$")


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


with open("packages.txt") as f:
    packages = [x for x in f.read().split() if x.strip()]
    publisher_data = {}

    for package in tqdm(packages, unit="packages"):
        resp = http.request("GET", f"https://pypi.org/pypi/{package}/json")
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
                    requires_extras[extra]["dists"].append(dist_from_requires_dist(req))
            else:
                requires_dist["specifiers"].append(req)
                requires_dist["dists"].append(dist_from_requires_dist(req))

        requires_python = resp["info"]["requires_python"] or ""

        for relv, downloads in resp["releases"].items():
            for download in downloads:
                if download["yanked"]:
                    yanked.append(relv)
                    break
        yanked = sorted_versions(set(yanked))

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
    with open(os.path.join(package_data_dir, f"publishers.json"), "w") as f:
        f.truncate()
        f.write(
            json.dumps(
                {k: sorted(v) for k, v in publisher_data.items()},
                indent=2,
                sort_keys=True,
            )
        )
