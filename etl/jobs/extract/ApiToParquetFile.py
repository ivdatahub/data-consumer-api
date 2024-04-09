from etl.jobs.extract import (
    pyarrow, requests, ConsoleInfo, ConsoleError, ConsoleWarning
     ,DefaultOutputFolder, DefaultTimestampStr, CustomBeam
    ,ENDPOINT_LIST_AVALIABLE_PARITYS, ENDPOINT_QUOTES_AWESOME_API
)

class extraction: 
    def __init__(self, *xargs: str) -> None:
        self.params = xargs
        self.PipelineRun()
        
    def APIToDicionary(self):
        valParams = []
        list_of_avaliable = requests.get(ENDPOINT_LIST_AVALIABLE_PARITYS).json()
        
        for param in self.params:
            if param in list_of_avaliable:
                valParams.append(param)
            else:
                ConsoleWarning(f"Param: {param} is not valid for call")
    
        if valParams:
            ConsoleInfo(f"Parameters OK >>> {valParams}")
            response = requests.get(ENDPOINT_QUOTES_AWESOME_API + ','.join(valParams))
            if response.ok:
                ConsoleInfo(f"Response OK >>> {response}")
                return dict(responseData=response.json(), params=valParams)
            else:
                ConsoleError(f"Response failed >>> {response}")

    def ParquetSchemaLoad(self, element: dict):
        try:
            api_header = list(element.keys())
            schema = []

            for field in api_header:
                schema += [(field, pyarrow.string())]

            beam_schema = pyarrow.schema(schema)
            ConsoleInfo("Schema - 200 OK")

            return beam_schema

        except Exception as Err:
            ConsoleInfo(f"Schema - Error >>>> {Err}")

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
                        ConsoleInfo(f"Starting pipeline {index + 1} of {len(params)} - {param} - Starting!")
                        
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

                        ConsoleInfo(f"Pipeline execution OK >> {index + 1} of {len(params)} - {param} - Extracted!")

                        extracted_files.append(f"{output_path}{param}-{insert_timestamp}-00000-of-00001.parquet")
                    
                    except Exception as err:
                        ConsoleError(f"{param} - Pipeline Execution Error >>>  {err}")
                        