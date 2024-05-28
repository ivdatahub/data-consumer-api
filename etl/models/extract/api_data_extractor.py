import time
from typing import Tuple


import requests
from tqdm import tqdm

from etl.common.utils.logs import logging_info, logging_warn
from etl.config.logFile import log_file_name
from etl.config.datasource import API
from etl.models.extract import params_validator

default_folder = log_file_name(file=__file__)


class extraction:
    def __init__(self, params: list) -> None:
        self.params = params

    @property
    def run(self) -> Tuple[dict, list]:
        validator = params_validator.ParamsValidator(self.params)
        valid_params = validator.valid_params_for_call()

        url_endpoint = API.ENDPOINT_LAST_COTATION + ",".join(valid_params)
        logging_info(
            f"Sending request to: {API.ENDPOINT_LAST_COTATION} :: 1 of {API.RETRY_ATTEMPTS}",
            default_folder,
        )
        response = requests.get(url_endpoint)

        for try_number in range(API.RETRY_ATTEMPTS):
            if response.ok:
                logging_info(
                    f"Request finished with status {response.status_code}", default_folder
                )
                json_data = response.json()
                return json_data, valid_params
            else:
                if try_number < API.RETRY_ATTEMPTS - 1:
                    logging_warn(
                        f"""response error, status_code {response.status_code}. 
                        Retrying in {API.RETRY_TIME_SECONDS} seconds...""",
                        default_folder,
                    )
                    for _ in tqdm(range(100), total=100, desc=f"loading"):
                        time.sleep(API.RETRY_TIME_SECONDS / 100)
                    logging_info(
                        f"Sending request to: {API.ENDPOINT_LAST_COTATION} :: {try_number + 2} of {API.RETRY_ATTEMPTS}",
                        default_folder,
                    )
                else:
                    logging_warn("Attempt limits exceeded", default_folder)
                    raise ConnectionError(
                        f"""Could not connect to the server after 3 attempts. 
                        Please try again later. 
                        Response status code: {response.status_code}"""
                    )

        return {}, []
