
import pandas as pd

from etl.config.logFile import log_file_name
from etl.common.utils.logs import CustomLogger
from etl.common.utils.common import (
    DefaultTimestampStr,
    DefaultOutputFolder,
    DefaultUTCDatetime,
)

logger = CustomLogger(log_file_name(file=__file__))

class load:
    def __init__(self, item) -> None:
        self.dic = item

    def run(self):
        extracted_files = []
        param = self.dic["code"] + "-" + self.dic["codein"]
        ts = DefaultTimestampStr()
        df = pd.DataFrame([self.dic])

        if df.empty:
            logger.error("DataFrame is empty")
            raise ValueError("DataFrame is empty")

        # Add new columns to the DataFrame
        df["symbol"] = param

        # Add two columns with the current date and time
        df["extracted_at"] = DefaultUTCDatetime()

        df["id"] = f"{param}-{ts}"

        # Write the DataFrame to a Parquet file
        try:
            df.to_parquet(f"{DefaultOutputFolder()}{param}-{ts}.parquet")
        except Exception as e:
            logger.error(f"Error writing parquet file: {e}")

        # Append list with the file path
        extracted_files.append(f"{param}-{ts}.parquet")

        return extracted_files
