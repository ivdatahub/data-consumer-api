from etl.config.datasource import API
import requests
import random
from etl.controller.pipeline import PipelineExecutor
import time
import sys

start = time.time()


def generate_random_params(params_qty: int) -> list:
    """
    Generate a list of random parameters from the available list of parities.

    Args:
        params_qty (int): The number of random parameters to generate.

    Returns:
        list: A list of randomly generated parameters.
    """
    avaliable_list = list(requests.get(API.ENDPOINT_AVALIABLE_PARITIES).json())
    min = random.randint(0, len(avaliable_list) - params_qty)
    max = min + params_qty
    if max > len(avaliable_list):
        max = len(avaliable_list)
    if params_qty == len(avaliable_list):
        max -= max
    return avaliable_list[min : max - 1]


def main(total_files: int = 2):
    NewExec = PipelineExecutor(*generate_random_params(total_files))
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
