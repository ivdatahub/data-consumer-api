# Imports de Bibliotecas Padrão
import time

# Imports de Bibliotecas de Terceiros
import requests
from tqdm import tqdm

# Imports de Módulos Internos
from etl.common.utils.logs import loggingInfo, loggingWarn
from etl.config.logFile import logFileName
from etl.config.datasource import API
from . import params_validator as Validation

WORK_DIR = logFileName(file=__file__)


class extraction:
    def __init__(self, params: list) -> None:
        """
        Initializes the extraction class.

        Args:
            ValidParams (list): A list of valid parameters.

        Returns:
            None
        """
        self.params = params
        __validator__ = Validation.ParamsValidator(params)
        self.ValidParams = __validator__.ValidParamsForCall()
        self.json_data = self.__run__(self.ValidParams)

    def __run__(self, ValidParams: list) -> dict:
        """
        Runs the data extraction pipeline.

        Returns:
            list: A list of extracted file paths.
        """
        ## extract Data
        maked_endpoint = API.ENDPOINT_LAST_COTATION + ",".join(ValidParams)
        loggingInfo(
            f"Sending request to: {API.ENDPOINT_LAST_COTATION} :: 1 of {API.RETRY_ATTEMPTS}",
            WORK_DIR,
        )
        response = requests.get(maked_endpoint)

        for tryNumber in range(API.RETRY_ATTEMPTS):
            if response.ok:
                loggingInfo(
                    f"Request finished with status {response.status_code}", WORK_DIR
                )
                json_data = response.json()
                return json_data
            else:
                if tryNumber < API.RETRY_ATTEMPTS - 1:
                    loggingWarn(
                        f"""response error, status_code {response.status_code}. 
                        Retrying in {API.RETRY_TIME_SECONDS} seconds...""",
                        WORK_DIR,
                    )
                    for _ in tqdm(range(100), total=100, desc=f"loading"):
                        time.sleep(API.RETRY_TIME_SECONDS / 100)
                    loggingInfo(
                        f"Sending request to: {API.ENDPOINT_LAST_COTATION} :: {tryNumber + 2} of {API.RETRY_ATTEMPTS}",
                        WORK_DIR,
                    )
                else:
                    loggingWarn("Attempt limits exceeded", WORK_DIR)
                    raise ConnectionError(
                        f"""Could not connect to the server after 3 attempts. 
                        Please try again later. 
                        Response status code: {response.status_code}"""
                    )
        return (
            {}
        )  # Add this line to return an empty dictionary if no other return statement is reached
