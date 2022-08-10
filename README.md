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
- Yanked versions (`yanked`)
- Wheel data (`python_tags`, `abi_tags`, `platform_tags`)
- Maintainers on PyPI
- URLs used by packages
- OpenSSF scorecard data

### Database Schemas

```sql
-- Packages --
CREATE TABLE packages (
    name STRING,
    version STRING,
    requires_python STRING,
    yanked BOOLEAN DEFAULT FALSE,
    has_binary_wheel BOOLEAN,
    uploaded_at TIMESTAMP,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    downloads INTEGER,
    scorecard_overall FLOAT,
    PRIMARY KEY (name, version)
);

-- Dependencies --
CREATE TABLE deps (
    name STRING,
    version STRING,
    extra STRING DEFAULT NULL,
    dep_name STRING,
    dep_specifier STRING,
    PRIMARY KEY (name, version, dep_name, dep_specifier)
);

-- Wheel data --
CREATE TABLE wheels (
    name STRING,
    version STRING,
    filename STRING,
    python STRING,
    abi STRING,
    platform STRING
);

-- Maintainer data --
CREATE TABLE maintainers (
    name STRING,
    package_name STRING
);

-- Package URLs --
CREATE TABLE package_urls (
    package_name STRING,
    url STRING,
    public_suffix STRING
)

-- OpenSSF Scorecard --
CREATE TABLE scorecard_checks (
    package_name STRING,
    name STRING,
    score INTEGER
)
```

### Download data

Downloads are grabbed manually from BigQuery with this query:

```sql
SELECT file.project, COUNT(*) AS downloads
FROM `bigquery-public-data.pypi.file_downloads`
WHERE (
  DATE(timestamp)
  BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
  AND CURRENT_DATE()
)
GROUP BY file.project
ORDER BY downloads DESC;
```

The results are stored in `downloads.csv`.

## Running locally

```
$ docker build -t pypi-data .
$ docker run --rm pypi-data
```

## License

Apache-2.0
