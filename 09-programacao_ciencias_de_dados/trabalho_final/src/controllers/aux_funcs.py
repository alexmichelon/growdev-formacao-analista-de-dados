def fix_columns_name(df):
    for i in range (len(df.columns)):
        if df.columns.values[i].find('Unnamed: ') != -1:
            df.columns.values[i] = f'column_{i}'
        else:
            for c in "#@&$.%+*/!|=:; ":
                df.columns.values[i] = df.columns.values[i].replace(c, '')
    return df

def search_numeric_columns(df):
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


def generate_group_by_command(df_query, request):
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