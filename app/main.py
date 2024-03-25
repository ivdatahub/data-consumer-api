from extract import ApiToParquetFile
# from .transform import TransformAPIData

api = "https://economia.awesomeapi.com.br/last/BTC-USD"

myExtract = ApiToParquetFile.Save(api)