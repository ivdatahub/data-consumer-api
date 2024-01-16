## Apache Beam imports
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam

## PostGres
import psycopg2

## PyArrow for read .parquet file
import pyarrow.parquet as pq

import os

# Custom Logs
from .logs import ConsoleInfo, ConsoleError, ConsoleWarning


class TransformAPIData:
    def __init__(self, FolderFiles) -> None:
        self.path =  FolderFiles
        self.pipe_options = PipelineOptions(['--runner', 'Direct'])
        self.postgres_conn =  {
            'host': 'localhost',
            'port': '5432',
            'database': 'DW',
            'user': 'SVC_DW',
            'password': 'SVC_DW'}
        
    def WriteToPostGres(self):
        conn = {
                'host': 'localhost',
                'port': '5432',
                'database': 'DW',
                'user': 'SVC_DW',
                'password': 'SVC_DW'}
                
        # Conecte-se ao PostgreSQL
        with psycopg2.connect(**conn) as conn:
            # Abra um cursor para executar comandos SQL
            with conn.cursor() as cursor:
                for file in os.listdir(self.path):
                    file_schema = pq.read_schema(self.path + file, memory_map=True)
                    schema_processing = [item + " text" for item in file_schema.names]
                    table_schema = ', '.join(schema_processing)
                
                    table_name = '-'.join(file.split("-")[0:2])
                    query = f"""CREATE TABLE IF NOT EXISTS "STG"."{table_name}" ({table_schema + ", filename text, ts_execution timestamp with timezone"});"""
                    
                    cursor.execute(query)
                    
                    query = f"""
                        SELECT COUNT(1) FROM "STG"."{table_name}"
                    """
        
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