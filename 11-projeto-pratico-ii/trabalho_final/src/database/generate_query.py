#função que define tipo de banco de dados dado um tipo de dado de um DataFrame
def generate_db_type(df_column_type):
    if df_column_type == 'float64':
        db_column_type = 'float'
    elif df_column_type == 'int32':
        db_column_type = 'smallint'
    elif df_column_type == 'int64':
        db_column_type = 'int'
    elif df_column_type == 'object':
        db_column_type = 'varchar(255)'
    elif df_column_type == 'str':
        db_column_type = 'varchar(255)'
    return db_column_type

#função que cria uma instrução SQL do tipo CREATE TABLE
def query_create_table(table_schema, table_name, columns, columns_type):
    query = f'CREATE TABLE {table_schema}.{table_name} ('
    for column, column_type in zip(columns, columns_type):
        column_type = generate_db_type(column_type)
        query += f'{column} {column_type}, '
    query = query[:-2] + ');\n'
    return query

#função que cria uma instrução SQL do tipo SELECT
def query_create_select(table_name, columns_selected, where_clausule):
    if where_clausule == None:
        query = f'SELECT {columns_selected} FROM {table_name};'
    else:
        query = f'SELECT {columns_selected} FROM {table_name} WHERE {where_clausule};'    
    return query    

#função que cria uma instrução SQL do tipo insert
def query_create_insert(table_schema, table_name, columns, values):
    query = f'INSERT INTO {table_schema}.{table_name} ({columns}) VALUES ({values});\n'    
    return query

#função que cria instruções SQL a partir de dados de um DataFrame
def generate_db_scripts(table_schema, table, df):    
    data = query_create_table(table_schema, table, df.columns, df.dtypes) #cria script CREATE TABLE
    #cria script INSERT
    columns = ''
    for column in df.columns:
        columns += f'{column}, '
    columns = columns[:-2]
    rows = df.values.tolist()
    for row in rows:       
        row = str(row).replace('[', '').replace(']', '')
        data += query_create_insert(table_schema, table, columns, row)
    return data