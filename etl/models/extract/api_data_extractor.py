import time
from typing import Tuple


import requests
from tqdm import tqdm

from etl.common.utils.logs import CustomLogger
from etl.config.logFile import log_file_name
from etl.config.datasource import API
from etl.models.extract import params_validator

logger = CustomLogger(log_file_name(file=__file__))

class extraction:
    def __init__(self, params: list) -> None:
        self.params = params

    @property
    def run(self) -> Tuple[dict, list]:
        validator = params_validator.ParamsValidator(self.params)
        valid_params = validator.valid_params_for_call()

        url_endpoint = API.ENDPOINT_LAST_COTATION + ",".join(valid_params)
        logger.info(
            f"Sending request to: {API.ENDPOINT_LAST_COTATION} :: 1 of {API.RETRY_ATTEMPTS}",
        )
        response = requests.get(url_endpoint)

        for try_number in range(API.RETRY_ATTEMPTS):
            if response.ok:
                logger.info(
                    f"Request finished with status {response.status_code}")
                json_data = response.json()
                return json_data, valid_params
            else:
                if try_number < API.RETRY_ATTEMPTS - 1:
                    logger.warning(
                        f"""response error, status_code {response.status_code}. 
                        Retrying in {API.RETRY_TIME_SECONDS} seconds..."""
                    )
                    for _ in tqdm(range(100), total=100, desc=f"loading"):
                        time.sleep(API.RETRY_TIME_SECONDS / 100)
                    logger.info(
                        f"Sending request to: {API.ENDPOINT_LAST_COTATION} :: {try_number + 2} of {API.RETRY_ATTEMPTS}",
                    )
                else:
                    logger.warning("Attempt limits exceeded")
                    raise ConnectionError(
                        f"""Could not connect to the server after 3 attempts. 
                        Please try again later. 
                        Response status code: {response.status_code}"""
                    )

        return {}, []
