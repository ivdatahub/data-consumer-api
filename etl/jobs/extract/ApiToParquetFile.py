from etl.jobs.extract import (
    pyarrow, requests, loggingInfo, loggingError, loggingWarn
     ,DefaultOutputFolder, DefaultTimestampStr, CustomBeam
    , ENDPOINT_QUOTES_AWESOME_API, WORK_DIR
)

class extraction: 
    def __init__(self, ValidParams: list) -> None:
        self.params = ValidParams
        self.PipelineRun()

    def ParquetSchemaLoad(self, element: dict):
        api_header = list(element.keys())
        schema = []

        for field in api_header:
            schema += [(field, pyarrow.string())]

        beam_schema = pyarrow.schema(schema)
        loggingInfo("Schema - 200 OK", WORK_DIR)

        return beam_schema

    def PipelineRun(self):
        response = requests.get(ENDPOINT_QUOTES_AWESOME_API + ','.join(self.params))

        if response.ok:
            json_data = response.json()
            params = self.params
        else:
            raise ConnectionError(f"endpoint connection: {ENDPOINT_QUOTES_AWESOME_API}. status_code: {response.status_code}")
            
        ## For generate schema is necessary extract one currency from dicionary
        extract_index_params = [item.replace("-", "") for item in params]      
        
        FileSchema = self.ParquetSchemaLoad(json_data[extract_index_params[0]])

        for index, param in enumerate(params):
            dic = json_data[param.replace("-", "")]

            if dic:
                output_path = DefaultOutputFolder()
                insert_timestamp = DefaultTimestampStr()
                beam = CustomBeam.BeamObj()
                extracted_files = []
                try:
                    loggingInfo(f"Starting pipeline {index + 1} of {len(params)} - {param} - Starting!", WORK_DIR)
                    
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

                    loggingInfo(f"Pipeline execution OK >> {index + 1} of {len(params)} - {param} - Extracted!", WORK_DIR)

                    extracted_files.append(f"{output_path}{param}-{insert_timestamp}-00000-of-00001.parquet")
                
                except Exception as err:
                    loggingError(f"{param} - Pipeline Execution Error >>>  {err}", WORK_DIR)
                    