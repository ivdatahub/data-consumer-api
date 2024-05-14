import sys
import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

SRV_URL = str(os.getenv("SERVER_URL"))

if not SRV_URL:
    raise Exception("SERVER_URL is not defined in the .env file.")

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(WORK_DIR))

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
    NewExec = ExecutePipeline(*GenerateRandomParams(300))
    
