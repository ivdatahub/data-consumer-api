from extract import (
    beam
    ,os
    ,requests
    ,ConsoleWarning
    ,ConsoleInfo
    ,ConsoleError
    ,datetime
    ,pyarrow
)

from config import BeamDirectRunnerOptions, OutputFolder

class extraction:    
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
        self.output_path = OutputFolder
        self.pipe_options = BeamDirectRunnerOptions(workers=1)
        self.ExtractedFilePath = []
        self.ValidParams = []
        self.PipelineRun()
        
    def APIToDicionary(self):
        def ValidListOfParams():
            arr_endpoint = self.endpoint.split("/")
            params = arr_endpoint[len(arr_endpoint) - 1]
            lstParams = params.split(",")
            
            list_of_avaliable = requests.get("https://economia.awesomeapi.com.br/json/available").json()
            
            valParams = []
            
            for param in lstParams:
                if param in list_of_avaliable:
                    valParams.append(param)
                else:
                    ConsoleWarning(f"Param: {param} is not valid for call")
            
            self.endpoint = self.endpoint.replace(''.join(params), ','.join(valParams))
            return valParams
        ## Se for válido segue
        
        ParamsValidate = ValidListOfParams()
        if ParamsValidate:
            ConsoleInfo(f"Parameters OK >>> {ParamsValidate}")
            response = requests.get(self.endpoint)
            if response.ok:
                ConsoleInfo(f"Response OK >>> {response}")
                return dict(responseData=response.json(), params=ParamsValidate)
            else:
                ConsoleError(f"Response failed >>> {response}")

    def CurrentTimestampStr(self) -> str:
        current = datetime.now().timestamp()
        return str(int(current))

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
            ## Extract Schema              
            FileSchema = self.ParquetSchemaLoad(json_data[extract_index_params[0]]
                                                )
            insert_date = self.CurrentTimestampStr()

            for index, param in enumerate(params):
                dic = json_data[param.replace("-", "")]

                if dic:
                    try:
                        ConsoleInfo(
                            f"Starting pipeline {index + 1} of {len(params)} - {param} - Starting!"
                        )
                        with beam.Pipeline(options=self.pipe_options) as pipe:
                            input_pcollection = (
                                pipe
                                | "Create" >> beam.Create([dic])
                                | "WriteToParquet"
                                >> beam.io.WriteToParquet(
                                    file_path_prefix=f"{self.output_path}{param}-{insert_date}",
                                    file_name_suffix=".parquet",
                                    num_shards=1,
                                    schema=FileSchema,
                                )
                            )

                        ConsoleInfo(
                            f"Pipeline execution OK >> {index + 1} of {len(params)} - {param} - Extracted!"
                        )

                        self.ExtractedFilePath.append(
                            f"{self.output_path}{param}-{insert_date}-00000-of-00001.parquet"
                        )
                        

                    except Exception as err:
                        ConsoleError(f"{param} - Pipeline Execution Error >>>  {err}")

def PipelineExecute(uri: str): 
    extraction(endpoint=uri)