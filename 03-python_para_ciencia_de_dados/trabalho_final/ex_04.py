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

from functions_utils import open_csv_file, convert_to_currency, convert_data_dict_list, list_dict_group_by_values_two_keys

list_keys = {'name': str, 'last_name': str, 'age': int, 'sex': str, 'purchase': float, 'year': int, 'payment': str}

header, data = open_csv_file('compras.csv', 'r')

people = convert_data_dict_list(data, list_keys)

purchases_women = {}
total_purcheses_women = ''

for person in people:
    if(person['sex'] == 'M') and (person['year'] == 2014):
        purchases_women = list_dict_group_by_values_two_keys(purchases_women, person, 'sex', 'purchase')

total_purcheses_women = convert_to_currency(purchases_women[max(purchases_women, key=purchases_women.get)])

print(f'No ano de 2014, a soma total de compras feitas por mulheres foi de R$ {total_purcheses_women}')
