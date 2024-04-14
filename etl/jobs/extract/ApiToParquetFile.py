from etl.jobs.extract import (
    pyarrow, requests, loggingInfo, loggingError, loggingWarn
     ,DefaultOutputFolder, DefaultTimestampStr, CustomBeam
    ,ENDPOINT_LIST_AVALIABLE_PARITYS, ENDPOINT_QUOTES_AWESOME_API, WORK_DIR
)

class extraction: 
    def __init__(self, *xargs: str) -> None:
        self.params = xargs[0]
        self.PipelineRun()
        
    def APIToDicionary(self):
        loggingInfo(msg="[STARTING NEW PIPELINE]", module=WORK_DIR)
        valParams = []
        list_of_avaliable = requests.get(ENDPOINT_LIST_AVALIABLE_PARITYS).json()
        
        for param in self.params:
            if param in list_of_avaliable:
                valParams.append(param)
            else:
                loggingWarn(f"Param: {param} is not valid for call", WORK_DIR)
    
        if valParams:
            loggingInfo(f"Parameters OK >>> {valParams}", WORK_DIR)
            response = requests.get(ENDPOINT_QUOTES_AWESOME_API + ','.join(valParams))
            if response.ok:
                loggingInfo(f"Response OK >>> {response}", WORK_DIR)
                return dict(responseData=response.json(), params=valParams)
            else:
                loggingError(f"Response failed >>> {response}", WORK_DIR)
        else:
            loggingError("There are not valid params for extract.",  WORK_DIR)

    def ParquetSchemaLoad(self, element: dict):
        try:
            api_header = list(element.keys())
            schema = []

            for field in api_header:
                schema += [(field, pyarrow.string())]

            beam_schema = pyarrow.schema(schema)
            loggingInfo("Schema - 200 OK", WORK_DIR)

            return beam_schema

        except Exception as Err:
            loggingError(f"Schema - Error >>>> {Err}", WORK_DIR)

    def PipelineRun(self):
        response = self.APIToDicionary()
        if response:
            json_data = response["responseData"]
            params = response["params"]
            
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
                        