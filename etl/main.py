from etl.controller.pipeline import PipelineExecutor
import time

start = time.time()
import random
import requests

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
    if max > len(AvaliableList):
        max = len(AvaliableList)
    if ParamsQty == len(AvaliableList):
        max -= max
    return AvaliableList[min : max - 1]


if __name__ == "__main__":
    NewExec = PipelineExecutor(*GenerateRandomParams(10))
    NewExec.pipeline_run()

print("Tempo decorrido: ", round(time.time() - start, 2), "segundos")
