# [apache-airflow](https://pypi.org/project/apache-airflow)

## Dependencies
- [alembic (<2.0,>=1.2)](packages/a/alembic.md)
- [argcomplete (~=1.10)](packages/a/argcomplete.md)
- [attrs (<21.0,>=20.0)](packages/a/attrs.md)
- [cached-property (~=1.5)](packages/c/cached-property.md)
- [cattrs (<1.1.0,>=1.0); python_version<='3.6'](packages/c/cattrs.md)
- [cattrs (<2.0,>=1.0); python_version>'3.6'](packages/c/cattrs.md)
- [colorlog (==4.0.2)](packages/c/colorlog.md)
- [connexion[flask,swagger-ui] (<3,>=2.6.0)](packages/c/connexion.md)
- [croniter (<0.4,>=0.3.17)](packages/c/croniter.md)
- [cryptography (>=0.9.3)](packages/c/cryptography.md)
- [dill (<0.4,>=0.2.2)](packages/d/dill.md)
- [flask (<2.0,>=1.1.0)](packages/f/flask.md)
- [flask-appbuilder (~=3.1.1)](packages/f/flask-appbuilder.md)
- [flask-caching (<2.0.0,>=1.5.0)](packages/f/flask-caching.md)
- [flask-login (<0.5,>=0.3)](packages/f/flask-login.md)
- [flask-swagger (==0.2.13)](packages/f/flask-swagger.md)
- [flask-wtf (<0.15,>=0.14.3)](packages/f/flask-wtf.md)
- [funcsigs (<2.0.0,>=1.0.0)](packages/f/funcsigs.md)
- [graphviz (>=0.12)](packages/g/graphviz.md)
- [gunicorn (<20.0,>=19.5.0)](packages/g/gunicorn.md)
- [iso8601 (>=0.1.12)](packages/i/iso8601.md)
- [jinja2 (<2.12.0,>=2.10.1)](packages/j/jinja2.md)
- [json-merge-patch (==0.2)](packages/j/json-merge-patch.md)
- [jsonschema (~=3.0)](packages/j/jsonschema.md)
- [lazy-object-proxy (~=1.3)](packages/l/lazy-object-proxy.md)
- [lockfile (>=0.12.2)](packages/l/lockfile.md)
- [markdown (<4.0,>=2.5.2)](packages/m/markdown.md)
- [markupsafe (<2.0,>=1.1.1)](packages/m/markupsafe.md)
- [marshmallow-oneofschema (>=2.0.1)](packages/m/marshmallow-oneofschema.md)
- [pandas (<2.0,>=0.17.1)](packages/p/pandas.md)
- [pendulum (~=2.0)](packages/p/pendulum.md)
- [pep562 (~=1.0); python_version<'3.7'](packages/p/pep562.md)
- [psutil (<6.0.0,>=4.2.0)](packages/p/psutil.md)
- [pygments (<3.0,>=2.0.1)](packages/p/pygments.md)
- [python-daemon (>=2.1.1)](packages/p/python-daemon.md)
- [python-dateutil (<3,>=2.3)](packages/p/python-dateutil.md)
- [python-nvd3 (~=0.15.0)](packages/p/python-nvd3.md)
- [python-slugify (<5.0,>=3.0.0)](packages/p/python-slugify.md)
- [requests (<3,>=2.20.0)](packages/r/requests.md)
- [rich (==9.2.0)](packages/r/rich.md)
- [setproctitle (<2,>=1.1.8)](packages/s/setproctitle.md)
- [sqlalchemy (<2,>=1.3.18)](packages/s/sqlalchemy.md)
- [sqlalchemy-jsonfield (~=0.9)](packages/s/sqlalchemy-jsonfield.md)
- [tabulate (<0.9,>=0.7.5)](packages/t/tabulate.md)
- [tenacity (~=6.2.0)](packages/t/tenacity.md)
- [termcolor (>=1.1.0)](packages/t/termcolor.md)
- [thrift (>=0.9.2)](packages/t/thrift.md)
- [typing; python_version<'3.6'](packages/t/typing.md)
- [typing-extensions (>=3.7.4); python_version<'3.8'](packages/t/typing-extensions.md)
- [tzlocal (<2.0.0,>=1.4)](packages/t/tzlocal.md)
- [unicodecsv (>=0.14.1)](packages/u/unicodecsv.md)
- [werkzeug (>=1.0.1,~=1.0)](packages/w/werkzeug.md)


## Extras

### all_dbs
- [apache-airflow-providers-apache-cassandra; extra=='all_dbs'](packages/a/apache-airflow-providers-apache-cassandra.md)
- [apache-airflow-providers-apache-druid; extra=='all_dbs'](packages/a/apache-airflow-providers-apache-druid.md)
- [apache-airflow-providers-apache-hdfs; extra=='all_dbs'](packages/a/apache-airflow-providers-apache-hdfs.md)
- [apache-airflow-providers-apache-hive; extra=='all_dbs'](packages/a/apache-airflow-providers-apache-hive.md)
- [apache-airflow-providers-apache-pinot; extra=='all_dbs'](packages/a/apache-airflow-providers-apache-pinot.md)
- [apache-airflow-providers-cloudant; extra=='all_dbs'](packages/a/apache-airflow-providers-cloudant.md)
- [apache-airflow-providers-exasol; extra=='all_dbs'](packages/a/apache-airflow-providers-exasol.md)
- [apache-airflow-providers-microsoft-mssql; extra=='all_dbs'](packages/a/apache-airflow-providers-microsoft-mssql.md)
- [apache-airflow-providers-mongo; extra=='all_dbs'](packages/a/apache-airflow-providers-mongo.md)
- [apache-airflow-providers-mysql; extra=='all_dbs'](packages/a/apache-airflow-providers-mysql.md)
- [apache-airflow-providers-postgres; extra=='all_dbs'](packages/a/apache-airflow-providers-postgres.md)
- [apache-airflow-providers-presto; extra=='all_dbs'](packages/a/apache-airflow-providers-presto.md)
- [apache-airflow-providers-vertica; extra=='all_dbs'](packages/a/apache-airflow-providers-vertica.md)
- [cassandra-driver (<3.21.0,>=3.13.0); extra=='all_dbs'](packages/c/cassandra-driver.md)
- [cloudant (>=2.0); extra=='all_dbs'](packages/c/cloudant.md)
- [dnspython (<2.0.0,>=1.13.0); extra=='all_dbs'](packages/d/dnspython.md)
- [hmsclient (>=0.1.0); extra=='all_dbs'](packages/h/hmsclient.md)
- [mysql-connector-python (<=8.0.18,>=8.0.11); extra=='all_dbs'](packages/m/mysql-connector-python.md)
- [mysqlclient (<1.4,>=1.3.6); extra=='all_dbs'](packages/m/mysqlclient.md)
- [pinotdb (==0.1.1); extra=='all_dbs'](packages/p/pinotdb.md)
- [presto-python-client (<0.8,>=0.7.0); extra=='all_dbs'](packages/p/presto-python-client.md)
- [psycopg2-binary (>=2.7.4); extra=='all_dbs'](packages/p/psycopg2-binary.md)
- [pydruid (>=0.4.1); extra=='all_dbs'](packages/p/pydruid.md)
- [pyexasol (<1.0.0,>=0.5.1); extra=='all_dbs'](packages/p/pyexasol.md)
- [pyhive[hive] (>=0.6.0); extra=='all_dbs'](packages/p/pyhive.md)
- [pymongo (>=3.6.0); extra=='all_dbs'](packages/p/pymongo.md)
- [pymssql (>=2.1.5,~=2.1); extra=='all_dbs'](packages/p/pymssql.md)
- [snakebite-py3; extra=='all_dbs'](packages/s/snakebite-py3.md)
- [vertica-python (>=0.5.1); extra=='all_dbs'](packages/v/vertica-python.md)

### amazon
- [apache-airflow-providers-amazon; extra=='amazon'](packages/a/apache-airflow-providers-amazon.md)
- [boto3 (<2.0.0,>=1.12.0); extra=='amazon'](packages/b/boto3.md)
- [watchtower (~=0.7.3); extra=='amazon'](packages/w/watchtower.md)

### apache.atlas
- [atlasclient (>=0.1.2); extra=='apache.atlas'](packages/a/atlasclient.md)

### apache.beam
- [apache-beam[gcp]; extra=='apache.beam'](packages/a/apache-beam.md)

### apache.cassandra
- [apache-airflow-providers-apache-cassandra; extra=='apache.cassandra'](packages/a/apache-airflow-providers-apache-cassandra.md)
- [cassandra-driver (<3.21.0,>=3.13.0); extra=='apache.cassandra'](packages/c/cassandra-driver.md)

### apache.druid
- [apache-airflow-providers-apache-druid; extra=='apache.druid'](packages/a/apache-airflow-providers-apache-druid.md)
- [pydruid (>=0.4.1); extra=='apache.druid'](packages/p/pydruid.md)

### apache.hdfs
- [apache-airflow-providers-apache-hdfs; extra=='apache.hdfs'](packages/a/apache-airflow-providers-apache-hdfs.md)
- [snakebite-py3; extra=='apache.hdfs'](packages/s/snakebite-py3.md)

### apache.hive
- [apache-airflow-providers-apache-hive; extra=='apache.hive'](packages/a/apache-airflow-providers-apache-hive.md)
- [hmsclient (>=0.1.0); extra=='apache.hive'](packages/h/hmsclient.md)
- [pyhive[hive] (>=0.6.0); extra=='apache.hive'](packages/p/pyhive.md)

### apache.kylin
- [apache-airflow-providers-apache-kylin; extra=='apache.kylin'](packages/a/apache-airflow-providers-apache-kylin.md)
- [kylinpy (>=2.6); extra=='apache.kylin'](packages/k/kylinpy.md)

### apache.pinot
- [apache-airflow-providers-apache-pinot; extra=='apache.pinot'](packages/a/apache-airflow-providers-apache-pinot.md)
- [pinotdb (==0.1.1); extra=='apache.pinot'](packages/p/pinotdb.md)

### apache.spark
- [apache-airflow-providers-apache-spark; extra=='apache.spark'](packages/a/apache-airflow-providers-apache-spark.md)
- [pyspark; extra=='apache.spark'](packages/p/pyspark.md)

### apache.webhdfs
- [apache-airflow-providers-apache-hdfs; extra=='apache.webhdfs'](packages/a/apache-airflow-providers-apache-hdfs.md)
- [hdfs[avro,dataframe,kerberos] (>=2.0.4); extra=='apache.webhdfs'](packages/h/hdfs.md)

### async
- [eventlet (>=0.9.7); extra=='async'](packages/e/eventlet.md)
- [gevent (>=0.13); extra=='async'](packages/g/gevent.md)
- [greenlet (>=0.4.9); extra=='async'](packages/g/greenlet.md)

### atlas
- [atlasclient (>=0.1.2); extra=='atlas'](packages/a/atlasclient.md)

### aws
- [apache-airflow-providers-amazon; extra=='aws'](packages/a/apache-airflow-providers-amazon.md)
- [boto3 (<2.0.0,>=1.12.0); extra=='aws'](packages/b/boto3.md)
- [watchtower (~=0.7.3); extra=='aws'](packages/w/watchtower.md)

### azure
- [apache-airflow-providers-microsoft-azure; extra=='azure'](packages/a/apache-airflow-providers-microsoft-azure.md)
- [azure-batch (>=8.0.0); extra=='azure'](packages/a/azure-batch.md)
- [azure-cosmos (<4,>=3.0.1); extra=='azure'](packages/a/azure-cosmos.md)
- [azure-datalake-store (>=0.0.45); extra=='azure'](packages/a/azure-datalake-store.md)
- [azure-identity (>=1.3.1); extra=='azure'](packages/a/azure-identity.md)
- [azure-keyvault (>=4.1.0); extra=='azure'](packages/a/azure-keyvault.md)
- [azure-kusto-data (<0.1,>=0.0.43); extra=='azure'](packages/a/azure-kusto-data.md)
- [azure-mgmt-containerinstance (<2.0,>=1.5.0); extra=='azure'](packages/a/azure-mgmt-containerinstance.md)
- [azure-mgmt-datalake-store (>=0.5.0); extra=='azure'](packages/a/azure-mgmt-datalake-store.md)
- [azure-mgmt-resource (>=2.2.0); extra=='azure'](packages/a/azure-mgmt-resource.md)
- [azure-storage (<0.37.0,>=0.34.0); extra=='azure'](packages/a/azure-storage.md)
- [azure-storage-blob (<12.0); extra=='azure'](packages/a/azure-storage-blob.md)

### cassandra
- [apache-airflow-providers-apache-cassandra; extra=='cassandra'](packages/a/apache-airflow-providers-apache-cassandra.md)
- [cassandra-driver (<3.21.0,>=3.13.0); extra=='cassandra'](packages/c/cassandra-driver.md)

### celery
- [apache-airflow-providers-celery; extra=='celery'](packages/a/apache-airflow-providers-celery.md)
- [celery (~=4.4.2); extra=='celery'](packages/c/celery.md)
- [flower (<1.0,>=0.7.3); extra=='celery'](packages/f/flower.md)
- [vine (~=1.3); extra=='celery'](packages/v/vine.md)

### cgroups
- [cgroupspy (>=0.1.4); extra=='cgroups'](packages/c/cgroupspy.md)

### cloudant
- [apache-airflow-providers-cloudant; extra=='cloudant'](packages/a/apache-airflow-providers-cloudant.md)
- [cloudant (>=2.0); extra=='cloudant'](packages/c/cloudant.md)

### cncf.kubernetes
- [apache-airflow-providers-cncf-kubernetes; extra=='cncf.kubernetes'](packages/a/apache-airflow-providers-cncf-kubernetes.md)
- [cryptography (>=2.0.0); extra=='cncf.kubernetes'](packages/c/cryptography.md)
- [kubernetes (<12.0.0,>=3.0.0); extra=='cncf.kubernetes'](packages/k/kubernetes.md)

### dask
- [cloudpickle (<1.5.0,>=1.4.1); extra=='dask'](packages/c/cloudpickle.md)
- [distributed (<2.20,>=2.11.1); extra=='dask'](packages/d/distributed.md)

### databricks
- [apache-airflow-providers-databricks; extra=='databricks'](packages/a/apache-airflow-providers-databricks.md)
- [requests (<3,>=2.20.0); extra=='databricks'](packages/r/requests.md)

### datadog
- [apache-airflow-providers-datadog; extra=='datadog'](packages/a/apache-airflow-providers-datadog.md)
- [datadog (>=0.14.0); extra=='datadog'](packages/d/datadog.md)

### devel_ci
- [amqp; extra=='devel_ci'](packages/a/amqp.md)
- [analytics-python (>=1.2.9); extra=='devel_ci'](packages/a/analytics-python.md)
- [apache-airflow-providers-amazon; extra=='devel_ci'](packages/a/apache-airflow-providers-amazon.md)
- [apache-airflow-providers-apache-cassandra; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-cassandra.md)
- [apache-airflow-providers-apache-druid; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-druid.md)
- [apache-airflow-providers-apache-hdfs; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-hdfs.md)
- [apache-airflow-providers-apache-hive; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-hive.md)
- [apache-airflow-providers-apache-kylin; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-kylin.md)
- [apache-airflow-providers-apache-livy; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-livy.md)
- [apache-airflow-providers-apache-pig; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-pig.md)
- [apache-airflow-providers-apache-pinot; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-pinot.md)
- [apache-airflow-providers-apache-spark; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-spark.md)
- [apache-airflow-providers-apache-sqoop; extra=='devel_ci'](packages/a/apache-airflow-providers-apache-sqoop.md)
- [apache-airflow-providers-celery; extra=='devel_ci'](packages/a/apache-airflow-providers-celery.md)
- [apache-airflow-providers-cloudant; extra=='devel_ci'](packages/a/apache-airflow-providers-cloudant.md)
- [apache-airflow-providers-cncf-kubernetes; extra=='devel_ci'](packages/a/apache-airflow-providers-cncf-kubernetes.md)
- [apache-airflow-providers-databricks; extra=='devel_ci'](packages/a/apache-airflow-providers-databricks.md)
- [apache-airflow-providers-datadog; extra=='devel_ci'](packages/a/apache-airflow-providers-datadog.md)
- [apache-airflow-providers-dingding; extra=='devel_ci'](packages/a/apache-airflow-providers-dingding.md)
- [apache-airflow-providers-discord; extra=='devel_ci'](packages/a/apache-airflow-providers-discord.md)
- [apache-airflow-providers-docker; extra=='devel_ci'](packages/a/apache-airflow-providers-docker.md)
- [apache-airflow-providers-elasticsearch; extra=='devel_ci'](packages/a/apache-airflow-providers-elasticsearch.md)
- [apache-airflow-providers-exasol; extra=='devel_ci'](packages/a/apache-airflow-providers-exasol.md)
- [apache-airflow-providers-facebook; extra=='devel_ci'](packages/a/apache-airflow-providers-facebook.md)
- [apache-airflow-providers-ftp; extra=='devel_ci'](packages/a/apache-airflow-providers-ftp.md)
- [apache-airflow-providers-google; extra=='devel_ci'](packages/a/apache-airflow-providers-google.md)
- [apache-airflow-providers-grpc; extra=='devel_ci'](packages/a/apache-airflow-providers-grpc.md)
- [apache-airflow-providers-hashicorp; extra=='devel_ci'](packages/a/apache-airflow-providers-hashicorp.md)
- [apache-airflow-providers-http; extra=='devel_ci'](packages/a/apache-airflow-providers-http.md)
- [apache-airflow-providers-imap; extra=='devel_ci'](packages/a/apache-airflow-providers-imap.md)
- [apache-airflow-providers-jdbc; extra=='devel_ci'](packages/a/apache-airflow-providers-jdbc.md)
- [apache-airflow-providers-jenkins; extra=='devel_ci'](packages/a/apache-airflow-providers-jenkins.md)
- [apache-airflow-providers-jira; extra=='devel_ci'](packages/a/apache-airflow-providers-jira.md)
- [apache-airflow-providers-microsoft-azure; extra=='devel_ci'](packages/a/apache-airflow-providers-microsoft-azure.md)
- [apache-airflow-providers-microsoft-mssql; extra=='devel_ci'](packages/a/apache-airflow-providers-microsoft-mssql.md)
- [apache-airflow-providers-microsoft-winrm; extra=='devel_ci'](packages/a/apache-airflow-providers-microsoft-winrm.md)
- [apache-airflow-providers-mongo; extra=='devel_ci'](packages/a/apache-airflow-providers-mongo.md)
- [apache-airflow-providers-mysql; extra=='devel_ci'](packages/a/apache-airflow-providers-mysql.md)
- [apache-airflow-providers-odbc; extra=='devel_ci'](packages/a/apache-airflow-providers-odbc.md)
- [apache-airflow-providers-openfaas; extra=='devel_ci'](packages/a/apache-airflow-providers-openfaas.md)
- [apache-airflow-providers-opsgenie; extra=='devel_ci'](packages/a/apache-airflow-providers-opsgenie.md)
- [apache-airflow-providers-oracle; extra=='devel_ci'](packages/a/apache-airflow-providers-oracle.md)
- [apache-airflow-providers-pagerduty; extra=='devel_ci'](packages/a/apache-airflow-providers-pagerduty.md)
- [apache-airflow-providers-papermill; extra=='devel_ci'](packages/a/apache-airflow-providers-papermill.md)
- [apache-airflow-providers-plexus; extra=='devel_ci'](packages/a/apache-airflow-providers-plexus.md)
- [apache-airflow-providers-postgres; extra=='devel_ci'](packages/a/apache-airflow-providers-postgres.md)
- [apache-airflow-providers-presto; extra=='devel_ci'](packages/a/apache-airflow-providers-presto.md)
- [apache-airflow-providers-qubole; extra=='devel_ci'](packages/a/apache-airflow-providers-qubole.md)
- [apache-airflow-providers-redis; extra=='devel_ci'](packages/a/apache-airflow-providers-redis.md)
- [apache-airflow-providers-salesforce; extra=='devel_ci'](packages/a/apache-airflow-providers-salesforce.md)
- [apache-airflow-providers-samba; extra=='devel_ci'](packages/a/apache-airflow-providers-samba.md)
- [apache-airflow-providers-segment; extra=='devel_ci'](packages/a/apache-airflow-providers-segment.md)
- [apache-airflow-providers-sendgrid; extra=='devel_ci'](packages/a/apache-airflow-providers-sendgrid.md)
- [apache-airflow-providers-sftp; extra=='devel_ci'](packages/a/apache-airflow-providers-sftp.md)
- [apache-airflow-providers-singularity; extra=='devel_ci'](packages/a/apache-airflow-providers-singularity.md)
- [apache-airflow-providers-slack; extra=='devel_ci'](packages/a/apache-airflow-providers-slack.md)
- [apache-airflow-providers-snowflake; extra=='devel_ci'](packages/a/apache-airflow-providers-snowflake.md)
- [apache-airflow-providers-sqlite; extra=='devel_ci'](packages/a/apache-airflow-providers-sqlite.md)
- [apache-airflow-providers-ssh; extra=='devel_ci'](packages/a/apache-airflow-providers-ssh.md)
- [apache-airflow-providers-vertica; extra=='devel_ci'](packages/a/apache-airflow-providers-vertica.md)
- [apache-airflow-providers-yandex; extra=='devel_ci'](packages/a/apache-airflow-providers-yandex.md)
- [apache-airflow-providers-zendesk; extra=='devel_ci'](packages/a/apache-airflow-providers-zendesk.md)
- [arrow (>=0.16.0); extra=='devel_ci'](packages/a/arrow.md)
- [atlasclient (>=0.1.2); extra=='devel_ci'](packages/a/atlasclient.md)
- [azure-batch (>=8.0.0); extra=='devel_ci'](packages/a/azure-batch.md)
- [azure-cosmos (<4,>=3.0.1); extra=='devel_ci'](packages/a/azure-cosmos.md)
- [azure-datalake-store (>=0.0.45); extra=='devel_ci'](packages/a/azure-datalake-store.md)
- [azure-identity (>=1.3.1); extra=='devel_ci'](packages/a/azure-identity.md)
- [azure-keyvault (>=4.1.0); extra=='devel_ci'](packages/a/azure-keyvault.md)
- [azure-kusto-data (<0.1,>=0.0.43); extra=='devel_ci'](packages/a/azure-kusto-data.md)
- [azure-mgmt-containerinstance (<2.0,>=1.5.0); extra=='devel_ci'](packages/a/azure-mgmt-containerinstance.md)
- [azure-mgmt-datalake-store (>=0.5.0); extra=='devel_ci'](packages/a/azure-mgmt-datalake-store.md)
- [azure-mgmt-resource (>=2.2.0); extra=='devel_ci'](packages/a/azure-mgmt-resource.md)
- [azure-storage (<0.37.0,>=0.34.0); extra=='devel_ci'](packages/a/azure-storage.md)
- [azure-storage-blob (<12.0); extra=='devel_ci'](packages/a/azure-storage-blob.md)
- [bcrypt (>=2.0.0); extra=='devel_ci'](packages/b/bcrypt.md)
- [beautifulsoup4 (~=4.7.1); extra=='devel_ci'](packages/b/beautifulsoup4.md)
- [black; extra=='devel_ci'](packages/b/black.md)
- [blinker (>=1.1); extra=='devel_ci'](packages/b/blinker.md)
- [blinker; extra=='devel_ci'](packages/b/blinker.md)
- [boto3 (<2.0.0,>=1.12.0); extra=='devel_ci'](packages/b/boto3.md)
- [bowler; extra=='devel_ci'](packages/b/bowler.md)
- [cassandra-driver (<3.21.0,>=3.13.0); extra=='devel_ci'](packages/c/cassandra-driver.md)
- [celery (~=4.4.2); extra=='devel_ci'](packages/c/celery.md)
- [cgroupspy (>=0.1.4); extra=='devel_ci'](packages/c/cgroupspy.md)
- [click (~=7.1); extra=='devel_ci'](packages/c/click.md)
- [cloudant (>=2.0); extra=='devel_ci'](packages/c/cloudant.md)
- [cloudpickle (<1.5.0,>=1.4.1); extra=='devel_ci'](packages/c/cloudpickle.md)
- [contextdecorator; (python_version<'3.4') and extra=='devel_ci'](packages/c/contextdecorator.md)
- [coverage; extra=='devel_ci'](packages/c/coverage.md)
- [cryptography (>=2.0.0); extra=='devel_ci'](packages/c/cryptography.md)
- [cx-oracle (>=5.1.2); extra=='devel_ci'](packages/c/cx-oracle.md)
- [datadog (>=0.14.0); extra=='devel_ci'](packages/d/datadog.md)
- [distributed (<2.20,>=2.11.1); extra=='devel_ci'](packages/d/distributed.md)
- [dnspython (<2.0.0,>=1.13.0); extra=='devel_ci'](packages/d/dnspython.md)
- [docker (~=3.0); extra=='devel_ci'](packages/d/docker.md)
- [docutils; extra=='devel_ci'](packages/d/docutils.md)
- [elasticsearch (<7.6.0,>7); extra=='devel_ci'](packages/e/elasticsearch.md)
- [elasticsearch-dbapi (==0.1.0); extra=='devel_ci'](packages/e/elasticsearch-dbapi.md)
- [elasticsearch-dsl (>=5.0.0); extra=='devel_ci'](packages/e/elasticsearch-dsl.md)
- [eventlet (>=0.9.7); extra=='devel_ci'](packages/e/eventlet.md)
- [facebook-business (>=6.0.2); extra=='devel_ci'](packages/f/facebook-business.md)
- [flake8 (>=3.6.0); extra=='devel_ci'](packages/f/flake8.md)
- [flake8-colors; extra=='devel_ci'](packages/f/flake8-colors.md)
- [flaky; extra=='devel_ci'](packages/f/flaky.md)
- [flask-bcrypt (>=0.7.1); extra=='devel_ci'](packages/f/flask-bcrypt.md)
- [flask-oauthlib (<0.9.6,>=0.9.1); extra=='devel_ci'](packages/f/flask-oauthlib.md)
- [flower (<1.0,>=0.7.3); extra=='devel_ci'](packages/f/flower.md)
- [freezegun; extra=='devel_ci'](packages/f/freezegun.md)
- [gevent (>=0.13); extra=='devel_ci'](packages/g/gevent.md)
- [github3.py; extra=='devel_ci'](packages/g/github3.py.md)
- [gitpython; extra=='devel_ci'](packages/g/gitpython.md)
- [google-ads (>=4.0.0); extra=='devel_ci'](packages/g/google-ads.md)
- [google-api-python-client (<2.0.0,>=1.6.0); extra=='devel_ci'](packages/g/google-api-python-client.md)
- [google-auth (<2.0.0,>=1.0.0); extra=='devel_ci'](packages/g/google-auth.md)
- [google-auth (<2.0.0dev,>=1.0.0); extra=='devel_ci'](packages/g/google-auth.md)
- [google-auth-httplib2 (>=0.0.1); extra=='devel_ci'](packages/g/google-auth-httplib2.md)
- [google-cloud-automl (<2.0.0,>=0.4.0); extra=='devel_ci'](packages/g/google-cloud-automl.md)
- [google-cloud-bigquery-datatransfer (<2.0.0,>=0.4.0); extra=='devel_ci'](packages/g/google-cloud-bigquery-datatransfer.md)
- [google-cloud-bigtable (<2.0.0,>=1.0.0); extra=='devel_ci'](packages/g/google-cloud-bigtable.md)
- [google-cloud-container (<2.0.0,>=0.1.1); extra=='devel_ci'](packages/g/google-cloud-container.md)
- [google-cloud-datacatalog (<0.8,>=0.5.0); extra=='devel_ci'](packages/g/google-cloud-datacatalog.md)
- [google-cloud-dataproc (<2.0.0,>=1.0.1); extra=='devel_ci'](packages/g/google-cloud-dataproc.md)
- [google-cloud-dlp (<2.0.0,>=0.11.0); extra=='devel_ci'](packages/g/google-cloud-dlp.md)
- [google-cloud-kms (<2.0.0,>=1.2.1); extra=='devel_ci'](packages/g/google-cloud-kms.md)
- [google-cloud-language (<2.0.0,>=1.1.1); extra=='devel_ci'](packages/g/google-cloud-language.md)
- [google-cloud-logging (<2.0.0,>=1.14.0); extra=='devel_ci'](packages/g/google-cloud-logging.md)
- [google-cloud-memcache (>=0.2.0); extra=='devel_ci'](packages/g/google-cloud-memcache.md)
- [google-cloud-monitoring (<2.0.0,>=0.34.0); extra=='devel_ci'](packages/g/google-cloud-monitoring.md)
- [google-cloud-os-login (<2.0.0,>=1.0.0); extra=='devel_ci'](packages/g/google-cloud-os-login.md)
- [google-cloud-pubsub (<2.0.0,>=1.0.0); extra=='devel_ci'](packages/g/google-cloud-pubsub.md)
- [google-cloud-redis (<2.0.0,>=0.3.0); extra=='devel_ci'](packages/g/google-cloud-redis.md)
- [google-cloud-secret-manager (<2.0.0,>=0.2.0); extra=='devel_ci'](packages/g/google-cloud-secret-manager.md)
- [google-cloud-spanner (<2.0.0,>=1.10.0); extra=='devel_ci'](packages/g/google-cloud-spanner.md)
- [google-cloud-speech (<2.0.0,>=0.36.3); extra=='devel_ci'](packages/g/google-cloud-speech.md)
- [google-cloud-storage (<2.0.0,>=1.16); extra=='devel_ci'](packages/g/google-cloud-storage.md)
- [google-cloud-tasks (<2.0.0,>=1.2.1); extra=='devel_ci'](packages/g/google-cloud-tasks.md)
- [google-cloud-texttospeech (<2.0.0,>=0.4.0); extra=='devel_ci'](packages/g/google-cloud-texttospeech.md)
- [google-cloud-translate (<2.0.0,>=1.5.0); extra=='devel_ci'](packages/g/google-cloud-translate.md)
- [google-cloud-videointelligence (<2.0.0,>=1.7.0); extra=='devel_ci'](packages/g/google-cloud-videointelligence.md)
- [google-cloud-vision (<2.0.0,>=0.35.2); extra=='devel_ci'](packages/g/google-cloud-vision.md)
- [greenlet (>=0.4.9); extra=='devel_ci'](packages/g/greenlet.md)
- [grpcio (>=1.15.0); extra=='devel_ci'](packages/g/grpcio.md)
- [grpcio-gcp (>=0.2.2); extra=='devel_ci'](packages/g/grpcio-gcp.md)
- [hdfs[avro,dataframe,kerberos] (>=2.0.4); extra=='devel_ci'](packages/h/hdfs.md)
- [hmsclient (>=0.1.0); extra=='devel_ci'](packages/h/hmsclient.md)
- [hvac (~=0.10); extra=='devel_ci'](packages/h/hvac.md)
- [ipdb; extra=='devel_ci'](packages/i/ipdb.md)
- [jaydebeapi (>=1.1.1); extra=='devel_ci'](packages/j/jaydebeapi.md)
- [jira (>1.0.7); extra=='devel_ci'](packages/j/jira.md)
- [jira; extra=='devel_ci'](packages/j/jira.md)
- [kubernetes (<12.0.0,>=3.0.0); extra=='devel_ci'](packages/k/kubernetes.md)
- [kylinpy (>=2.6); extra=='devel_ci'](packages/k/kylinpy.md)
- [ldap3 (>=2.5.1); extra=='devel_ci'](packages/l/ldap3.md)
- [mongomock; extra=='devel_ci'](packages/m/mongomock.md)
- [moto (==1.3.14); extra=='devel_ci'](packages/m/moto.md)
- [mypy (==0.770); extra=='devel_ci'](packages/m/mypy.md)
- [mysql-connector-python (<=8.0.18,>=8.0.11); extra=='devel_ci'](packages/m/mysql-connector-python.md)
- [mysqlclient (<1.4,>=1.3.6); extra=='devel_ci'](packages/m/mysqlclient.md)
- [nteract-scrapbook[all] (>=0.3.1); extra=='devel_ci'](packages/n/nteract-scrapbook.md)
- [oauthlib (!=2.0.3,!=2.0.4,!=2.0.5,<3.0.0,>=1.1.2); extra=='devel_ci'](packages/o/oauthlib.md)
- [pandas-gbq; extra=='devel_ci'](packages/p/pandas-gbq.md)
- [papermill[all] (>=1.2.1); extra=='devel_ci'](packages/p/papermill.md)
- [parameterized; extra=='devel_ci'](packages/p/parameterized.md)
- [paramiko (>=2.6.0); extra=='devel_ci'](packages/p/paramiko.md)
- [paramiko; extra=='devel_ci'](packages/p/paramiko.md)
- [pdpyras (<5,>=4.1.2); extra=='devel_ci'](packages/p/pdpyras.md)
- [pinotdb (==0.1.1); extra=='devel_ci'](packages/p/pinotdb.md)
- [pipdeptree; extra=='devel_ci'](packages/p/pipdeptree.md)
- [pre-commit; extra=='devel_ci'](packages/p/pre-commit.md)
- [presto-python-client (<0.8,>=0.7.0); extra=='devel_ci'](packages/p/presto-python-client.md)
- [psycopg2-binary (>=2.7.4); extra=='devel_ci'](packages/p/psycopg2-binary.md)
- [pydruid (>=0.4.1); extra=='devel_ci'](packages/p/pydruid.md)
- [pyexasol (<1.0.0,>=0.5.1); extra=='devel_ci'](packages/p/pyexasol.md)
- [pyhive[hive] (>=0.6.0); extra=='devel_ci'](packages/p/pyhive.md)
- [pykerberos (>=1.1.13); extra=='devel_ci'](packages/p/pykerberos.md)
- [pylint (==2.5.3); extra=='devel_ci'](packages/p/pylint.md)
- [pymongo (>=3.6.0); extra=='devel_ci'](packages/p/pymongo.md)
- [pymssql (>=2.1.5,~=2.1); extra=='devel_ci'](packages/p/pymssql.md)
- [pyodbc; extra=='devel_ci'](packages/p/pyodbc.md)
- [pyopenssl; extra=='devel_ci'](packages/p/pyopenssl.md)
- [pysftp (>=0.2.9); extra=='devel_ci'](packages/p/pysftp.md)
- [pysftp; extra=='devel_ci'](packages/p/pysftp.md)
- [pysmbclient (>=0.1.3); extra=='devel_ci'](packages/p/pysmbclient.md)
- [pyspark; extra=='devel_ci'](packages/p/pyspark.md)
- [pytest; extra=='devel_ci'](packages/p/pytest.md)
- [pytest-cov; extra=='devel_ci'](packages/p/pytest-cov.md)
- [pytest-instafail; extra=='devel_ci'](packages/p/pytest-instafail.md)
- [pytest-rerunfailures; extra=='devel_ci'](packages/p/pytest-rerunfailures.md)
- [pytest-timeouts; extra=='devel_ci'](packages/p/pytest-timeouts.md)
- [pytest-xdist; extra=='devel_ci'](packages/p/pytest-xdist.md)
- [python-jenkins (>=1.0.0); extra=='devel_ci'](packages/p/python-jenkins.md)
- [pywinrm (~=0.4); extra=='devel_ci'](packages/p/pywinrm.md)
- [pywinrm; extra=='devel_ci'](packages/p/pywinrm.md)
- [qds-sdk (>=1.10.4); extra=='devel_ci'](packages/q/qds-sdk.md)
- [qds-sdk (>=1.9.6); extra=='devel_ci'](packages/q/qds-sdk.md)
- [redis (~=3.2); extra=='devel_ci'](packages/r/redis.md)
- [requests (<2.24.0); extra=='devel_ci'](packages/r/requests.md)
- [requests (<3,>=2.20.0); extra=='devel_ci'](packages/r/requests.md)
- [requests-kerberos (>=0.10.0); extra=='devel_ci'](packages/r/requests-kerberos.md)
- [requests-mock; extra=='devel_ci'](packages/r/requests-mock.md)
- [requests-oauthlib (==1.1.0); extra=='devel_ci'](packages/r/requests-oauthlib.md)
- [sendgrid (<7,>=6.0.0); extra=='devel_ci'](packages/s/sendgrid.md)
- [sentry-sdk (>=0.8.0); extra=='devel_ci'](packages/s/sentry-sdk.md)
- [setuptools; extra=='devel_ci'](packages/s/setuptools.md)
- [simple-salesforce (>=1.0.0); extra=='devel_ci'](packages/s/simple-salesforce.md)
- [slackclient (<3.0.0,>=2.0.0); extra=='devel_ci'](packages/s/slackclient.md)
- [snowflake-connector-python (>=1.5.2); extra=='devel_ci'](packages/s/snowflake-connector-python.md)
- [snowflake-sqlalchemy (>=1.1.0); extra=='devel_ci'](packages/s/snowflake-sqlalchemy.md)
- [sphinx (>=2.1.2); extra=='devel_ci'](packages/s/sphinx.md)
- [sphinx-argparse (>=0.1.13); extra=='devel_ci'](packages/s/sphinx-argparse.md)
- [sphinx-autoapi (==1.0.0); extra=='devel_ci'](packages/s/sphinx-autoapi.md)
- [sphinx-copybutton; extra=='devel_ci'](packages/s/sphinx-copybutton.md)
- [sphinx-jinja (~=1.1); extra=='devel_ci'](packages/s/sphinx-jinja.md)
- [sphinx-rtd-theme (>=0.1.6); extra=='devel_ci'](packages/s/sphinx-rtd-theme.md)
- [sphinxcontrib-httpdomain (>=1.7.0); extra=='devel_ci'](packages/s/sphinxcontrib-httpdomain.md)
- [sphinxcontrib-redoc (>=1.6.0); extra=='devel_ci'](packages/s/sphinxcontrib-redoc.md)
- [sphinxcontrib-spelling (==5.2.1); extra=='devel_ci'](packages/s/sphinxcontrib-spelling.md)
- [spython (>=0.0.56); extra=='devel_ci'](packages/s/spython.md)
- [sshtunnel (<0.2,>=0.1.4); extra=='devel_ci'](packages/s/sshtunnel.md)
- [statsd (<4.0,>=3.3.0); extra=='devel_ci'](packages/s/statsd.md)
- [tableauserverclient (~=0.12); extra=='devel_ci'](packages/t/tableauserverclient.md)
- [testfixtures; extra=='devel_ci'](packages/t/testfixtures.md)
- [thrift-sasl (>=0.2.0); extra=='devel_ci'](packages/t/thrift-sasl.md)
- [vertica-python (>=0.5.1); extra=='devel_ci'](packages/v/vertica-python.md)
- [vine (~=1.3); extra=='devel_ci'](packages/v/vine.md)
- [virtualenv; extra=='devel_ci'](packages/v/virtualenv.md)
- [watchtower (~=0.7.3); extra=='devel_ci'](packages/w/watchtower.md)
- [wheel; extra=='devel_ci'](packages/w/wheel.md)
- [yamllint; extra=='devel_ci'](packages/y/yamllint.md)
- [yandexcloud (>=0.22.0); extra=='devel_ci'](packages/y/yandexcloud.md)
- [zdesk; extra=='devel_ci'](packages/z/zdesk.md)

### devel_hadoop
- [apache-airflow-providers-apache-hdfs; extra=='devel_hadoop'](packages/a/apache-airflow-providers-apache-hdfs.md)
- [apache-airflow-providers-apache-hive; extra=='devel_hadoop'](packages/a/apache-airflow-providers-apache-hive.md)
- [apache-airflow-providers-presto; extra=='devel_hadoop'](packages/a/apache-airflow-providers-presto.md)
- [bcrypt (>=2.0.0); extra=='devel_hadoop'](packages/b/bcrypt.md)
- [beautifulsoup4 (~=4.7.1); extra=='devel_hadoop'](packages/b/beautifulsoup4.md)
- [black; extra=='devel_hadoop'](packages/b/black.md)
- [blinker; extra=='devel_hadoop'](packages/b/blinker.md)
- [bowler; extra=='devel_hadoop'](packages/b/bowler.md)
- [cgroupspy (>=0.1.4); extra=='devel_hadoop'](packages/c/cgroupspy.md)
- [click (~=7.1); extra=='devel_hadoop'](packages/c/click.md)
- [contextdecorator; (python_version<'3.4') and extra=='devel_hadoop'](packages/c/contextdecorator.md)
- [coverage; extra=='devel_hadoop'](packages/c/coverage.md)
- [cryptography (>=2.0.0); extra=='devel_hadoop'](packages/c/cryptography.md)
- [docutils; extra=='devel_hadoop'](packages/d/docutils.md)
- [flake8 (>=3.6.0); extra=='devel_hadoop'](packages/f/flake8.md)
- [flake8-colors; extra=='devel_hadoop'](packages/f/flake8-colors.md)
- [flaky; extra=='devel_hadoop'](packages/f/flaky.md)
- [flask-bcrypt (>=0.7.1); extra=='devel_hadoop'](packages/f/flask-bcrypt.md)
- [freezegun; extra=='devel_hadoop'](packages/f/freezegun.md)
- [github3.py; extra=='devel_hadoop'](packages/g/github3.py.md)
- [gitpython; extra=='devel_hadoop'](packages/g/gitpython.md)
- [hdfs[avro,dataframe,kerberos] (>=2.0.4); extra=='devel_hadoop'](packages/h/hdfs.md)
- [hmsclient (>=0.1.0); extra=='devel_hadoop'](packages/h/hmsclient.md)
- [ipdb; extra=='devel_hadoop'](packages/i/ipdb.md)
- [jira; extra=='devel_hadoop'](packages/j/jira.md)
- [kubernetes (<12.0.0,>=3.0.0); extra=='devel_hadoop'](packages/k/kubernetes.md)
- [mongomock; extra=='devel_hadoop'](packages/m/mongomock.md)
- [moto (==1.3.14); extra=='devel_hadoop'](packages/m/moto.md)
- [mypy (==0.770); extra=='devel_hadoop'](packages/m/mypy.md)
- [mysql-connector-python (<=8.0.18,>=8.0.11); extra=='devel_hadoop'](packages/m/mysql-connector-python.md)
- [mysqlclient (<1.4,>=1.3.6); extra=='devel_hadoop'](packages/m/mysqlclient.md)
- [parameterized; extra=='devel_hadoop'](packages/p/parameterized.md)
- [paramiko; extra=='devel_hadoop'](packages/p/paramiko.md)
- [pipdeptree; extra=='devel_hadoop'](packages/p/pipdeptree.md)
- [pre-commit; extra=='devel_hadoop'](packages/p/pre-commit.md)
- [presto-python-client (<0.8,>=0.7.0); extra=='devel_hadoop'](packages/p/presto-python-client.md)
- [pyhive[hive] (>=0.6.0); extra=='devel_hadoop'](packages/p/pyhive.md)
- [pykerberos (>=1.1.13); extra=='devel_hadoop'](packages/p/pykerberos.md)
- [pylint (==2.5.3); extra=='devel_hadoop'](packages/p/pylint.md)
- [pysftp; extra=='devel_hadoop'](packages/p/pysftp.md)
- [pytest; extra=='devel_hadoop'](packages/p/pytest.md)
- [pytest-cov; extra=='devel_hadoop'](packages/p/pytest-cov.md)
- [pytest-instafail; extra=='devel_hadoop'](packages/p/pytest-instafail.md)
- [pytest-rerunfailures; extra=='devel_hadoop'](packages/p/pytest-rerunfailures.md)
- [pytest-timeouts; extra=='devel_hadoop'](packages/p/pytest-timeouts.md)
- [pytest-xdist; extra=='devel_hadoop'](packages/p/pytest-xdist.md)
- [pywinrm; extra=='devel_hadoop'](packages/p/pywinrm.md)
- [qds-sdk (>=1.9.6); extra=='devel_hadoop'](packages/q/qds-sdk.md)
- [requests-kerberos (>=0.10.0); extra=='devel_hadoop'](packages/r/requests-kerberos.md)
- [requests-mock; extra=='devel_hadoop'](packages/r/requests-mock.md)
- [setuptools; extra=='devel_hadoop'](packages/s/setuptools.md)
- [snakebite-py3; extra=='devel_hadoop'](packages/s/snakebite-py3.md)
- [sphinx (>=2.1.2); extra=='devel_hadoop'](packages/s/sphinx.md)
- [sphinx-argparse (>=0.1.13); extra=='devel_hadoop'](packages/s/sphinx-argparse.md)
- [sphinx-autoapi (==1.0.0); extra=='devel_hadoop'](packages/s/sphinx-autoapi.md)
- [sphinx-copybutton; extra=='devel_hadoop'](packages/s/sphinx-copybutton.md)
- [sphinx-jinja (~=1.1); extra=='devel_hadoop'](packages/s/sphinx-jinja.md)
- [sphinx-rtd-theme (>=0.1.6); extra=='devel_hadoop'](packages/s/sphinx-rtd-theme.md)
- [sphinxcontrib-httpdomain (>=1.7.0); extra=='devel_hadoop'](packages/s/sphinxcontrib-httpdomain.md)
- [sphinxcontrib-redoc (>=1.6.0); extra=='devel_hadoop'](packages/s/sphinxcontrib-redoc.md)
- [sphinxcontrib-spelling (==5.2.1); extra=='devel_hadoop'](packages/s/sphinxcontrib-spelling.md)
- [testfixtures; extra=='devel_hadoop'](packages/t/testfixtures.md)
- [thrift-sasl (>=0.2.0); extra=='devel_hadoop'](packages/t/thrift-sasl.md)
- [wheel; extra=='devel_hadoop'](packages/w/wheel.md)
- [yamllint; extra=='devel_hadoop'](packages/y/yamllint.md)

### docker
- [apache-airflow-providers-docker; extra=='docker'](packages/a/apache-airflow-providers-docker.md)
- [docker (~=3.0); extra=='docker'](packages/d/docker.md)

### druid
- [apache-airflow-providers-apache-druid; extra=='druid'](packages/a/apache-airflow-providers-apache-druid.md)
- [pydruid (>=0.4.1); extra=='druid'](packages/p/pydruid.md)

### elasticsearch
- [apache-airflow-providers-elasticsearch; extra=='elasticsearch'](packages/a/apache-airflow-providers-elasticsearch.md)
- [elasticsearch (<7.6.0,>7); extra=='elasticsearch'](packages/e/elasticsearch.md)
- [elasticsearch-dbapi (==0.1.0); extra=='elasticsearch'](packages/e/elasticsearch-dbapi.md)
- [elasticsearch-dsl (>=5.0.0); extra=='elasticsearch'](packages/e/elasticsearch-dsl.md)

### exasol
- [apache-airflow-providers-exasol; extra=='exasol'](packages/a/apache-airflow-providers-exasol.md)
- [pyexasol (<1.0.0,>=0.5.1); extra=='exasol'](packages/p/pyexasol.md)

### facebook
- [apache-airflow-providers-facebook; extra=='facebook'](packages/a/apache-airflow-providers-facebook.md)
- [facebook-business (>=6.0.2); extra=='facebook'](packages/f/facebook-business.md)

### gcp
- [apache-airflow-providers-google; extra=='gcp'](packages/a/apache-airflow-providers-google.md)
- [google-ads (>=4.0.0); extra=='gcp'](packages/g/google-ads.md)
- [google-api-python-client (<2.0.0,>=1.6.0); extra=='gcp'](packages/g/google-api-python-client.md)
- [google-auth (<2.0.0,>=1.0.0); extra=='gcp'](packages/g/google-auth.md)
- [google-auth-httplib2 (>=0.0.1); extra=='gcp'](packages/g/google-auth-httplib2.md)
- [google-cloud-automl (<2.0.0,>=0.4.0); extra=='gcp'](packages/g/google-cloud-automl.md)
- [google-cloud-bigquery-datatransfer (<2.0.0,>=0.4.0); extra=='gcp'](packages/g/google-cloud-bigquery-datatransfer.md)
- [google-cloud-bigtable (<2.0.0,>=1.0.0); extra=='gcp'](packages/g/google-cloud-bigtable.md)
- [google-cloud-container (<2.0.0,>=0.1.1); extra=='gcp'](packages/g/google-cloud-container.md)
- [google-cloud-datacatalog (<0.8,>=0.5.0); extra=='gcp'](packages/g/google-cloud-datacatalog.md)
- [google-cloud-dataproc (<2.0.0,>=1.0.1); extra=='gcp'](packages/g/google-cloud-dataproc.md)
- [google-cloud-dlp (<2.0.0,>=0.11.0); extra=='gcp'](packages/g/google-cloud-dlp.md)
- [google-cloud-kms (<2.0.0,>=1.2.1); extra=='gcp'](packages/g/google-cloud-kms.md)
- [google-cloud-language (<2.0.0,>=1.1.1); extra=='gcp'](packages/g/google-cloud-language.md)
- [google-cloud-logging (<2.0.0,>=1.14.0); extra=='gcp'](packages/g/google-cloud-logging.md)
- [google-cloud-memcache (>=0.2.0); extra=='gcp'](packages/g/google-cloud-memcache.md)
- [google-cloud-monitoring (<2.0.0,>=0.34.0); extra=='gcp'](packages/g/google-cloud-monitoring.md)
- [google-cloud-os-login (<2.0.0,>=1.0.0); extra=='gcp'](packages/g/google-cloud-os-login.md)
- [google-cloud-pubsub (<2.0.0,>=1.0.0); extra=='gcp'](packages/g/google-cloud-pubsub.md)
- [google-cloud-redis (<2.0.0,>=0.3.0); extra=='gcp'](packages/g/google-cloud-redis.md)
- [google-cloud-secret-manager (<2.0.0,>=0.2.0); extra=='gcp'](packages/g/google-cloud-secret-manager.md)
- [google-cloud-spanner (<2.0.0,>=1.10.0); extra=='gcp'](packages/g/google-cloud-spanner.md)
- [google-cloud-speech (<2.0.0,>=0.36.3); extra=='gcp'](packages/g/google-cloud-speech.md)
- [google-cloud-storage (<2.0.0,>=1.16); extra=='gcp'](packages/g/google-cloud-storage.md)
- [google-cloud-tasks (<2.0.0,>=1.2.1); extra=='gcp'](packages/g/google-cloud-tasks.md)
- [google-cloud-texttospeech (<2.0.0,>=0.4.0); extra=='gcp'](packages/g/google-cloud-texttospeech.md)
- [google-cloud-translate (<2.0.0,>=1.5.0); extra=='gcp'](packages/g/google-cloud-translate.md)
- [google-cloud-videointelligence (<2.0.0,>=1.7.0); extra=='gcp'](packages/g/google-cloud-videointelligence.md)
- [google-cloud-vision (<2.0.0,>=0.35.2); extra=='gcp'](packages/g/google-cloud-vision.md)
- [grpcio-gcp (>=0.2.2); extra=='gcp'](packages/g/grpcio-gcp.md)
- [pandas-gbq; extra=='gcp'](packages/p/pandas-gbq.md)
- [pyopenssl; extra=='gcp'](packages/p/pyopenssl.md)

### gcp_api
- [apache-airflow-providers-google; extra=='gcp_api'](packages/a/apache-airflow-providers-google.md)
- [google-ads (>=4.0.0); extra=='gcp_api'](packages/g/google-ads.md)
- [google-api-python-client (<2.0.0,>=1.6.0); extra=='gcp_api'](packages/g/google-api-python-client.md)
- [google-auth (<2.0.0,>=1.0.0); extra=='gcp_api'](packages/g/google-auth.md)
- [google-auth-httplib2 (>=0.0.1); extra=='gcp_api'](packages/g/google-auth-httplib2.md)
- [google-cloud-automl (<2.0.0,>=0.4.0); extra=='gcp_api'](packages/g/google-cloud-automl.md)
- [google-cloud-bigquery-datatransfer (<2.0.0,>=0.4.0); extra=='gcp_api'](packages/g/google-cloud-bigquery-datatransfer.md)
- [google-cloud-bigtable (<2.0.0,>=1.0.0); extra=='gcp_api'](packages/g/google-cloud-bigtable.md)
- [google-cloud-container (<2.0.0,>=0.1.1); extra=='gcp_api'](packages/g/google-cloud-container.md)
- [google-cloud-datacatalog (<0.8,>=0.5.0); extra=='gcp_api'](packages/g/google-cloud-datacatalog.md)
- [google-cloud-dataproc (<2.0.0,>=1.0.1); extra=='gcp_api'](packages/g/google-cloud-dataproc.md)
- [google-cloud-dlp (<2.0.0,>=0.11.0); extra=='gcp_api'](packages/g/google-cloud-dlp.md)
- [google-cloud-kms (<2.0.0,>=1.2.1); extra=='gcp_api'](packages/g/google-cloud-kms.md)
- [google-cloud-language (<2.0.0,>=1.1.1); extra=='gcp_api'](packages/g/google-cloud-language.md)
- [google-cloud-logging (<2.0.0,>=1.14.0); extra=='gcp_api'](packages/g/google-cloud-logging.md)
- [google-cloud-memcache (>=0.2.0); extra=='gcp_api'](packages/g/google-cloud-memcache.md)
- [google-cloud-monitoring (<2.0.0,>=0.34.0); extra=='gcp_api'](packages/g/google-cloud-monitoring.md)
- [google-cloud-os-login (<2.0.0,>=1.0.0); extra=='gcp_api'](packages/g/google-cloud-os-login.md)
- [google-cloud-pubsub (<2.0.0,>=1.0.0); extra=='gcp_api'](packages/g/google-cloud-pubsub.md)
- [google-cloud-redis (<2.0.0,>=0.3.0); extra=='gcp_api'](packages/g/google-cloud-redis.md)
- [google-cloud-secret-manager (<2.0.0,>=0.2.0); extra=='gcp_api'](packages/g/google-cloud-secret-manager.md)
- [google-cloud-spanner (<2.0.0,>=1.10.0); extra=='gcp_api'](packages/g/google-cloud-spanner.md)
- [google-cloud-speech (<2.0.0,>=0.36.3); extra=='gcp_api'](packages/g/google-cloud-speech.md)
- [google-cloud-storage (<2.0.0,>=1.16); extra=='gcp_api'](packages/g/google-cloud-storage.md)
- [google-cloud-tasks (<2.0.0,>=1.2.1); extra=='gcp_api'](packages/g/google-cloud-tasks.md)
- [google-cloud-texttospeech (<2.0.0,>=0.4.0); extra=='gcp_api'](packages/g/google-cloud-texttospeech.md)
- [google-cloud-translate (<2.0.0,>=1.5.0); extra=='gcp_api'](packages/g/google-cloud-translate.md)
- [google-cloud-videointelligence (<2.0.0,>=1.7.0); extra=='gcp_api'](packages/g/google-cloud-videointelligence.md)
- [google-cloud-vision (<2.0.0,>=0.35.2); extra=='gcp_api'](packages/g/google-cloud-vision.md)
- [grpcio-gcp (>=0.2.2); extra=='gcp_api'](packages/g/grpcio-gcp.md)
- [pandas-gbq; extra=='gcp_api'](packages/p/pandas-gbq.md)
- [pyopenssl; extra=='gcp_api'](packages/p/pyopenssl.md)

### github_enterprise
- [flask-oauthlib (<0.9.6,>=0.9.1); extra=='github_enterprise'](packages/f/flask-oauthlib.md)
- [oauthlib (!=2.0.3,!=2.0.4,!=2.0.5,<3.0.0,>=1.1.2); extra=='github_enterprise'](packages/o/oauthlib.md)
- [requests-oauthlib (==1.1.0); extra=='github_enterprise'](packages/r/requests-oauthlib.md)

### google
- [apache-airflow-providers-google; extra=='google'](packages/a/apache-airflow-providers-google.md)
- [google-ads (>=4.0.0); extra=='google'](packages/g/google-ads.md)
- [google-api-python-client (<2.0.0,>=1.6.0); extra=='google'](packages/g/google-api-python-client.md)
- [google-auth (<2.0.0,>=1.0.0); extra=='google'](packages/g/google-auth.md)
- [google-auth-httplib2 (>=0.0.1); extra=='google'](packages/g/google-auth-httplib2.md)
- [google-cloud-automl (<2.0.0,>=0.4.0); extra=='google'](packages/g/google-cloud-automl.md)
- [google-cloud-bigquery-datatransfer (<2.0.0,>=0.4.0); extra=='google'](packages/g/google-cloud-bigquery-datatransfer.md)
- [google-cloud-bigtable (<2.0.0,>=1.0.0); extra=='google'](packages/g/google-cloud-bigtable.md)
- [google-cloud-container (<2.0.0,>=0.1.1); extra=='google'](packages/g/google-cloud-container.md)
- [google-cloud-datacatalog (<0.8,>=0.5.0); extra=='google'](packages/g/google-cloud-datacatalog.md)
- [google-cloud-dataproc (<2.0.0,>=1.0.1); extra=='google'](packages/g/google-cloud-dataproc.md)
- [google-cloud-dlp (<2.0.0,>=0.11.0); extra=='google'](packages/g/google-cloud-dlp.md)
- [google-cloud-kms (<2.0.0,>=1.2.1); extra=='google'](packages/g/google-cloud-kms.md)
- [google-cloud-language (<2.0.0,>=1.1.1); extra=='google'](packages/g/google-cloud-language.md)
- [google-cloud-logging (<2.0.0,>=1.14.0); extra=='google'](packages/g/google-cloud-logging.md)
- [google-cloud-memcache (>=0.2.0); extra=='google'](packages/g/google-cloud-memcache.md)
- [google-cloud-monitoring (<2.0.0,>=0.34.0); extra=='google'](packages/g/google-cloud-monitoring.md)
- [google-cloud-os-login (<2.0.0,>=1.0.0); extra=='google'](packages/g/google-cloud-os-login.md)
- [google-cloud-pubsub (<2.0.0,>=1.0.0); extra=='google'](packages/g/google-cloud-pubsub.md)
- [google-cloud-redis (<2.0.0,>=0.3.0); extra=='google'](packages/g/google-cloud-redis.md)
- [google-cloud-secret-manager (<2.0.0,>=0.2.0); extra=='google'](packages/g/google-cloud-secret-manager.md)
- [google-cloud-spanner (<2.0.0,>=1.10.0); extra=='google'](packages/g/google-cloud-spanner.md)
- [google-cloud-speech (<2.0.0,>=0.36.3); extra=='google'](packages/g/google-cloud-speech.md)
- [google-cloud-storage (<2.0.0,>=1.16); extra=='google'](packages/g/google-cloud-storage.md)
- [google-cloud-tasks (<2.0.0,>=1.2.1); extra=='google'](packages/g/google-cloud-tasks.md)
- [google-cloud-texttospeech (<2.0.0,>=0.4.0); extra=='google'](packages/g/google-cloud-texttospeech.md)
- [google-cloud-translate (<2.0.0,>=1.5.0); extra=='google'](packages/g/google-cloud-translate.md)
- [google-cloud-videointelligence (<2.0.0,>=1.7.0); extra=='google'](packages/g/google-cloud-videointelligence.md)
- [google-cloud-vision (<2.0.0,>=0.35.2); extra=='google'](packages/g/google-cloud-vision.md)
- [grpcio-gcp (>=0.2.2); extra=='google'](packages/g/grpcio-gcp.md)
- [pandas-gbq; extra=='google'](packages/p/pandas-gbq.md)
- [pyopenssl; extra=='google'](packages/p/pyopenssl.md)

### google_auth
- [flask-oauthlib (<0.9.6,>=0.9.1); extra=='google_auth'](packages/f/flask-oauthlib.md)
- [oauthlib (!=2.0.3,!=2.0.4,!=2.0.5,<3.0.0,>=1.1.2); extra=='google_auth'](packages/o/oauthlib.md)
- [requests-oauthlib (==1.1.0); extra=='google_auth'](packages/r/requests-oauthlib.md)

### grpc
- [apache-airflow-providers-grpc; extra=='grpc'](packages/a/apache-airflow-providers-grpc.md)
- [google-auth (<2.0.0dev,>=1.0.0); extra=='grpc'](packages/g/google-auth.md)
- [google-auth-httplib2 (>=0.0.1); extra=='grpc'](packages/g/google-auth-httplib2.md)
- [grpcio (>=1.15.0); extra=='grpc'](packages/g/grpcio.md)

### hashicorp
- [apache-airflow-providers-hashicorp; extra=='hashicorp'](packages/a/apache-airflow-providers-hashicorp.md)
- [hvac (~=0.10); extra=='hashicorp'](packages/h/hvac.md)

### hdfs
- [apache-airflow-providers-apache-hdfs; extra=='hdfs'](packages/a/apache-airflow-providers-apache-hdfs.md)
- [snakebite-py3; extra=='hdfs'](packages/s/snakebite-py3.md)

### hive
- [apache-airflow-providers-apache-hive; extra=='hive'](packages/a/apache-airflow-providers-apache-hive.md)
- [hmsclient (>=0.1.0); extra=='hive'](packages/h/hmsclient.md)
- [pyhive[hive] (>=0.6.0); extra=='hive'](packages/p/pyhive.md)

### jdbc
- [apache-airflow-providers-jdbc; extra=='jdbc'](packages/a/apache-airflow-providers-jdbc.md)
- [jaydebeapi (>=1.1.1); extra=='jdbc'](packages/j/jaydebeapi.md)

### jira
- [apache-airflow-providers-jira; extra=='jira'](packages/a/apache-airflow-providers-jira.md)
- [jira (>1.0.7); extra=='jira'](packages/j/jira.md)

### kerberos
- [pykerberos (>=1.1.13); extra=='kerberos'](packages/p/pykerberos.md)
- [requests-kerberos (>=0.10.0); extra=='kerberos'](packages/r/requests-kerberos.md)
- [thrift-sasl (>=0.2.0); extra=='kerberos'](packages/t/thrift-sasl.md)

### kubernetes
- [apache-airflow-providers-cncf-kubernetes; extra=='kubernetes'](packages/a/apache-airflow-providers-cncf-kubernetes.md)
- [cryptography (>=2.0.0); extra=='kubernetes'](packages/c/cryptography.md)
- [kubernetes (<12.0.0,>=3.0.0); extra=='kubernetes'](packages/k/kubernetes.md)

### ldap
- [ldap3 (>=2.5.1); extra=='ldap'](packages/l/ldap3.md)

### microsoft.azure
- [apache-airflow-providers-microsoft-azure; extra=='microsoft.azure'](packages/a/apache-airflow-providers-microsoft-azure.md)
- [azure-batch (>=8.0.0); extra=='microsoft.azure'](packages/a/azure-batch.md)
- [azure-cosmos (<4,>=3.0.1); extra=='microsoft.azure'](packages/a/azure-cosmos.md)
- [azure-datalake-store (>=0.0.45); extra=='microsoft.azure'](packages/a/azure-datalake-store.md)
- [azure-identity (>=1.3.1); extra=='microsoft.azure'](packages/a/azure-identity.md)
- [azure-keyvault (>=4.1.0); extra=='microsoft.azure'](packages/a/azure-keyvault.md)
- [azure-kusto-data (<0.1,>=0.0.43); extra=='microsoft.azure'](packages/a/azure-kusto-data.md)
- [azure-mgmt-containerinstance (<2.0,>=1.5.0); extra=='microsoft.azure'](packages/a/azure-mgmt-containerinstance.md)
- [azure-mgmt-datalake-store (>=0.5.0); extra=='microsoft.azure'](packages/a/azure-mgmt-datalake-store.md)
- [azure-mgmt-resource (>=2.2.0); extra=='microsoft.azure'](packages/a/azure-mgmt-resource.md)
- [azure-storage (<0.37.0,>=0.34.0); extra=='microsoft.azure'](packages/a/azure-storage.md)
- [azure-storage-blob (<12.0); extra=='microsoft.azure'](packages/a/azure-storage-blob.md)

### microsoft.mssql
- [apache-airflow-providers-microsoft-mssql; extra=='microsoft.mssql'](packages/a/apache-airflow-providers-microsoft-mssql.md)
- [pymssql (>=2.1.5,~=2.1); extra=='microsoft.mssql'](packages/p/pymssql.md)

### microsoft.winrm
- [apache-airflow-providers-microsoft-winrm; extra=='microsoft.winrm'](packages/a/apache-airflow-providers-microsoft-winrm.md)
- [pywinrm (~=0.4); extra=='microsoft.winrm'](packages/p/pywinrm.md)

### mongo
- [apache-airflow-providers-mongo; extra=='mongo'](packages/a/apache-airflow-providers-mongo.md)
- [dnspython (<2.0.0,>=1.13.0); extra=='mongo'](packages/d/dnspython.md)
- [pymongo (>=3.6.0); extra=='mongo'](packages/p/pymongo.md)

### mssql
- [apache-airflow-providers-microsoft-mssql; extra=='mssql'](packages/a/apache-airflow-providers-microsoft-mssql.md)
- [pymssql (>=2.1.5,~=2.1); extra=='mssql'](packages/p/pymssql.md)

### mysql
- [apache-airflow-providers-microsoft-mssql; extra=='mysql'](packages/a/apache-airflow-providers-microsoft-mssql.md)
- [mysql-connector-python (<=8.0.18,>=8.0.11); extra=='mysql'](packages/m/mysql-connector-python.md)
- [mysqlclient (<1.4,>=1.3.6); extra=='mysql'](packages/m/mysqlclient.md)

### odbc
- [apache-airflow-providers-odbc; extra=='odbc'](packages/a/apache-airflow-providers-odbc.md)
- [pyodbc; extra=='odbc'](packages/p/pyodbc.md)

### oracle
- [apache-airflow-providers-oracle; extra=='oracle'](packages/a/apache-airflow-providers-oracle.md)
- [cx-oracle (>=5.1.2); extra=='oracle'](packages/c/cx-oracle.md)

### pagerduty
- [apache-airflow-providers-pagerduty; extra=='pagerduty'](packages/a/apache-airflow-providers-pagerduty.md)
- [pdpyras (<5,>=4.1.2); extra=='pagerduty'](packages/p/pdpyras.md)

### papermill
- [apache-airflow-providers-papermill; extra=='papermill'](packages/a/apache-airflow-providers-papermill.md)
- [nteract-scrapbook[all] (>=0.3.1); extra=='papermill'](packages/n/nteract-scrapbook.md)
- [papermill[all] (>=1.2.1); extra=='papermill'](packages/p/papermill.md)

### password
- [bcrypt (>=2.0.0); extra=='password'](packages/b/bcrypt.md)
- [flask-bcrypt (>=0.7.1); extra=='password'](packages/f/flask-bcrypt.md)

### pinot
- [apache-airflow-providers-apache-pinot; extra=='pinot'](packages/a/apache-airflow-providers-apache-pinot.md)
- [pinotdb (==0.1.1); extra=='pinot'](packages/p/pinotdb.md)

### plexus
- [apache-airflow-providers-plexus; extra=='plexus'](packages/a/apache-airflow-providers-plexus.md)
- [arrow (>=0.16.0); extra=='plexus'](packages/a/arrow.md)

### postgres
- [apache-airflow-providers-postgres; extra=='postgres'](packages/a/apache-airflow-providers-postgres.md)
- [psycopg2-binary (>=2.7.4); extra=='postgres'](packages/p/psycopg2-binary.md)

### presto
- [apache-airflow-providers-presto; extra=='presto'](packages/a/apache-airflow-providers-presto.md)
- [presto-python-client (<0.8,>=0.7.0); extra=='presto'](packages/p/presto-python-client.md)

### qds
- [apache-airflow-providers-qubole; extra=='qds'](packages/a/apache-airflow-providers-qubole.md)
- [qds-sdk (>=1.10.4); extra=='qds'](packages/q/qds-sdk.md)

### qubole
- [apache-airflow-providers-qubole; extra=='qubole'](packages/a/apache-airflow-providers-qubole.md)
- [qds-sdk (>=1.10.4); extra=='qubole'](packages/q/qds-sdk.md)

### rabbitmq
- [amqp; extra=='rabbitmq'](packages/a/amqp.md)

### redis
- [apache-airflow-providers-redis; extra=='redis'](packages/a/apache-airflow-providers-redis.md)
- [redis (~=3.2); extra=='redis'](packages/r/redis.md)

### salesforce
- [apache-airflow-providers-salesforce; extra=='salesforce'](packages/a/apache-airflow-providers-salesforce.md)
- [simple-salesforce (>=1.0.0); extra=='salesforce'](packages/s/simple-salesforce.md)

### samba
- [apache-airflow-providers-samba; extra=='samba'](packages/a/apache-airflow-providers-samba.md)
- [pysmbclient (>=0.1.3); extra=='samba'](packages/p/pysmbclient.md)

### segment
- [analytics-python (>=1.2.9); extra=='segment'](packages/a/analytics-python.md)
- [apache-airflow-providers-segment; extra=='segment'](packages/a/apache-airflow-providers-segment.md)

### sendgrid
- [apache-airflow-providers-sendgrid; extra=='sendgrid'](packages/a/apache-airflow-providers-sendgrid.md)
- [sendgrid (<7,>=6.0.0); extra=='sendgrid'](packages/s/sendgrid.md)

### sentry
- [blinker (>=1.1); extra=='sentry'](packages/b/blinker.md)
- [sentry-sdk (>=0.8.0); extra=='sentry'](packages/s/sentry-sdk.md)

### singularity
- [apache-airflow-providers-singularity; extra=='singularity'](packages/a/apache-airflow-providers-singularity.md)
- [spython (>=0.0.56); extra=='singularity'](packages/s/spython.md)

### slack
- [apache-airflow-providers-slack; extra=='slack'](packages/a/apache-airflow-providers-slack.md)
- [slackclient (<3.0.0,>=2.0.0); extra=='slack'](packages/s/slackclient.md)

### snowflake
- [apache-airflow-providers-snowflake; extra=='snowflake'](packages/a/apache-airflow-providers-snowflake.md)
- [requests (<2.24.0); extra=='snowflake'](packages/r/requests.md)
- [snowflake-connector-python (>=1.5.2); extra=='snowflake'](packages/s/snowflake-connector-python.md)
- [snowflake-sqlalchemy (>=1.1.0); extra=='snowflake'](packages/s/snowflake-sqlalchemy.md)

### spark
- [apache-airflow-providers-apache-spark; extra=='spark'](packages/a/apache-airflow-providers-apache-spark.md)
- [pyspark; extra=='spark'](packages/p/pyspark.md)

### ssh
- [apache-airflow-providers-ssh; extra=='ssh'](packages/a/apache-airflow-providers-ssh.md)
- [paramiko (>=2.6.0); extra=='ssh'](packages/p/paramiko.md)
- [pysftp (>=0.2.9); extra=='ssh'](packages/p/pysftp.md)
- [sshtunnel (<0.2,>=0.1.4); extra=='ssh'](packages/s/sshtunnel.md)

### statsd
- [statsd (<4.0,>=3.3.0); extra=='statsd'](packages/s/statsd.md)

### tableau
- [tableauserverclient (~=0.12); extra=='tableau'](packages/t/tableauserverclient.md)

### vertica
- [apache-airflow-providers-vertica; extra=='vertica'](packages/a/apache-airflow-providers-vertica.md)
- [vertica-python (>=0.5.1); extra=='vertica'](packages/v/vertica-python.md)

### virtualenv
- [virtualenv; extra=='virtualenv'](packages/v/virtualenv.md)

### webhdfs
- [apache-airflow-providers-apache-hdfs; extra=='webhdfs'](packages/a/apache-airflow-providers-apache-hdfs.md)
- [hdfs[avro,dataframe,kerberos] (>=2.0.4); extra=='webhdfs'](packages/h/hdfs.md)

### winrm
- [apache-airflow-providers-microsoft-winrm; extra=='winrm'](packages/a/apache-airflow-providers-microsoft-winrm.md)
- [pywinrm (~=0.4); extra=='winrm'](packages/p/pywinrm.md)

### yandex
- [apache-airflow-providers-yandex; extra=='yandex'](packages/a/apache-airflow-providers-yandex.md)
- [yandexcloud (>=0.22.0); extra=='yandex'](packages/y/yandexcloud.md)

### yandexcloud
- [apache-airflow-providers-yandex; extra=='yandexcloud'](packages/a/apache-airflow-providers-yandex.md)
- [yandexcloud (>=0.22.0); extra=='yandexcloud'](packages/y/yandexcloud.md)


## Publishers
- [aoen](https://pypi.org/user/aoen)
- [artwr](https://pypi.org/user/artwr)
- [ashb](https://pypi.org/user/ashb)
- [bolke](https://pypi.org/user/bolke)
- [criccomini](https://pypi.org/user/criccomini)
- [Fokko](https://pypi.org/user/Fokko)
- [kaxil](https://pypi.org/user/kaxil)
- [mistercrunch](https://pypi.org/user/mistercrunch)
- [msumit](https://pypi.org/user/msumit)
- [potiuk](https://pypi.org/user/potiuk)
- [r39132](https://pypi.org/user/r39132)


## Yanked Versions
- [1.10.11](https://pypi.org/project/apache-airflow/1.10.11)
- [1.10.13](https://pypi.org/project/apache-airflow/1.10.13)
 