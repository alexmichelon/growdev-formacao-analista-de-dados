from flask import render_template, request
import pandas as pd

db = 'tabela-fipe-historico-precos.csv'  
df = pd.read_csv(db)
amount_records_load_display = 25000

def fix_columns_name():
    for i in range (len(df.columns)):
        df.columns.values[i] = ''.join(filter(str.isalnum, df.columns.values[i])) 
    return df

df = fix_columns_name() 

def index():                      
    return render_template('index.html', name_database=db)

def search_numeric_columns():
    num_cols = []
    numerics = ["int16", 'int32', 'int64', 'float16', 'float32', "float64"]
    df_numeric = df.select_dtypes(include=numerics)
    for column in df_numeric:
        num_cols.append(column)
    return num_cols

def build_search_text(search_text, i, columns, comparisions, data_search):
    if (comparisions[i] == '=='):
        search_text = f'("{columns[i]}" Igual {data_search[i]})'
    elif (comparisions[i] == '!='):
        search_text = f'("{columns[i]}" Diferente {data_search[i]})'
    elif (comparisions[i] == '>'):
        search_text = f'("{columns[i]}" Igual {data_search[i]})'
    elif (comparisions[i] == '>='):
        search_text = f'("{columns[i]}" Maior ou Igual {data_search[i]})'
    elif (comparisions[i] == '<'):
        search_text = f'("{columns[i]}" Menor {data_search[i]})'
    elif (comparisions[i] == '<='):
        search_text = f'("{columns[i]}" Menor ou Igual {data_search[i]})'
    elif (comparisions[i] == 'contains'):
        search_text = f'("{columns[i]}" Contém {data_search[i]})'
    else:
        search_text = f'("{columns[i]}" Não contém {data_search[i]})'
    return search_text

def search_data():    
    query = ''
    search_text = ''
    columns = request.form.getlist('columns[]')
    comparisions = request.form.getlist('comparisions[]')
    data_search = request.form.getlist('data_search[]')        
    for i in range (len(columns)):
        if i != 0:    
            query += ' and '
            search_text += ' e '
            
        if (not data_search[i].isdigit()):
            data_search[i] = f'"{data_search[i]}"'
            
        if (comparisions[i] == 'contains'):
            query += f'({columns[i]}.str.{comparisions[i]}({data_search[i]}))'
        elif (comparisions[i] == 'not_contains'):
            query += f'({columns[i]}.str.contains({data_search[i]}) == {False})'
        else:
            query += f'({columns[i]} {comparisions[i]} {data_search[i]})'        
        
        search_text += build_search_text(search_text, i, columns, comparisions, data_search)            
        
    if len(query) > 0:
        df_query = df.query(query)
    else:
        df_query = df
    return render_template('database_form_search.html', database=df_query, query=search_text, amount_records_load_display=amount_records_load_display)  



def generate_group_by_command(df_query):
    query_text = ''
    fields_text = ''
    field_value_type = ''
    columns_group_by = request.form.getlist('columns_group_by[]')
    column_value_type = request.form.getlist('column_value_type')
    value_type = request.form.getlist('value_type')
    check_sum = request.form.get('sum')
    if len(columns_group_by) != 0:
        if check_sum:
            campo_somar = 'Marcado'            
            if 'mean()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].sum().mean().round(6).reset_index()
                field_value_type = 'Média'
            elif 'max()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].sum().max().round(2).reset_index()
                field_value_type = 'Valor Máximo'
            elif 'idxmax()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].sum().idxmax().reset_index()
                field_value_type = 'Índice Valor Máximo'
            elif 'min()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].sum().min().round(2).reset_index()
                field_value_type = 'Desvio Padrão'
            elif 'idxmin()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].sum().idxmin().reset_index()
                field_value_type = 'Índice Valor Mínimo'
            elif 'std()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].sum().std().round(6).reset_index()
                field_value_type = 'Desvio Padrão'
            else:
                df_query = df_query.groupby(columns_group_by)[column_value_type].sum().round(2)
            query_text = f'DataFrame.groupby({columns_group_by}){column_value_type}.sum().{str( value_type).replace("[", "").replace("]", "")}.reset_index()'
        else:
            campo_somar = 'Desmarcado'
            if 'mean()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].mean().round(6).reset_index()
                field_value_type = 'Média'
            elif 'max()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].max().round(2).reset_index()
                field_value_type = 'Valor Máximo'
            elif 'idxmax()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].idxmax().reset_index()
                field_value_type = 'Índice Valor Máximo'
            elif 'min()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].min().round(2).reset_index()
                field_value_type = 'Valor Mínimo'
            elif 'idxmin()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].idxmin().reset_index()
                field_value_type = 'Índice Valor Mínimo'
            elif 'std()' in value_type:
                df_query = df_query.groupby(columns_group_by)[column_value_type].std().round(6).reset_index()
                field_value_type = 'Desvio Padrão'
            else:
                df_query = df_query.groupby(columns_group_by)[column_value_type]
            query_text = f'DataFrame.groupby({columns_group_by}){column_value_type}.{str(value_type).replace("[", "").replace("]", "")}.reset_index()'
         
        fields_text = f'Agrupador: {columns_group_by}, Numérico: {column_value_type}, Dado: {field_value_type}, Somar: {campo_somar}'

    return df_query, query_text, fields_text

def group_by_data():
    query_text = ''
    fields_text = ''
    df_query = df          
    df_query, query_text, fields_text = generate_group_by_command(df_query)  
    if(type(df_query) != type(df)):
        df_query = df_query.to_frame()
    numeric_columns = search_numeric_columns()         
    return render_template('database_form_group_by.html', database=df, database_grouped=df_query, numeric_columns=numeric_columns, query_text=query_text, fields_text=fields_text, amount_records_load_display=amount_records_load_display)  


def search_group_by_data():
    df_query = df    
    query = ''    
    search_text = ''
    
    #--
    columns = request.form.getlist('columns[]')
    comparisions = request.form.getlist('comparisions[]')
    data_search = request.form.getlist('data_search[]')        
    for i in range (len(columns)):
        if i != 0:    
            query += ' and '
            search_text += ' e '
            
        if (not data_search[i].isdigit()):
            data_search[i] = f'"{data_search[i]}"'
            
        if (comparisions[i] == 'contains'):
            query += f'({columns[i]}.str.{comparisions[i]}({data_search[i]}))'
        elif (comparisions[i] == 'not_contains'):
            query += f'({columns[i]}.str.contains({data_search[i]}) == {False})'
        else:
            query += f'({columns[i]} {comparisions[i]} {data_search[i]})'        
        search_text += build_search_text(search_text, i, columns, comparisions, data_search)            
    if len(query) > 0:
        df_query = df.query(query)
    else:
        df_query = df
    #--
        
    query_text = ''
    fields_text = ''         
    df_query, query_text, fields_text = generate_group_by_command(df_query)  
    if(type(df_query) != type(df)):
        df_query = df_query.to_frame()
    numeric_columns = search_numeric_columns() 
     
    return render_template('database_form_search_group_by.html', database=df, database_grouped=df_query, numeric_columns=numeric_columns, query=search_text, query_text=query_text, fields_text=fields_text, amount_records_load_display=amount_records_load_display)  


def describe_info():
    df_describe = df.describe().reset_index()
    data = {}
    for index in df.columns:
        data[index] = [df[index].dtype, df[index].isnull().sum()]   
    df_columns_types = pd.DataFrame(data, columns=df.columns.values.tolist())
    df_columns_types.insert(0, "Dado", ["Tipo", "Qtd Nulos"], True)
    return render_template('database_describe_info.html', database=df, df_describe=df_describe, name_database=db, df_columns_types=df_columns_types)  