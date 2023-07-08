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

people_group_by_men = {}
people_group_by_women = {}
count_men = 0
count_women = 0

#acessa a lista de dicionários "people" em cada dicionário "person"
for person in people:
    #verifica se a linha "person" é homem (sex == "M")
    if (person['sex'] == 'M'):
        #cria um dicionário "people_group_by_men" com chave "sex" e valor com a soma dos registros do tipo "M"
        people_group_by_men = list_dict_count_values_key(people_group_by_men, person, 'sex')
    else:
        #cria um dicionário "people_group_by_women" com chave "sex" e valor com a soma dos registros diferentes do tipo "M"
        people_group_by_women = list_dict_count_values_key(people_group_by_women, person, 'sex')

#atribui o valor do dicionário "people_group_by_men" para o contador do número de homens "count_men"
count_men = people_group_by_men[max(people_group_by_men, key=people_group_by_men.get)]
#atribui o valor do dicionário "people_group_by_women" para o contador do número de mulheres "count_women"
count_women = people_group_by_women[max(people_group_by_women, key=people_group_by_women.get)]

print(f'Há {count_men} homens na base de dados.')
print(f'Há {count_women} mulheres na base de dados.')