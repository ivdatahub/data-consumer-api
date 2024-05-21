from etl.models.extract.ApiToParquetFile import extraction


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
        self.extractedFiles = []

        totalInvalidParams = 0
        for arg in self.params:
            if not isinstance(arg, str):
                totalInvalidParams += 1

        if totalInvalidParams == self.params_count:
            raise TypeError(f"Invalid parameters >>>> {self.params}")

        self.pipelineExecute(InputParams=self.params)

    def pipelineExecute(self, InputParams: list):
        """
        Executes the pipeline.

        Raises:
            KeyError: If the informed parameters are not available for extraction.

        """
        NewExt = extraction(InputParams)
        self.extractedFiles = NewExt.GetGeneratedFiles()

    def GetExtractedFiles(self) -> list:
        """
        Returns the list of extracted files.

        Returns:
            list: List of extracted files.

        """
        return self.extractedFiles
