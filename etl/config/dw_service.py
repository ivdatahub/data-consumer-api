# import psycopg2
import yaml
import psycopg2

class NewDBConnection:
    def __init__(self) -> None:
        self.conn =  GetConnectionsParameters()
        
        def GetConnectionsParameters() -> dict:
            with open('docker-compose.yaml', 'r') as DockerComposeFile:
                FileContent = yaml.safe_load(DockerComposeFile)
                dwService = FileContent["services"]["dw-service"]
                dbEnvParams = dwService["environment"]
                
            PORT = dwService["ports"][0].split(":")[0]
            USER = dbEnvParams["POSTGRES_USER"]
            PASS = dbEnvParams["POSTGRES_PASSWORD"]
            DB_NAME = dbEnvParams["POSTGRES_DB"]
            
            return  {
                'host': 'localhost',
                'port': PORT,
                'database': DB_NAME,
                'user': USER,
                'password': PASS
                }
        
    def pgConnection(self): 
        return psycopg2.connect(self.conn)
        