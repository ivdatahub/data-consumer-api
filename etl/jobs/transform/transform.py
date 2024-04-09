
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam


import psycopg2


import pyarrow.parquet as pq

import os


from utils.logs import ConsoleInfo, ConsoleError, ConsoleWarning


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
        files = self.files
        ConsoleInfo("CreateDynamicTable: Start")
        
        try:                
        
            with psycopg2.connect(**self.connection) as conn:
                ## Refatorar para pegar de um componente que devolve o cursor e conector
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
                
        
        with psycopg2.connect(**self.connection) as conn:
            ## Refatorar para pegar de um componente que devolve o cursor e conector
            with conn.cursor() as cursor:
                for table in tables:
                    table  = '-'.join(table)
                    query = f"""
                    SELECT distinct filename FROM "STG"."{table}"
                    """
                    
                    cursor.execute(query)
                    
                    files_in_db = cursor.fetchall()
                    files_in_db = [item[0] for item in files_in_db]
                    
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
                ## Refatorar para pegar de um componente que devolve o cursor e conector
                with psycopg2.connect(**self.conn) as conn:
                    
                    with conn.cursor() as cursor:
                        columns = ', '.join(element.column_names)
                        placeholders = ', '.join(['%s'] * len(element))
                        
                        query = f""" 
                            INSERT INTO nome_tabela ({columns})
                            VALUES ({placeholders})
                        """
                        
                        ## TODO: Adicionar a lógica que lê os dados do parquet com um loop e monta a string da query dinamicamente.
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
                    )
                ConsoleInfo(f"Writed >>>> {file}")
            except Exception as err:
                ConsoleError(f"Pipeline error: {err}")