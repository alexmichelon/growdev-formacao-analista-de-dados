'''
Utilize as seguintes faixas etárias nos exercícios em que for necessário.
● Jovens, 18 a 25 anos
● Adultos, 26 a 59 anos
● Idosos, igual ou maior que 60 anos

Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
exercícios.

1) Utilizando as faixas etárias, diga quantas pessoas jovens há?
2) Quantos homens e mulheres existem na base de dados?
3) Quantas compras no crédito foram feitas em 2010?
4) Qual foi o valor total de compras realizadas por mulheres em 2014?
5) Quem gastou mais no total, jovens, adultos ou idosos? após avaliar
o resultado que você encontrou. Tem algum motivo para esse resultado?
'''

from functions_utils import open_csv_file, convert_data_dict_list, list_dict_count_values_key

list_keys = {'name': str, 'last_name': str, 'age': int, 'sex': str, 'purchase': float, 'year': int, 'payment': str}

header, data = open_csv_file('compras.csv', 'r')

people = convert_data_dict_list(data, list_keys)

purchases_group_by_2010 = {}
count_purchases_2010 = 0

#acessa a lista de dicionários "people" em cada linha "person"
for person in people:
    #verifica se a linha "person" é do ano de 2010 e pagamento no tipo credito
    if (person['year'] == 2010) and (person['payment'] == 'credito'):
        #cria um dicionário "purchases_group_by_2010" com chave "year" e valor com a soma dos registros do tipo "credito"
        purchases_group_by_2010 = list_dict_count_values_key(purchases_group_by_2010, person, 'year')

#atribui o valor do dicionário "purchases_group_by_2010" para o contador das compras feitas no credito no ano 2010 "count_purchases_2010"
count_purchases_2010 = purchases_group_by_2010[max(purchases_group_by_2010, key=purchases_group_by_2010.get)]

print(f'Foram feitas {count_purchases_2010} compras no crédito no ano de 2010.')
