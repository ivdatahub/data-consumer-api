from etl.models.extract import (
    requests
    ,pandas as pd
    ,loggingInfo
    ,loggingWarn
    ,DefaultOutputFolder
    ,DefaultTimestampStr
    ,DefaultUTCDatetime
    ,SRV_URL
    ,WORK_DIR
)

import concurrent.futures
import time
from tqdm import tqdm
import os


counter = 0
retry_time = 2
class extraction: 
    def __init__(self, ValidParams: list) -> None:
        """
        Initializes the extraction class.

        Args:
            ValidParams (list): A list of valid parameters.

        Returns:
            None
        """
        self.extractedFiles = self.PipelineRun(ValidParams)
        

    def PipelineRun(self, params: list) -> list:
        """
        Runs the data extraction pipeline.

        Returns:
            list: A list of extracted file paths.
        """
        ## extract Data
        maked_endpoint = SRV_URL + '/last/' + ','.join(params)
        loggingInfo(f"Sending request to: {SRV_URL + '/last/'} :: 1 of 3", WORK_DIR)
        response = requests.get(maked_endpoint)
        
        for tryNumber in range(3):
            if response.ok:
                loggingInfo(f"Request finished with status {response.status_code}", WORK_DIR)
                json_data = response.json()
                break
            else:
                if tryNumber <2:
                    loggingWarn(f"response error, status_code {response.status_code}. Retrying in {retry_time} seconds...", WORK_DIR)
                    for _ in tqdm(range(100), total=100, desc=f"loading"):
                        time.sleep(retry_time / 100)
                    loggingInfo(f"Sending request to: {SRV_URL + '/last/'} :: {tryNumber + 2} of 3", WORK_DIR)
                else:
                    loggingWarn("Attempt limits exceeded", WORK_DIR)
                    raise ConnectionError(f"Could not connect to the server after 3 attempts. Please try again later. Response status code: {response.status_code}") 
                    
        output_path = DefaultOutputFolder()
        insert_timestamp = DefaultTimestampStr()
        extracted_files = []
        totalParams = len(params)

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
            list(tqdm(executor.map(process_param, enumerate(params)), total=totalParams, desc="Processing files"))

        loggingInfo(f"{totalParams} files extracted in: {output_path}", WORK_DIR)    
            
        return extracted_files
            
    def GetGeneratedFiles(self) -> list:
        """
        Returns the generated files.

        Returns:
            list: A list of generated file paths.
        """
        return self.extractedFiles
    