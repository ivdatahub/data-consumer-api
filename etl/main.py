import random

import requests

from etl.controller.pipeline import ExecutePipeline
from etl.config.datasource import API


def GenerateRandomParams(ParamsQty: int) -> list:
    """
    Generate a list of random parameters from the available list of parities.

    Args:
        ParamsQty (int): The number of random parameters to generate.

    Returns:
        list: A list of randomly generated parameters.
    """
    AvaliableList = list(requests.get(API.ENDPOINT_AVALIABLE_PARITIES).json())
    min = random.randint(0, len(AvaliableList) - ParamsQty)
    max = min + ParamsQty
    return AvaliableList[min:max]


if __name__ == "__main__":
    NewExec = ExecutePipeline(*GenerateRandomParams(1))
