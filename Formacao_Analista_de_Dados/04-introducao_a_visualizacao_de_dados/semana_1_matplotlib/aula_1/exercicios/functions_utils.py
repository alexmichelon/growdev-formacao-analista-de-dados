#converte valor float em moeda (Brasil)
def convert_to_currency(value):
    x = "{:,.2f}".format(float(value))
    y = x.replace(',','x')
    z = y.replace('.',',')
    return z.replace('x','.')

#abrir arquivo csv
def open_csv_file(file_path, mode_file):
    file = open(file_path, mode_file)
    content = file.readlines()
    header = content[0]
    data = content[1:]
    return header, data

#converte dados em uma lista de dicionários passando como parâmetro os campos e tipos dos campos da tabela
def convert_data_dict_list(data, dict_keys):
    list = []
  
    for d in data:      
        record = d.split(',')
        line = {}
        position = 0
        for key, value in dict_keys.items():
            if(value == str):
                line.setdefault(key, value(record[position]).replace('\n',''))
            elif(value == bool):
                if(record[position][0].upper() in ('T', 'V', '1') ):
                    line.setdefault(key, True)
                else:
                    line.setdefault(key, False)
            else:    
                line.setdefault(key, value(record[position]))
            position += 1
        list.append(line)   
    return list

#agrupa valores de uma lista de dicionários em um dicionário utilizando duas chaves 
def list_dict_group_by_values_two_keys(dictionary_grouped, dictionary, key_group, key_sum):
    dictionary_grouped[dictionary[key_group]] =  dictionary_grouped.get(dictionary[key_group], 0) + dictionary[key_sum]
    return dictionary_grouped

#conta número de ocorrências de valores de uma chave em uma lista de dicionários
def list_dict_count_values_key(dictionary_grouped, dictionary, key_group):
    dictionary_grouped[dictionary[key_group]] =  dictionary_grouped.get(dictionary[key_group], 0) + 1
    return dictionary_grouped

def sum_column_values_whitout_conditions(list_dict, key):
    column_values = 0
    for dict in list_dict:
        column_values += dict[key]
    return column_values
