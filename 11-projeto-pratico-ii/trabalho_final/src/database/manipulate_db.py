import database.generate_query as gquery
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

#função que cria conexão com o banco de dados
def create_engine_db_connection(host, user, password, database):
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    return engine

#função que cria um DataFrame a partir de um arquivo csv
def convert_csv_to_dataframe(csv_path): #csv_path: caminho do arquivo csv
    csv_path = csv_path
    df = pd.DataFrame(pd.read_csv(csv_path))
    df = normalize_columns_name(df) #ajusta caracteres do nome das colunas do arquivo csv
    return df

#função que busca informações o banco de dados e as converte em um DataFrame
def convert_sql_to_dataframe(query, connection): #query: consulta SQL a ser executada, connection: conexão com o banco de dados
    df = pd.read_sql(sql=query, con=connection)    
    return df

#função que substitui caracteres especiais para definição dos nomes das colunas do DataFrame
def normalize_columns_name(df):
    for c in '()':
        df.columns = df.columns.str.replace(c,'')
    df.columns = df.columns.str.replace(' ','_')
    df.columns = df.columns.str.replace('-','_')
    df.columns = df.columns.str.replace('+','plus')
    df = df.rename(columns=str.lower) #deixa o nome geradao todo em letras minúsculas
    return df
    
#função que define o nome da tabela do banco de dados a partir do nome do arquivo csv
def table_name(csv_path): #csv_path: caminho do arquivo csv
    file_name = csv_path[csv_path.rfind('/')+1:csv_path.rfind('.')].lower() #pega o trecho da str dentre o último ponto e a última barra invertida
    return file_name

#função que cria uma tabela no banco de dados (MySQL) com dados de um DataFrame 
def convert_dataframe_to_sql(df, file_name, connection, if_exists, index, index_label): #if_exists{‘fail’, ‘replace’, ‘append’}, default ‘fail’
    rows = df.to_sql(name=file_name, con=connection, if_exists=if_exists, index=index, index_label=index_label)
    return rows

#função que gera uma lista de diretórios de arquivos de um determinado tipo dado um endereço 
def list_files_of_path(full_path, file_type): #full_path: endereço onde se deseja buscar arquivos, file_type: tipo do arquivo
    directorys_files = Path(f'{full_path}').glob(f'*.{file_type}')
    return directorys_files

#função que transforma todos os dados dos arquivos do diretório em dados em tabelas no banco de dados MySQL
def file_to_db(connection, full_path, file_type, to_sql_if_exists): #connection: conexão com o banco, full_path: endereço a ser buscado arquivos, file_type: tipo de extensão de arquivo, to_sql_if_exists: ação a ser executada no banco de dados
    files = list_files_of_path(full_path, file_type) #lista os endereços dos arquivos dado uma extensão
    amount_rows = ''
    total_rows = 0
    for file in files: #busca cada endereço da lista de endereços dos arquivos
        file_name = table_name(repr(file)) #gera o nome da tabela
        df = convert_csv_to_dataframe(file) #gera um DataFrame a partir de um arquivo csv
        rows = convert_dataframe_to_sql(df, file_name, connection, to_sql_if_exists, False, None) #cria uma tabela com dados no banco de dados com dados do DataFrame
        total_rows += rows #incrementa o numero de linhas executadas no banco de dados
        amount_rows += f'Table: {file_name}: {rows} records inserted.\n' #insere informação de dados inseridos no banco
    amount_rows += f'Total: {total_rows} records inserted.'#itera texto de dados inseridos
    return amount_rows # retorna texto de dados inseridos

#função que retorna o nome das tabelas do banco de dados
def return_db_tables_name(connection, table_schema):
    table_name = 'information_schema.tables' #schema/banco de dados
    #columns_selected = 'table_schema, table_name, table_type'
    columns_selected = 'table_name' #colunas a serem retornadas
    where_clausule = f'table_schema = "{table_schema}"' #clausula Where aplicada
    query = gquery.query_create_select(table_name, columns_selected, where_clausule) #retorna query SELECTa ser executada para retorno dos nomes das tabelas existentes no schema/banco de dados
    df_tables = pd.read_sql(query, con=connection) #executa query e retona os dados do banco de dados em formato DataFrame
    return df_tables #retorna um DataFrame com os nomes das tabelas existentes no schema/banco de dados

#função que gera scripts SQL provindos do banco de dados e os salva em um arquivo
def generate_file_whit_db_scripts(file_path, open_file_mode, connection, where_clausule, new_values, table_schema, table, value, erros):
    file = open(file_path, open_file_mode) #cria/abre o arquivo com determinado formato de leiturta/escrita
    df = replace_values_in_df_db(connection, table, where_clausule, new_values, value, erros) #substitui carcateres indesejados nos dados retornados
    data = gquery.generate_db_scripts(table_schema, table, df) #gera os scripts SQL com dados provindos do banco de dados
    file.write(data) #escreve os dados em um arquivo 
    file.close() #fecha o arquivo

#função que substitui valores nulos e converte colunas em tipo numérico
def convert_columns_to_numeric(df, value, erros):
    df = df.fillna(value) #substitui valores nan em zero
    df = df.apply(pd.to_numeric, errors=erros) #converte, se possível, as colunas do DataFrame em tipo numérico
    return df #retorno DataFrame

#função que substitui valores passados no DataFrame
def replace_values_in_df_db(connection, table, where_clausule, new_values, value, erros):
    query = gquery.query_create_select(table, '*', where_clausule) #cria uma query do tipo SELECT
    df = pd.read_sql_query(query, connection) #através da query busca informações no schema/banco de dados
    for key, value in new_values.items(): #lê um dicionário contendo chaves e valors com valores a serem susbtituídos
        df.replace(key, value, inplace=True) #substitui os valores e atualiza os valores do DataFrame
    df = convert_columns_to_numeric(df, value, erros) #converte, se possível, as colunas do DataFrame em tipo numérico
    return df #retorno DataFrame

#função que gera um DataFrame com base em tabelas do schema/banco de dados
def generate_df_db(connection, table_schema, join_column, value, erros, reference_column):
    df_tables_names = return_db_tables_name(connection, table_schema) #função que retorna o nome das tabelas do banco de dados
    df = pd.DataFrame() #cria um DataFrame vazio
    for table in df_tables_names['TABLE_NAME']: #lê o nome de uma tabela no DataFrame que tem todos os nomes de tabelas do schema/banco de dados
        table = f'{table_schema}.{table}' #adiciona o nome do schema/banco de dados no nome da tabela
        query = gquery.query_create_select(table, '*', None) #cria query select
        if df.empty: #se DataFrame vazio
            df = convert_sql_to_dataframe(query, connection) #busca dados do banco de dados e os converte em um DataFrame
        else:        
            df_table = convert_sql_to_dataframe(query, connection) #busca dados do banco de dados e os converte em um DataFrame
            df = pd.merge(df, df_table, how='outer', on=join_column, suffixes=('', '_remove')) #une o DataFrame existente com o DataFrame com os dados da última tabela buscada
            df.drop([i for i in df.columns if 'remove' in i], axis=1, inplace=True) #remove do DataFrame as colunas duplicadas
    df = convert_columns_to_numeric(df, value, erros) #substitui valores nulos e converte colunas em tipo numérico
    df = df.drop_duplicates(subset=reference_column, keep='first') #elimina do Pandas DataFrame os registros duplicados
    return df, df_tables_names #retorna DataFrame contendo os dados do banco e outro DataFrame com os nomes das tabelas do schema/banco de dados