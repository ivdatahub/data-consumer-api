import psycopg2


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
        query = """ 
        INSERT INTO "STG".teste(teste) VALUES (2);
        """
        # values = (element['coluna1'], element['coluna2'])
        cursor.execute(query)