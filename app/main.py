from .extract import ExtractDataAPI
from .transform import TransformAPIData
import os

api = "https://economia.awesomeapi.com.br/last/BTC-USD,ETH-USD,USD-BRL"
path = "/Users/ivsouza/repos/github.com/IvanildoBarauna/ETL-awesome-api/quotes-api/data/raw/"

NewTransform = TransformAPIData(FolderFiles=path)
NewTransform.PipelineRun()