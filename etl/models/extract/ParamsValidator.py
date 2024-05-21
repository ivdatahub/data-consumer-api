import requests
from etl.common.utils.logs import loggingWarn
from etl.config.datasource import API
from etl.config.logFile import logFileName

WORK_DIR = logFileName(file=__file__)


class ParamsValidator:
    def __init__(self, params: list) -> None:
        self.params = params
        self.validParams = self.__ValidParamsForCall__()

    def __ValidParamsForCall__(self) -> list:
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
                loggingWarn(f"Param: {param} is not valid for call", WORK_DIR)

        if valParams:
            return valParams
        else:
            raise KeyError(
                f"The informed params: {self.params} are not avaliable for extract, see available list in: {API.ENDPOINT_AVALIABLE_PARITIES}"
            )
