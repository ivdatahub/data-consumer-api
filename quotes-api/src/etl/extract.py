# Apache Beam Dependencies
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# Auxiliar Dependencies
import pyarrow
import requests
from datetime import datetime

# Custom Logs
from .logs import ConsoleInfo, ConsoleError, ConsoleWarning

class ExtractDataAPI:
    """
    ** Summary **: 
        ExtractDataAPI is class for extract data from endpoint and export in .parquet file for processing.
    

    *** args ***:
        endpoint (string), output_path (string)
        
        Use:
        
        MyAPI = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    
        NewExtract = ExtractDataAPI(endpoint=api, output_path="/.DataSource/")
        NewExtract.PipelineRun()
        
    """
    
    def __init__(self, endpoint: str, output_path: str) -> None:
        self.endpoint = endpoint
        self.output_path = output_path
        self.pipe_options = PipelineOptions(
            ["--runner", "Direct", "--direct_num_workers=1"]
        )
        self.ExtractedFilePath = []
        self.ValidParams = []

    def APIToDicionary(self):
        """
        ** Summary **: 
            APIToDicionary is a method for return valid dicionary and params for extract Currency awesomeAPI.
        

        *** noargs ***:
            -- 
            
            Use:
            
                dic = APIToDicionary()
        
            returns:

                response_list = dic["responseData] with reponse data in JSON
                params_list = dic["params] with valid currencys for JSON filter
        """
        def ValidListOfParams():
            """
            ** Summary **: 
                ValidListOfParams is a method for return validate list of params.
                OBS: Use "https://economia.awesomeapi.com.br/json/available" with datasource for define if currency is valid or not. 
            
            *** noargs ***:
                -- 
                
                Use:
                
                    MyValidParams = ValidListOfParams()
            
                returns:

                    List of params without transform. Ex
            """
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
        """ 
            CurrentTimestampStr is a method for return actual timestamp as string.
            Use case: For name of .parquet file
            
            returns: 
                actual timestamp as string
        """
        current = datetime.now().timestamp()
        return str(int(current))

    def ParquetSchemaLoad(self, element: dict):
        """ 
        ParquetSchemaLoad is a method for return ParquetSchema using pyarrow lib
        
        args: 
            element (dicionary)
        returns: 
            pyarrow.schema of element arg
        """
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
        """ 
        Sumary: 
            PipelineRun: The main method of extract API Data
        
        noargs:
        
        returns:
        
            Apache Beam read and map the dictionary of API and export for prefered path (passed as arg, see ExtractDataAPI )
            Export Format: for each currency passed as args will generated one file per each currency, follow examples: 
            
            Ex1: 
                api = "https://economia.awesomeapi.com.br/last/USD-BRL"
                NewExtract = ExtractDataAPI(endpoint=api, output_path="./")
            return Will generated only USD-BRL file
            
            like this:
            .
            └── USDBRL_1705088794-00000-of-00001.parquet
            
            
            Ex2:
                api = "https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL,ETH-USD"
                NewExtract = ExtractDataAPI(endpoint=api, output_path="./")
            return Will generated tree files one for each currency
            
            like this:
            .
            ├── BTCBRL_1705089414-00000-of-00001.parquet
            ├── ETHUSD_1705089414-00000-of-00001.parquet
            └── USDBRL_1705089414-00000-of-00001.parquet

            Ex3:
                api = "https://economia.awesomeapi.com.br/last/hahaah"
                NewExtract = ExtractDataAPI(endpoint=api, output_path="./")
                return log in console and not execute request and pipeline
                
            like this:
            2024-01-12 16:59:05,071 - INFO -  Param: hahaah is not valid for call
            
        """
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