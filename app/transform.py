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
    def __init__(self, FolderFiles: str) -> None:
        self.path =  FolderFiles
        self.pipe_options = PipelineOptions(['--runner', 'Direct'])
        self.connection =  {
            'host': 'localhost',
            'port': '5432',
            'database': 'DW',
            'user': 'SVC_DW',
            'password': 'SVC_DW'}
        self.files = os.listdir(self.path)
        
        self.CreateDynamicTable()
            
    def CreateDynamicTable(self):
        """ 
        SUMMARY: Create dynamic table from new extracted files.
        """
        files = self.files
        ConsoleInfo("CreateDynamicTable: Start")
        
        try:                
        # Conecte-se ao PostgreSQL
            with psycopg2.connect(**self.connection) as conn:
                # Abra um cursor para executar comandos SQL
                with conn.cursor() as cursor:
                    for file in files:
                        file_schema = pq.read_schema(self.path + file, memory_map=True)
                        schema_processing = [item + " text" for item in file_schema.names]
                        table_schema = ', '.join(schema_processing)


                        table_name = file.split("-")[0:2]
                        table_name = '-'.join(table_name)
                        query = f"""CREATE TABLE IF NOT EXISTS "STG"."{table_name}" ({table_schema + ", filename text, ts_execution timestamp with time zone"});"""
                        
                        cursor.execute(query)
                        
                        ConsoleInfo(f"CreateDynamicTable: Table Created: >>> 'STG'.{table_name}")
        except Exception as err:
            ConsoleError(f"CreateDynamicTable: >>> {err}")      
        
    def ListNewFiles(self):
        """
        SUMMARY: List new files from extracted files comparing with loaded files in database.
        """
        ConsoleInfo("Start Discovery new files for extract")
        files = self.files 
        tables =  [item.split("-")[0:2] for item in files]
        tables = set(tuple(elemento) for elemento in tables)
                
        # Conecte-se ao PostgreSQL
        with psycopg2.connect(**self.connection) as conn:
            # Abra um cursor para executar comandos SQL
            with conn.cursor() as cursor:
                for table in tables:
                    table  = '-'.join(table)
                    query = f"""
                    SELECT distinct filename FROM "STG"."{table}"
                    """
                    
                    cursor.execute(query)
                    
                    files_in_db = cursor.fetchall()
                    files_in_db = [item[0] for item in files_in_db]
                    
                    # if len(files_in_db) >0: 
                    NewFiles =  list(set(files) -  set(files_in_db)) 
                    NewFiles = [self.path + item for item in NewFiles]
                    ConsoleInfo(f"ListNewFiles: Files for Extract: >>> {[print(item) for item in NewFiles]}")

                    return NewFiles
                
    class WriteToPostGress(beam.DoFn): 
        def __init__(self, postgres_config):
            self.conn = postgres_config
            
        
        def process(self, element):
            ConsoleInfo("InsertNewFileToPostgres: Start")
            try:
                # Conecte-se ao PostgreSQL
                with psycopg2.connect(**self.conn) as conn:
                    # Abra um cursor para executar comandos SQL
                    with conn.cursor() as cursor:
                        columns = ', '.join(element.column_names)
                        placeholders = ', '.join(['%s'] * len(element))
                        
                        query = f""" 
                            INSERT INTO nome_tabela ({columns})
                            VALUES ({placeholders})
                        """
                        
                        ## BREAK: Adicionar a lógica que lê os dados do parquet com um loop e monta a string da query dinamicamente.
                        values = tuple(element.values())
                        
                        cursor.execute(query, values)
                        ConsoleInfo("InsertNewFileToPostgres: Done")
            except Exception as err:
                ConsoleError(f"InsertNewFileToPostgres Error >>> {err}")
                    
        
    def PipelineRun(self):
        NewFilesForExtract = self.ListNewFiles()
        ConsoleInfo("Starting pipeline")
        for file in NewFilesForExtract:
            ConsoleInfo(f"Reading >>> {file}")
            try:
                with beam.Pipeline(options=self.pipe_options) as p:
                    beam_pipe = (
                        p 
                        | "ReadParquet" >> beam.io.ReadFromParquetBatched(file_pattern=file)
                        | "ProcessFile" >> beam.ParDo(self.WriteToPostGress(self.connection))
                        # | "ReadFromParquetFile" >> beam.io.ReadFromParquetBatched(self.path)
                        # | "Parquet to Pandas" >> beam.Map(lambda x: x.to_pandas())
                        # | "ProcessarDados" >> beam.Map(processar_dados)
                        # | "Printing DataFrame" >> beam.Map(lambda x: print(x.to_pandas()))
                    )
                ConsoleInfo(f"Writed >>>> {file}")
            except Exception as err:
                ConsoleError(f"Pipeline error: {err}")