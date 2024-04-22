import requests
from etl.utils.constants import ENDPOINT_LIST_AVALIABLE_PARITYS
from etl.utils.logs import loggingWarn
from etl.jobs.ExtractApiData.ApiToParquetFile import extraction

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

        self.ValidParams = self.ValidParamsForCall()
        self.pipelineExecute()

    def ValidParamsForCall(self) -> list:
        """
        Returns a list of valid parameters for the pipeline execution.

        Returns:
            list: List of valid parameters.

        """
        valParams = []
        AvaliableList = requests.get(ENDPOINT_LIST_AVALIABLE_PARITYS).json()

        for param in self.params:
            if param in AvaliableList:
                valParams.append(param)
            else:
                loggingWarn(f"Param: {param} is not valid for call", mdName)

        return valParams

    def pipelineExecute(self):
        """
        Executes the pipeline.

        Raises:
            KeyError: If the informed parameters are not available for extraction.

        """
        if self.ValidParams:
            NewExt = extraction(self.ValidParams)
            self.extractedFiles = NewExt.GetExtractedFilesList()
        else:
            raise KeyError(
                f"The informed params: {self.params} are not available for extract, see available list in: {ENDPOINT_LIST_AVALIABLE_PARITYS}"
            )

    def GetExtractedFiles(self) -> list:
        """
        Returns the list of extracted files.

        Returns:
            list: List of extracted files.

        """
        return self.extractedFiles