import requests
from etl.common.utils.logs import logging_warn
from etl.config.datasource import API
from etl.config.logFile import log_file_name

WORK_DIR = log_file_name(file=__file__)


class ParamsValidator:
    def __init__(self, params: list) -> None:
        self.params = params

    def valid_params_for_call(self) -> list:
        """
        Returns a list of valid parameters for the pipeline execution.

        Returns:
            list: List of valid parameters.

        """
        valParams = []
        AvaliableList = requests.get(API.ENDPOINT_AVALIABLE_PARITIES).json()

        for param in self.params:
            if param in AvaliableList:
                valParams.append(param)
            else:
                logging_warn(f"Param: {param} is not valid for call", WORK_DIR)

        if valParams:
            return valParams
        else:
            raise KeyError(
                f"The informed params: {self.params} are not avaliable for extract, see available list in: {API.ENDPOINT_AVALIABLE_PARITIES}"
            )
