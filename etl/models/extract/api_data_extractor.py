from typing import Tuple

from api_to_dataframe import ClientBuilder, RetryStrategies
from etl.common.utils.logs import CustomLogger
from etl.config.logFile import log_file_name
from etl.config.datasource import API
from etl.models.extract.params_validator import ParamsValidator

logger = CustomLogger(log_file_name(file=__file__))


class APIExtraction:
    @staticmethod
    def run(params) -> Tuple[dict, list]:
        valid_params = ParamsValidator.valid_params_for_call(params)

        url_endpoint = API.ENDPOINT_LAST_COTATION + ",".join(valid_params)
        logger.info(f"Sending request to: {API.ENDPOINT_LAST_COTATION}")

        client = ClientBuilder(
            endpoint=url_endpoint,
            retry_strategy=RetryStrategies.LINEAR_RETRY_STRATEGY,
            connection_timeout=API.CONNECTION_TIMEOUT,
            initial_delay=API.RETRY_TIME_SECONDS,
            retries=API.RETRY_ATTEMPTS
        )

        response = client.get_api_data()

        return response, valid_params
