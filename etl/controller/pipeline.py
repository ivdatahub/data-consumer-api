from etl.models.extract.ApiToParquetFile import extraction
from etl.models.transform.ResponseSplit import transformation


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
        TypeError: If all type of parameters passed to the pipeline execution are invalid.

    Methods:
        pipelineExecute: Executes the pipeline.
        GetExtractedFiles: Returns the list of extracted files.

    """

    def __init__(self, *xargs) -> None:
        self.params = list(xargs)
        self.params_count = len(self.params)

        totalInvalidParams = 0
        for arg in self.params:
            if not isinstance(arg, str):
                totalInvalidParams += 1

        if totalInvalidParams == self.params_count:
            raise TypeError(f"Invalid parameters >>>> {self.params}")

        self.__pipelineExecute__(InputParams=self.params)

    def __pipelineExecute__(self, InputParams: list):
        """
        Executes the pipeline.

        Raises:
            KeyError: If the informed parameters are not available for extraction.

        """
        NewExt = extraction(InputParams)
        NewTransform = transformation(NewExt.json_data, NewExt.ValidParams)