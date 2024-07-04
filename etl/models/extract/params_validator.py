from api_to_dataframe import ClientBuilder, RetryStrategies
from etl.common.utils.logs import CustomLogger
from etl.config.datasource import API
from etl.config.logFile import log_file_name

logger = CustomLogger(log_file_name(file=__file__))


class ParamsValidator:
    @staticmethod
    def valid_params_for_call(params) -> list:
        """
        Returns a list of valid parameters for the pipeline execution.

        Returns:
            list: List of valid parameters.

        """
        valid_params = []

        client = ClientBuilder(
            endpoint=API.ENDPOINT_AVALIABLE_PARITIES,
            retry_strategy=RetryStrategies.LINEAR_RETRY_STRATEGY,
            connection_timeout=API.CONNECTION_TIMEOUT,
            initial_delay=API.RETRY_TIME_SECONDS,
            retries=API.RETRY_ATTEMPTS,
        )

        avaliable_list = client.get_api_data()

        for param in params:
            if param in avaliable_list:
                valid_params.append(param)
            else:
                logger.warning(f"Param: {param} is not valid for call")

        if valid_params:
            return valid_params
        else:
            raise KeyError(
                f"The informed params: {params} are not avaliable for extract, see available list in: {API.ENDPOINT_AVALIABLE_PARITIES}"
            )
