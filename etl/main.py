import time
import sys
import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

SRV_URL = str(os.getenv("SERVER_URL"))

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(WORK_DIR))

start_time = time.time()

from etl import ExecutePipeline

def GenerateRandomParams(ParamsQty: int) -> list: 
    """
    Generate a list of random parameters from the available list of parities.
    
    Args:
        ParamsQty (int): The number of random parameters to generate.
        
    Returns:
        list: A list of randomly generated parameters.
    """
    AvaliableList = list(requests.get(SRV_URL + '/json/available').json())
    min = random.randint(0, len(AvaliableList) - ParamsQty)
    max = min + ParamsQty
    return AvaliableList[min:max]

if __name__ == "__main__":
    NewExec = ExecutePipeline(*GenerateRandomParams(2))
    
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
