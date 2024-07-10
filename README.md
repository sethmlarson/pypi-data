# PyPI Data

Mostly up-to-date data about almost every package on PyPI

Get access to the database via [GitHub releases](https://github.com/sethmlarson/pypi-data/releases).

```console
$ gunzip pypi.db.gz
$ sqlite3 'pypi.db' 'SELECT * FROM packages LIMIT 10 OFFSET 1000;'

acid-vault|1.3.2|>=3.6|1|0|2021-01-21 04:37:10
acidcli|1.0.1|>=3.6|0|0|2021-01-21 04:37:10
acidfile|1.2.1||0|0|2021-01-21 04:37:10
acidfs|1||0|0|2021-01-21 04:37:10
acidoseq|1.3.7||0|0|2021-01-21 04:37:10
acinonyx|0.1.0|>=3.6.0|0|0|2021-01-21 04:37:10
aciops|2.0.0|>=3.6|0|0|2021-01-21 04:37:10
acitoolkit|0.4||0|0|2021-01-21 04:37:10
ackeras|0.1.1||0|0|2021-01-21 04:37:10
ackg|0.0.5||0|0|2021-01-21 04:37:10
```

## Data being tracked

- Name, Version, Upload Time
- Direct requirements (`requires_dist`)
- Extra requirements (`requires_extras`)
- Python requirements (`requires_python`)
- Trove classifiers (`classifiers`)
- Yanked versions (`yanked`)
- Wheel data (`build_tag`, `python_tags`, `abi_tags`, `platform_tags`)
- Maintainers on PyPI
- URLs used by packages
- OpenSSF scorecard data
- Google Assured OSS

### Database Schemas

```sql
-- Packages --
CREATE TABLE packages (
    name STRING,
    version STRING,
    requires_python STRING,
    yanked BOOLEAN DEFAULT FALSE,
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

-- Dependencies --
CREATE TABLE deps (
    package_name STRING,
    extra STRING DEFAULT NULL,
    dep_name STRING,
    dep_specifier STRING,
    PRIMARY KEY (package_name, dep_name, dep_specifier)
);

-- Wheel data --
CREATE TABLE wheels (
    package_name STRING,
    filename STRING,
    build STRING,
    python STRING,
    abi STRING,
    platform STRING,
    uploaded_at TIMESTAMP,
    PRIMARY KEY (package_name, filename)
);

-- Maintainer data --
CREATE TABLE maintainers (
    name STRING,
    package_name STRING
);

-- Package URLs --
CREATE TABLE package_urls (
    package_name STRING,
    name STRING,
    url STRING,
    public_suffix STRING
)

-- OpenSSF Scorecard --
CREATE TABLE scorecard_checks (
    package_name STRING,
    name STRING,
    score INTEGER
)

-- Trove Classifiers --
CREATE TABLE classifiers (
    package_name TEXT,
    name TEXT,
    PRIMARY KEY (package_name, name),
    FOREIGN KEY (package_name) REFERENCES packages(name)
)
```

### Download data

Downloads are grabbed from https://github.com/hugovk/top-pypi-packages but only available for the top 5,000 packages.

## Running locally

```
$ docker build -t pypi-data .
$ docker run --rm pypi-data
```

## License

Apache-2.0
