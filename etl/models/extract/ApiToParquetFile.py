# Imports de Bibliotecas Padrão
import os
import time
import concurrent.futures

# Imports de Bibliotecas de Terceiros
import requests
import pandas as pd
from tqdm import tqdm

# Imports de Módulos Internos
from etl.common.utils.logs import loggingInfo, loggingWarn
from etl.common.utils.common import (
    DefaultTimestampStr,
    DefaultOutputFolder,
    DefaultUTCDatetime,
)
from etl.config.logFile import logFileName
from etl.config.datasource import API
from . import ParamsValidator as Validation

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

        ValidatedParameters = Validation.ParamsValidator(params)
        self.extractedFiles = self.PipelineRun(ValidatedParameters.validParams)

    def PipelineRun(self, ValidParams: list) -> list:
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
                break
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

        output_path = DefaultOutputFolder()
        insert_timestamp = DefaultTimestampStr()
        extracted_files = []
        totalParams = len(ValidParams)

        def process_param(args):

            index, param = args
            dic = json_data[param.replace("-", "")]

            # Convert 'dic' to a Pandas DataFrame
            df = pd.DataFrame([dic])

            # Add new columns to the DataFrame
            df["symbol"] = param

            # Add two columns with the current date and time
            df["extracted_at"] = DefaultUTCDatetime()

            # Write the DataFrame to a Parquet file
            df.to_parquet(f"{output_path}{param}-{insert_timestamp}.parquet")

            # Append list with the file path
            extracted_files.append(f"{output_path}{param}-{insert_timestamp}.parquet")

        ## Parallel Processing data
        with concurrent.futures.ThreadPoolExecutor(os.cpu_count()) as executor:
            list(
                tqdm(
                    executor.map(process_param, enumerate(ValidParams)),
                    total=totalParams,
                    desc="Processing files",
                )
            )

        loggingInfo(f"{totalParams} files extracted in: {output_path}", WORK_DIR)

        return extracted_files

    def GetGeneratedFiles(self) -> list:
        """
        Returns the generated files.

        Returns:
            list: A list of generated file paths.
        """
        return self.extractedFiles
