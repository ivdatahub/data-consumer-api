import time
import sys
import os
import requests
import random

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(WORK_DIR))

start_time = time.time()

from etl import ExecutePipeline
from etl.utils.constants import ENDPOINT_LIST_AVALIABLE_PARITYS

def GenerateRandomParams(ParamsQty: int) -> list: 
    AvaliableList = list(requests.get(ENDPOINT_LIST_AVALIABLE_PARITYS).json())
    min = random.randint(0, len(AvaliableList) - ParamsQty)
    max = min + ParamsQty
    return AvaliableList[min:max]

if __name__ == "__main__":
    NewExec = ExecutePipeline(*GenerateRandomParams(10))
    
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")