from etl.jobs.ExtractApiData import (
    requests
    ,pandas as pd
    ,loggingInfo
    ,DefaultOutputFolder
    ,DefaultTimestampStr
    ,DefaultUTCDatetime
    ,ENDPOINT_QUOTES_AWESOME_API, WORK_DIR
)

import concurrent.futures

class extraction: 
    def __init__(self, ValidParams: list) -> None:
        """
        Initializes the extraction class.

        Args:
            ValidParams (list): A list of valid parameters.

        Returns:
            None
        """
        self.params = ValidParams
        self.extractedFiles = self.PipelineRun()

    def PipelineRun(self) -> list:
        """
        Runs the data extraction pipeline.

        Returns:
            list: A list of extracted file paths.
        """
        ## extract Data
        maked_endpoint = ENDPOINT_QUOTES_AWESOME_API + ','.join(self.params)
        loggingInfo(f"Sending request: {maked_endpoint}", WORK_DIR)
        response = requests.get(maked_endpoint)

        if response.ok:
            loggingInfo(f"Request finished", WORK_DIR)
            json_data = response.json()
            params = self.params
        else:
            raise ConnectionError(f"endpoint connection: {ENDPOINT_QUOTES_AWESOME_API}. status_code: {response.status_code}")
                
        output_path = DefaultOutputFolder()
        insert_timestamp = DefaultTimestampStr()
        extracted_files = []

        def process_param(args):
            index, param = args
            dic = json_data[param.replace("-", "")]
            
            loggingInfo(f"{index + 1} of {len(params)} - {param} - Transforming..", WORK_DIR)
            
            # Convert 'dic' to a Pandas DataFrame
            df = pd.DataFrame([dic])
            
            # Add new columns to the DataFrame
            df["symbol"] = param
            
            # Add two columns with the current date and time           
            df["extracted_at"] = DefaultUTCDatetime()
            
            loggingInfo(f"{index + 1} of {len(params)} - {param} - Loading...", WORK_DIR)
            
            # Write the DataFrame to a Parquet file
            df.to_parquet(f"{output_path}{param}-{insert_timestamp}.parquet")

            loggingInfo(f"{index + 1} of {len(params)} - {param} - saved file: {output_path}{param}-{insert_timestamp}", WORK_DIR)

        ## Processing data
        with concurrent.futures.ThreadPoolExecutor() as executor:
            list(executor.map(process_param, enumerate(params)))
            
            
            #### old
            
            

            extracted_files = []
            
        loggingInfo(f"All files extracted in: {output_path}", WORK_DIR)    
            
        return extracted_files
            
    def GetExtractedFilesList(self) -> list:
        """
        Returns the list of extracted files.

        Returns:
            list: A list of extracted file paths.
        """
        return self.extractedFiles