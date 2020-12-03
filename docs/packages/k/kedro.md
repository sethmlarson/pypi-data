# [kedro](https://pypi.org/project/kedro)

## Dependencies
- [anyconfig (~=0.9.7)](packages/a/anyconfig.md)
- [cachetools (~=4.1)](packages/c/cachetools.md)
- [click (<8.0)](packages/c/click.md)
- [cookiecutter (<1.7.0,>=1.6.0)](packages/c/cookiecutter.md)
- [fsspec (<0.7.0,>=0.5.1)](packages/f/fsspec.md)
- [jmespath (<1.0,>=0.9.5)](packages/j/jmespath.md)
- [jupyter-client (<7.0,>=5.1)](packages/j/jupyter-client.md)
- [pip-tools (~=5.0)](packages/p/pip-tools.md)
- [pluggy (~=0.13.0)](packages/p/pluggy.md)
- [python-json-logger (~=0.1.9)](packages/p/python-json-logger.md)
- [pyyaml (<6.0,>=4.2)](packages/p/pyyaml.md)
- [setuptools (>=38.0)](packages/s/setuptools.md)
- [toposort (~=1.5)](packages/t/toposort.md)


## Extras

### api
- [requests (~=2.20); extra=='api'](packages/r/requests.md)

### api.apidataset
- [requests (~=2.20); extra=='api.apidataset'](packages/r/requests.md)

### biosequence
- [biopython (~=1.73); extra=='biosequence'](packages/b/biopython.md)

### biosequence.biosequencedataset
- [biopython (~=1.73); extra=='biosequence.biosequencedataset'](packages/b/biopython.md)

### dask
- [dask[complete] (~=2.6); extra=='dask'](packages/d/dask.md)

### dask.parquetdataset
- [dask[complete] (~=2.6); extra=='dask.parquetdataset'](packages/d/dask.md)

### geopandas
- [geopandas (<1.0,>=0.6.0); extra=='geopandas'](packages/g/geopandas.md)

### geopandas.geojsondataset
- [geopandas (<1.0,>=0.6.0); extra=='geopandas.geojsondataset'](packages/g/geopandas.md)

### holoviews
- [holoviews (~=1.13.0); extra=='holoviews'](packages/h/holoviews.md)

### holoviews.holoviewswriter
- [holoviews (~=1.13.0); extra=='holoviews.holoviewswriter'](packages/h/holoviews.md)

### matplotlib
- [matplotlib (<4.0,>=3.0.3); extra=='matplotlib'](packages/m/matplotlib.md)

### matplotlib.matplotlibwriter
- [matplotlib (<4.0,>=3.0.3); extra=='matplotlib.matplotlibwriter'](packages/m/matplotlib.md)

### networkx
- [networkx (~=2.4); extra=='networkx'](packages/n/networkx.md)

### networkx.networkxdataset
- [networkx (~=2.4); extra=='networkx.networkxdataset'](packages/n/networkx.md)

### notebook_templates
- [nbconvert (<6.0,>=5.3.1); extra=='notebook_templates'](packages/n/nbconvert.md)
- [nbformat (~=4.4); extra=='notebook_templates'](packages/n/nbformat.md)

### pandas
- [openpyxl (<4.0,>=3.0.3); extra=='pandas'](packages/o/openpyxl.md)
- [pandas (>=0.24); extra=='pandas'](packages/p/pandas.md)
- [pandas-gbq (<1.0,>=0.12.0); extra=='pandas'](packages/p/pandas-gbq.md)
- [pyarrow (<1.0.0,>=0.12.0); extra=='pandas'](packages/p/pyarrow.md)
- [sqlalchemy (~=1.2); extra=='pandas'](packages/s/sqlalchemy.md)
- [tables (~=3.6); extra=='pandas'](packages/t/tables.md)
- [xlrd (~=1.0); extra=='pandas'](packages/x/xlrd.md)
- [xlsxwriter (~=1.0); extra=='pandas'](packages/x/xlsxwriter.md)

### pandas.appendableexceldataset
- [openpyxl (<4.0,>=3.0.3); extra=='pandas.appendableexceldataset'](packages/o/openpyxl.md)
- [pandas (>=0.24); extra=='pandas.appendableexceldataset'](packages/p/pandas.md)

### pandas.csvdataset
- [pandas (>=0.24); extra=='pandas.csvdataset'](packages/p/pandas.md)

### pandas.exceldataset
- [pandas (>=0.24); extra=='pandas.exceldataset'](packages/p/pandas.md)
- [xlrd (~=1.0); extra=='pandas.exceldataset'](packages/x/xlrd.md)
- [xlsxwriter (~=1.0); extra=='pandas.exceldataset'](packages/x/xlsxwriter.md)

### pandas.featherdataset
- [pandas (>=0.24); extra=='pandas.featherdataset'](packages/p/pandas.md)

### pandas.gbqtabledataset
- [pandas (>=0.24); extra=='pandas.gbqtabledataset'](packages/p/pandas.md)
- [pandas-gbq (<1.0,>=0.12.0); extra=='pandas.gbqtabledataset'](packages/p/pandas-gbq.md)

### pandas.hdfdataset
- [pandas (>=0.24); extra=='pandas.hdfdataset'](packages/p/pandas.md)
- [tables (~=3.6); extra=='pandas.hdfdataset'](packages/t/tables.md)

### pandas.jsondataset
- [pandas (>=0.24); extra=='pandas.jsondataset'](packages/p/pandas.md)

### pandas.parquetdataset
- [pandas (>=0.24); extra=='pandas.parquetdataset'](packages/p/pandas.md)
- [pyarrow (<1.0.0,>=0.12.0); extra=='pandas.parquetdataset'](packages/p/pyarrow.md)

### pandas.sqltabledataset
- [pandas (>=0.24); extra=='pandas.sqltabledataset'](packages/p/pandas.md)
- [sqlalchemy (~=1.2); extra=='pandas.sqltabledataset'](packages/s/sqlalchemy.md)

### pillow
- [pillow (~=7.1.2); extra=='pillow'](packages/p/pillow.md)

### pillow.imagedataset
- [pillow (~=7.1.2); extra=='pillow.imagedataset'](packages/p/pillow.md)

### profilers
- [memory-profiler (<1.0,>=0.50.0); extra=='profilers'](packages/m/memory-profiler.md)

### spark
- [hdfs (<3.0,>=2.5.8); extra=='spark'](packages/h/hdfs.md)
- [pyspark (~=2.2); extra=='spark'](packages/p/pyspark.md)
- [s3fs (<0.4.1,>=0.3.0); extra=='spark'](packages/s/s3fs.md)

### spark.sparkdataset
- [hdfs (<3.0,>=2.5.8); extra=='spark.sparkdataset'](packages/h/hdfs.md)
- [pyspark (~=2.2); extra=='spark.sparkdataset'](packages/p/pyspark.md)
- [s3fs (<0.4.1,>=0.3.0); extra=='spark.sparkdataset'](packages/s/s3fs.md)

### spark.sparkhivedataset
- [hdfs (<3.0,>=2.5.8); extra=='spark.sparkhivedataset'](packages/h/hdfs.md)
- [pyspark (~=2.2); extra=='spark.sparkhivedataset'](packages/p/pyspark.md)
- [s3fs (<0.4.1,>=0.3.0); extra=='spark.sparkhivedataset'](packages/s/s3fs.md)

### spark.sparkjdbcdataset
- [hdfs (<3.0,>=2.5.8); extra=='spark.sparkjdbcdataset'](packages/h/hdfs.md)
- [pyspark (~=2.2); extra=='spark.sparkjdbcdataset'](packages/p/pyspark.md)
- [s3fs (<0.4.1,>=0.3.0); extra=='spark.sparkjdbcdataset'](packages/s/s3fs.md)

### tensorflow
- [tensorflow (~=2.0); extra=='tensorflow'](packages/t/tensorflow.md)

### tensorflow.tensorflowmodeldataset
- [tensorflow (~=2.0); extra=='tensorflow.tensorflowmodeldataset'](packages/t/tensorflow.md)

### yaml
- [pandas (>=0.24); extra=='yaml'](packages/p/pandas.md)
- [pyyaml (<6.0,>=4.2); extra=='yaml'](packages/p/pyyaml.md)

### yaml.yamldataset
- [pandas (>=0.24); extra=='yaml.yamldataset'](packages/p/pandas.md)
- [pyyaml (<6.0,>=4.2); extra=='yaml.yamldataset'](packages/p/pyyaml.md)


## Publishers
- [quantumblacklabs](https://pypi.org/user/quantumblacklabs)

