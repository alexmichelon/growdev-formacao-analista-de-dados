import database.manipulate_db as mdb

table_schema = 'trabalho_pratico_ii'

#método para criar conexão com o banco de dados
def connection():
    host = 'localhost'
    user = 'root'
    password = 'root123'    
    engine = mdb.create_engine_db_connection(host, user, password, table_schema)
    return engine
    
class Data:
    #variáveis para utilização nas classes dos gráficos
    join_column = 'player_id'
    reference_column = 'name'
    global_column_1 = 'current_team'
    global_column_1_label = 'Teams'
    global_column_2_label = 'Positions'
    global_column_2 = 'position' 
    value = 0
    erros='ignore'
         
    
    engine = connection()
    
    df_db, df_tables = mdb.generate_df_db(engine, table_schema, join_column, value, erros, reference_column)
    df = df_db

    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df_numeric = df.select_dtypes(include=numerics)
    
    #retorna colunas do DataFrame ordenados alfabeticamente
    def get_column():
        return Data.df.columns.sort_values()
    #retorna colunas do DataFrame numérico ordenados alfabeticamente
    def get_numeric_column():       
        return Data.df_numeric.columns.sort_values()
    #retorna valores da coluna do DataFrame
    def get_column_values(column):
        return Data.df[column].unique()