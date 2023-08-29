from flask import render_template, request
import controllers.aux_funcs as aux
import pandas as pd

db = 'vgsales.csv'  

df = pd.read_csv(db)

#número máximo de dados a serem carregados na página
amount_records_load_display = 2500

df = aux.fix_columns_name(df) 

def index():                      
    return render_template('index.html', name_database=db)

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
        
        search_text += aux.build_search_text(search_text, i, columns, comparisions, data_search)            
        
    if len(query) > 0:
        df_query = df.query(query)
    else:
        df_query = df
    return render_template('database_form_search.html', database=df_query, query=search_text, amount_records_load_display=amount_records_load_display)  


def group_by_data():
    query_text = ''
    fields_text = ''
    df_query = df          
    df_query, query_text, fields_text = aux.generate_group_by_command(df_query, request)  
    if(type(df_query) != type(df)):
        df_query = df_query.to_frame()
    numeric_columns = aux.search_numeric_columns(df)         
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
        search_text += aux.build_search_text(search_text, i, columns, comparisions, data_search)            
    if len(query) > 0:
        df_query = df.query(query)
    else:
        df_query = df
    #--
        
    query_text = ''
    fields_text = ''         
    df_query, query_text, fields_text = aux.generate_group_by_command(df_query, request)  
    if(type(df_query) != type(df)):
        df_query = df_query.to_frame()
    numeric_columns = aux.search_numeric_columns(df) 
     
    return render_template('database_form_search_group_by.html', database=df, database_grouped=df_query, numeric_columns=numeric_columns, query=search_text, query_text=query_text, fields_text=fields_text, amount_records_load_display=amount_records_load_display)  


def describe_info():
    df_describe = df.describe().reset_index()
    data = {}
    for index in df.columns:
        data[index] = [df[index].dtype, df[index].isnull().sum()]   
    df_columns_types = pd.DataFrame(data, columns=df.columns.values.tolist())
    df_columns_types.insert(0, "Dado", ["Tipo", "Qtd Nulos"], True)
    return render_template('database_describe_info.html', database=df, df_describe=df_describe, name_database=db, df_columns_types=df_columns_types)  