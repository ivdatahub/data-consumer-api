import psycopg2
import yaml

class dbEnviroment:
    def __init__(self) -> None:
        self.dbParameters = self.dbParams()
        self.HOST = self.dbParams()
        self.PORT = 5432
    
    def dbParams():
        pass
    
    
with open('docker-compose.yaml', 'r') as DockerComposeFile:
    FileContent = yaml.safe_load(DockerComposeFile)
    dbEnvParams = FileContent["services"]["dw-service"]["environment"]
    
print(dbEnvParams.keys())

conn = {
            'host': 'localhost',
            'port': '5432',
            'database': 'DW',
            'user': 'SVC_DW',
            'password': 'SVC_DW'}


# def dbConnection():
#     return psycopg2.connect(
        
#     )    