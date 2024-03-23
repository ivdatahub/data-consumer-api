from etl.extract import ExtractDataAPI
from etl.transform import TransformAPIData
import os

api = "https://economia.awesomeapi.com.br/last/BTC-USD,ETH-USD,USD-BRL"
path = "/Users/ivsouza/repos/github.com/IvanildoBarauna/ETL-awesome-api/quotes-api/data/raw/"

# NewExtract = ExtractDataAPI(endpoint=api, output_path=path)
# NewExtract.PipelineRun()

NewTransform = TransformAPIData(FolderFiles=path)
NewTransform.PipelineRun()

# files = os.listdir(path)

# for file in files:
#     print(file)
