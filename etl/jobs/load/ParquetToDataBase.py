from etl.jobs.load import (
    DefaultOutputFolder, CustomBeam, pyArrowParquet, ConsoleError, ConsoleInfo, ConsoleWarning, NewDBConnection
    ,QUOTES_API_SCHEMA
)

import os

class pgLoading:
    def __init__(self) -> None:
        self.CreateDynamicTable()
        self.NewFilesForLoad = self.ListNewFiles()
        self.PipelineRun()
            
    def CreateDynamicTable(self):
        output_path = DefaultOutputFolder()
        files = os.listdir(output_path)
        ConsoleInfo("CreateDynamicTable: Start")
        
        for file in files:
            table_name = file.split("-")[0:2]
            table_name = '-'.join(table_name)
            query = f"""CREATE TABLE IF NOT EXISTS "STG"."{table_name}" ({QUOTES_API_SCHEMA + ", filename text, ts_execution timestamp with time zone"});"""
        
        #  try:                            
        #     with NewDBConnection.pgConnection() as conn:            
        #         with conn.cursor() as cursor:
                
        #             cursor.execute(query)
                        
        #             ConsoleInfo(f"CreateDynamicTable: Table Created: >>> 'STG'.{table_name}")
        # except Exception as err:
        #     ConsoleError(f"CreateDynamicTable: >>> {err}")      
        
    def ListNewFiles(self):
        """
        SUMMARY: List new files from extracted files comparing with loaded files in database.
        """
        ConsoleInfo("Start Discovery new files for extract")
        files = self.files 
        tables =  [item.split("-")[0:2] for item in files]
        tables = set(tuple(elemento) for elemento in tables)
                
        
        with NewDBConnection.pgConnection() as conn:
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
                
    class WriteToPostGress(CustomBeam.BeamObj().DoFn): 
        def __init__(self, postgres_config):
            self.conn = postgres_config
            
        
        def process(self, element):
            ConsoleInfo("InsertNewFileToPostgres: Start")
            try:
                ## Refatorar para pegar de um componente que devolve o cursor e conector
                with NewDBConnection.pgConnection() as conn:
                    
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
        self.CreateDynamicTable()
        files = self.NewFilesForLoad 
        ConsoleInfo("Starting pipeline")
        for file in files:
            ConsoleInfo(f"Reading >>> {file}")
            try:
                with CustomBeam.PipelineDirectRunner() as p:
                    beam_pipe = (
                        p 
                        | "ReadParquet" >> CustomBeam.BeamObj().io.ReadFromParquetBatched(file_pattern=file)
                        | "ProcessFile" >> CustomBeam.BeamObj().ParDo(self.WriteToPostGress(self.connection))
                    )
                ConsoleInfo(f"Writed >>>> {file}")
            except Exception as err:
                ConsoleError(f"Pipeline error: {err}")