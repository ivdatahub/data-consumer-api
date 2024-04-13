from etl.jobs.extract.ApiToParquetFile import extraction
# from etl.jobs.load.ParquetToDataBase import pgLoading

class ExecutePipeline:
    def __init__(self, *xargs) -> None:
        extraction(xargs)
        # pgLoading()
        