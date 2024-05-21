import requests
import os
from dotenv import load_dotenv
from etl.common.utils.logs import loggingWarn

mdName = "extract"

load_dotenv()

SRV_URL = str(os.getenv("SERVER_URL"))
""" Reference for Server URL from enviroment variable """


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
        AvaliableList = requests.get(SRV_URL + "/json/available").json()

        for param in self.params:
            if param in AvaliableList:
                valParams.append(param)
            else:
                loggingWarn(f"Param: {param} is not valid for call", mdName)

        if valParams:
            return valParams
        else:
            raise KeyError(
                f"The informed params: {self.params} are not avaliable for extract, see available list in: {SRV_URL + '/json/available'}"
            )
