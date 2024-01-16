import os
import psycopg2
import pyarrow.parquet as pq

path = "/Users/ivsouza/repos/github.com/IvanildoBarauna/ETL-awesome-api/quotes-api/data/raw/"

class PostGresIntegration:
    def __init__(self, Folder: str) -> None:
        self.connection = {
                'host': 'localhost',
                'port': '5432',
                'database': 'DW',
                'user': 'SVC_DW',
                'password': 'SVC_DW'}
        self.folder = Folder
        
        self.CreateDynamicTable()
        self.ListNewFiles()

    def CreateDynamicTable(self):
        files = os.listdir(self.folder) 
                
        # Conecte-se ao PostgreSQL
        with psycopg2.connect(**self.connection) as conn:
            # Abra um cursor para executar comandos SQL
            with conn.cursor() as cursor:
                for file in files:
                    file_schema = pq.read_schema(path + file, memory_map=True)
                    schema_processing = [item + " text" for item in file_schema.names]
                    table_schema = ', '.join(schema_processing)
                
                    table_name = '-'.join(file.split("-")[0:2])
                    query = f"""CREATE TABLE IF NOT EXISTS "STG"."{table_name}" ({table_schema + ", filename text, ts_execution timestamp with time zone"});"""
                    
                    cursor.execute(query)
        
    def ListNewFiles(self):
        files = os.listdir(self.folder) 
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
                    
                    NewFiles =  list(
                        set(files) -  set(files_in_db)
                    )
                    
                    return NewFiles
                
    
new = PostGresIntegration(Folder=path)