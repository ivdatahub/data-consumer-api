from extract import ApiToParquetFile
# from .transform import TransformAPIData

endpoint_uri = "https://economia.awesomeapi.com.br/last/BTC-USD"

myExtract = ApiToParquetFile.Save(endpoint_uri)