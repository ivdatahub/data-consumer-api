import requests
from etl.common.utils.logs import loggingWarn
from etl.models.extract.ApiToParquetFile import extraction
from dotenv import load_dotenv
import os

load_dotenv()

SRV_URL = str(os.getenv("SERVER_URL"))
""" Reference for Server URL from enviroment variable """

mdName = "extract_prepare"

class ExecutePipeline:
    """
    Class representing a pipeline execution.

    Args:
        *xargs: Variable number of string arguments representing the parameters for the pipeline execution.

    Attributes:
        params (list): List of parameters passed to the pipeline execution.
        params_count (int): Number of parameters passed to the pipeline execution.
        extractedFiles (list): List of extracted files from the pipeline execution.

    Raises:
        TypeError: If all the parameters passed to the pipeline execution are invalid.

    Methods:
        ValidParamsForCall: Returns a list of valid parameters for the pipeline execution.
        pipelineExecute: Executes the pipeline.
        GetExtractedFiles: Returns the list of extracted files.

    """

    def __init__(self, *xargs) -> None:
        self.params = list(xargs)
        self.params_count = len(self.params)
        self.extractedFiles = []

        totalInvalidParams = 0
        for arg in self.params:
            if not isinstance(arg, str):
                totalInvalidParams += 1

        if totalInvalidParams == self.params_count:
            raise TypeError(f"Invalid parameters >>>> {self.params}")

        ValidParams = self.ValidParamsForCall()
        self.pipelineExecute(ValidParameters=ValidParams)

    def ValidParamsForCall(self) -> list:
        """
        Returns a list of valid parameters for the pipeline execution.

        Returns:
            list: List of valid parameters.

        """
        valParams = []
        AvaliableList = requests.get(SRV_URL + '/json/available').json()

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

    def pipelineExecute(self, ValidParameters: list):
        """
        Executes the pipeline.

        Raises:
            KeyError: If the informed parameters are not available for extraction.

        """
        NewExt = extraction(ValidParameters)
        self.extractedFiles = NewExt.GetGeneratedFiles()

    def GetExtractedFiles(self) -> list:
        """
        Returns the list of extracted files.

        Returns:
            list: List of extracted files.

        """
        return self.extractedFiles
    