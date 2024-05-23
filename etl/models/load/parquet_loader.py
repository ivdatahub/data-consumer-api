from math import e
from tqdm import tqdm
import pandas as pd

from etl.config.logFile import logFileName
from etl.common.utils.logs import loggingError, loggingInfo
from etl.common.utils.common import (
    DefaultTimestampStr,
    DefaultOutputFolder,
    DefaultUTCDatetime,
)

WORK_DIR = logFileName(file=__file__)


class load:
    def __init__(self, item) -> None:
        self.dic = item

    def run(self):
        extracted_files = []
        param = self.dic["code"] + "-" + self.dic["codein"]
        ts = DefaultTimestampStr()
        df = pd.DataFrame([self.dic])

        if df.empty:
            loggingError("DataFrame is empty", WORK_DIR)
            raise ValueError("DataFrame is empty")

        # Add new columns to the DataFrame
        df["symbol"] = param

        # Add two columns with the current date and time
        df["extracted_at"] = DefaultUTCDatetime()

        # Write the DataFrame to a Parquet file
        try:
            df.to_parquet(f"{DefaultOutputFolder()}{param}-{ts}.parquet")
        except Exception as e:
            loggingError(f"Error writing parquet file: {e}", WORK_DIR)

        # Append list with the file path
        extracted_files.append(f"{param}-{ts}.parquet")

        return extracted_files
