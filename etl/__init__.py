from etl.jobs.extract.ApiToParquetFile import extraction
# next steps
    # from etl.jobs.transform import transformation
    # from etl.jobs.extract.load import loadData

class ExecutePipeline:
    def __init__(self, *xargs) -> None:
        extraction(xargs)
        
        # next steps
            # transformation()
            # loadData()
            