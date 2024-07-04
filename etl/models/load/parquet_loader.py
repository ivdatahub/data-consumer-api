import pandas as pd

from etl.config.log_file import log_file_name
from etl.common.utils.logs import CustomLogger
from etl.common.utils.common import (
    default_timestamp_str,
    default_output_folder,
    default_utc_datetime,
)

logger = CustomLogger(log_file_name(file=__file__))


class ParquetLoader:
    @staticmethod
    def run(dic):
        extracted_files = []
        param = dic["code"] + "-" + dic["codein"]
        ts = default_timestamp_str()
        df = pd.DataFrame([dic])

        if df.empty:
            logger.error("DataFrame is empty")
            raise ValueError("DataFrame is empty")

        # Add new columns to the DataFrame
        df["symbol"] = param

        # Add two columns with the current date and time
        df["extracted_at"] = default_utc_datetime()

        df["id"] = f"{param}-{ts}"

        # Write the DataFrame to a Parquet file
        try:
            df.to_parquet(f"{default_output_folder()}{param}-{ts}.parquet")
        except ValueError as e:
            logger.error(f"Error writing parquet file: {e}")

        # Append list with the file path
        extracted_files.append(f"{param}-{ts}.parquet")

        return extracted_files
