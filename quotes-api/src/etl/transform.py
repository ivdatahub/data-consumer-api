## Apache Beam imports
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam

## PostGres
import psycopg2

# Custom Logs
from .logs import ConsoleInfo, ConsoleError, ConsoleWarning


class TransformAPIData:
    def __init__(self, FolderFiles) -> None:
        self.path =  FolderFiles
        self.pipe_options = PipelineOptions([
            '--runner', 'Direct'
        ])
        
    def WriteToPostGres(self, element):        
        connection_params = {
            'host': 'localhost',
            'port': '5432',
            'database': 'DW',
            'user': 'SVC_DW',
            'password': 'SVC_DW'}
        
         # Conecte-se ao PostgreSQL
        with psycopg2.connect(**connection_params) as conn:
            # Abra um cursor para executar comandos SQL
            with conn.cursor() as cursor:
                # Exemplo de inserção de dados (substitua isso com sua lógica específica)
                query = "select 1"
                # values = (element['coluna1'], element['coluna2'])
                cursor.execute(query)
        
    def PipelineRun(self):
        ConsoleInfo("Starting pipeline")
        try:
            with beam.Pipeline(options=self.pipe_options) as p:
                beam_pipe = (
                    p 
                    | "ReadFromParquetFile" >> beam.io.ReadFromParquetBatched(self.path)
                    | "Parquet to Pandas" >> beam.Map(lambda x: x.to_pandas())
                    | "Printing DataFrame" >> beam.Map(print)
                )
            ConsoleInfo("Finished pipeline")
        except Exception as err:
            ConsoleError(f"Pipeline error: {err}")