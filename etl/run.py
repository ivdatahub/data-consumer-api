import time

import sys
import random

import requests

from etl.controller.pipeline import PipelineExecutor
from etl.config.datasource import API

start = time.time()


def generate_random_params(params_qty: int) -> list:
    """
    Generate a list of random parameters from the available list of parities.

    Args:
        params_qty (int): The number of random parameters to generate.

    Returns:
        list: A list of randomly generated parameters.
    """
    available_list = list(requests.get(API.ENDPOINT_AVALIABLE_PARITIES).json())
    first_number = random.randint(0, len(available_list) - params_qty)
    last_number = first_number + params_qty
    if last_number > len(available_list):
        last_number = len(available_list)
    if params_qty == len(available_list):
        last_number -= last_number
    return available_list[first_number:last_number - 1]


def main(total_files: int = 2):
    new_exec = PipelineExecutor(*generate_random_params(total_files))
    new_exec.pipeline_run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        params_count = int(sys.argv[1])
    else:
        params_count = random.randint(3, 20)

    main(params_count)

print("Elapsed Time: ", round(time.time() - start, 2), "seconds")
