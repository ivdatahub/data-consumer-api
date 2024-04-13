import os
import sys 

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(WORK_DIR))

from etl.utils.logs import loggingInfo
from etl.jobs.extract.ApiToParquetFile import extraction

def test_extraction():
    params = extraction("test").params
    
    if isinstance(params, str):
        print("OK")
    else:
        raise