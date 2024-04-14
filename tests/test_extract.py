import os
import sys 

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(WORK_DIR))

from etl.utils.logs import loggingInfo
from etl.jobs.extract.ApiToParquetFile import extraction

def test_extraction():
    params = extraction("USD-BRL").params
    
    if not isinstance(params, str): raise