import os

import pandas as pd
import concurrent.futures
from tqdm import tqdm

from etl.common.utils.common import (
    DefaultTimestampStr,
    DefaultOutputFolder,
    DefaultUTCDatetime,
)
from etl.common.utils.logs import loggingInfo
from etl.config.logFile import logFileName

WORK_DIR = logFileName(file=__file__)


class transformation:
    def __init__(self, json_response: dict, params) -> None:
        self.output_path = DefaultOutputFolder()
        self.insert_timestamp = DefaultTimestampStr()
        self.extracted_files = []
        self.json_response = json_response
        self.totalParams = len(json_response)
        self.validParams = params

        ## Parallel Processing data
        with concurrent.futures.ThreadPoolExecutor(os.cpu_count()) as executor:
            list(
                tqdm(
                    executor.map(self.__process_param__, enumerate(self.validParams)),
                    total=self.totalParams,
                    desc="Processing files",
                )
            )

        loggingInfo(
            f"{self.totalParams} files extracted in: {self.output_path}", WORK_DIR
        )

    def __process_param__(self, args):

        index, param = args
        dic = self.json_response[param.replace("-", "")]

        # Convert 'dic' to a Pandas DataFrame
        df = pd.DataFrame([dic])

        # Add new columns to the DataFrame
        df["symbol"] = param

        # Add two columns with the current date and time
        df["extracted_at"] = DefaultUTCDatetime()

        # Write the DataFrame to a Parquet file
        df.to_parquet(f"{self.output_path}{param}-{self.insert_timestamp}.parquet")

        # Append list with the file path
        self.extracted_files.append(f"{param}-{self.insert_timestamp}.parquet")

        return None
