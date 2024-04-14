from etl.jobs.extract import (
    pyarrow, requests, loggingInfo, loggingError, loggingWarn
     ,DefaultOutputFolder, DefaultTimestampStr, DefaultQuotesAPISchema
     ,CustomBeam, ENDPOINT_QUOTES_AWESOME_API, WORK_DIR
)

class extraction: 
    def __init__(self, ValidParams: list) -> None:
        self.params = ValidParams
        self.PipelineRun()

    def PipelineRun(self):
        response = requests.get(ENDPOINT_QUOTES_AWESOME_API + ','.join(self.params))

        if response.ok:
            json_data = response.json()
            params = self.params
        else:
            raise ConnectionError(f"endpoint connection: {ENDPOINT_QUOTES_AWESOME_API}. status_code: {response.status_code}")
                
        FileSchema = DefaultQuotesAPISchema()
        output_path = DefaultOutputFolder()
        insert_timestamp = DefaultTimestampStr()
        beam = CustomBeam.BeamObj()
        extracted_files = []

        for index, param in enumerate(params):
            dic = json_data[param.replace("-", "")]
    
            loggingInfo(f"{index + 1} of {len(params)} - {param} - Starting", WORK_DIR)
            
            with CustomBeam.PipelineDirectRunner() as pipe:
                input_pcollection = (
                    pipe
                    | "Create" >> beam.Create([dic])
                    | "WriteToParquet"
                    >> beam.io.WriteToParquet(
                        file_path_prefix=f"{output_path}{param}-{insert_timestamp}",
                        file_name_suffix=".parquet",
                        num_shards=1,
                        schema=FileSchema,
                    )
                )

            loggingInfo(f"{index + 1} of {len(params)} - {param} - file extracted: {output_path}{param}-{insert_timestamp}", WORK_DIR)
            
        loggingInfo(f"All files extracted in: {output_path}", WORK_DIR)