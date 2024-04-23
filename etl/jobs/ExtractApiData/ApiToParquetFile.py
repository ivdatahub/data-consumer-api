from etl.jobs.ExtractApiData import (
    requests
    ,pandas as pd
    ,loggingInfo
    ,loggingWarn
    ,DefaultOutputFolder
    ,DefaultTimestampStr
    ,DefaultUTCDatetime
    ,ENDPOINT_QUOTES_AWESOME_API, WORK_DIR
)

import concurrent.futures
import threading
import time

counter = 0

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
        maked_endpoint = ENDPOINT_QUOTES_AWESOME_API + ','.join(params)
        loggingInfo(f"Sending request: {maked_endpoint}", WORK_DIR)
        response = requests.get(maked_endpoint)

        for tryNumber in range(3):
            try:
                if response.ok:
                    loggingInfo(f"Request finished", WORK_DIR)
                    json_data = response.json()
                    break
                else:
                    raise ConnectionError(f"endpoint connection: {ENDPOINT_QUOTES_AWESOME_API}.status_code: {response.status_code}")
            except ConnectionError as e:
                if tryNumber <2:
                    loggingWarn(f"{e}, retrying again in 5 seconds...", WORK_DIR)
                    time.sleep(5)
                else:
                    raise e
                    
        output_path = DefaultOutputFolder()
        insert_timestamp = DefaultTimestampStr()
        extracted_files = []
        totalParams = len(params)

        def process_param(args):
            global counter
            
            index, param = args
            dic = json_data[param.replace("-", "")]
            
            with threading.Lock():
                thread_num = counter
                counter += 1
            
            loggingInfo(f"{index + 1} of {totalParams} - {param} - Transforming using thread: {thread_num}", WORK_DIR)
            
            # Convert 'dic' to a Pandas DataFrame
            df = pd.DataFrame([dic])
            
            # Add new columns to the DataFrame
            df["symbol"] = param
            
            # Add two columns with the current date and time           
            df["extracted_at"] = DefaultUTCDatetime()
            
            loggingInfo(f"{index + 1} of {totalParams} - {param} - Loading using thread: {thread_num}", WORK_DIR)
            
            # Write the DataFrame to a Parquet file
            df.to_parquet(f"{output_path}{param}-{insert_timestamp}.parquet")
            
            # Append list with the file path
            extracted_files.append(f"{output_path}{param}-{insert_timestamp}.parquet")

            loggingInfo(f"{index + 1} of {totalParams} - {param} - saved file using thread: {thread_num}", WORK_DIR)

        ## Parallel Processing data
        with concurrent.futures.ThreadPoolExecutor(4) as executor:
            list(executor.map(process_param, enumerate(params)))

        loggingInfo(f"All files extracted in: {output_path}", WORK_DIR)    
            
        return extracted_files
            
    def GetGeneratedFiles(self) -> list:
        """
        Returns the generated files.

        Returns:
            list: A list of generated file paths.
        """
        return self.extractedFiles
    