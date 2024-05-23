from etl.config.datasource import API
import requests
import random
from etl.controller.pipeline import PipelineExecutor
import time
import sys

start = time.time()


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
    return AvaliableList[min: max - 1]


def main(total_files: int = 2):
    NewExec = PipelineExecutor(*GenerateRandomParams(total_files))
    NewExec.pipeline_run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Pega o número de parâmetros da linha de comando
        params_count = int(sys.argv[1])
    else:
        # Gera um número aleatório de parâmetros
        params_count = random.randint(3, 20)

    main(params_count)

print("Tempo decorrido: ", round(time.time() - start, 2), "segundos")
