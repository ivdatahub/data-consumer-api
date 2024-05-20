import os
import random
import requests
from dotenv import load_dotenv
from etl.controller.pipeline import ExecutePipeline

load_dotenv()

SRV_URL = str(os.getenv("SERVER_URL"))

if SRV_URL == "None" or SRV_URL == "":
    raise Exception("SERVER_URL is not defined in the .env file.")

def GenerateRandomParams(ParamsQty: int) -> list:
    """
    Generate a list of random parameters from the available list of parities.

    Args:
        ParamsQty (int): The number of random parameters to generate.

    Returns:
        list: A list of randomly generated parameters.
    """
    AvaliableList = list(requests.get(SRV_URL + "/json/available").json())
    min = random.randint(0, len(AvaliableList) - ParamsQty)
    max = min + ParamsQty
    return AvaliableList[min:max]


if __name__ == "__main__":
    NewExec = ExecutePipeline(*GenerateRandomParams(2))
    