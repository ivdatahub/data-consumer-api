from etl.extract import ExtractDataAPI
from etl.transform import TransformAPIData
import os

api = "https://economia.awesomeapi.com.br/last/USD-BRL,ETH-USD,BTC-USD,USDL-BRL"
path = f"/Users/{os.getenv('USER')}/repos/data-engineer-portfolio/API-ETL/apache-beam/awesome_data_ingestion/data/raw/"

# NewExtract = ExtractDataAPI(endpoint=api, output_path=path)
# NewExtract.PipelineRun()

NewTransform = TransformAPIData(FolderFiles=path)
NewTransform.PipelineRun()
