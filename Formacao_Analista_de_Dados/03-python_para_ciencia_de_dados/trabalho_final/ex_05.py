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

from functions_utils import open_csv_file, convert_data_dict_list, convert_to_currency

list_keys = {'name': str, 'last_name': str, 'age': int, 'sex': str, 'purchase': float, 'year': int, 'payment': str}

header, data = open_csv_file('compras.csv', 'r')

people = convert_data_dict_list(data, list_keys)

purchases_young = 0
purchases_adult = 0
purchases_older = 0
purchases_total = 0
value = ''

for person in people:
    if(person['age'] <= 25):
        purchases_young += person['purchase']
    elif(person['age'] >= 26) and (person['age'] <= 59):
        purchases_adult += person['purchase']
    else:
        purchases_older += person['purchase']
    purchases_total += person['purchase']

value = convert_to_currency(purchases_total)
print(f'\n-----\nGastos totais R$ {value}.\n----')
value = convert_to_currency(purchases_young)
print(f'Gastos de jovens R$ {value}.')
value = convert_to_currency(purchases_adult)
print(f'Gastos de adultos R$ {value}.')
value = convert_to_currency(purchases_older)
print(f'Gastos de idosos R$ {value}.')


count_young = 0
count_adult = 0
count_older = 0
average_young = 0
average_adult = 0
average_older = 0
total_young = 0
total_adult = 0
total_older = 0
total_person = 0

for person in people:
    if(person['age'] <= 25):
        count_young += 1
        total_young += person['purchase']
    elif(person['age'] >= 26) and (person['age'] <= 59):
        count_adult += 1
        total_adult += person['purchase']
    else:
        count_older += 1
        total_older += person['purchase']
    total_person += 1

print(f'\n----\nTotal de jovens: {count_young}, Gastos totais jovens: R$ {convert_to_currency(total_young)}, média jovens: R$ {convert_to_currency(total_young/count_young)}')
print(f'Total de adultos: {count_adult}, Gastos totais adultos: R$ {convert_to_currency(total_adult)}, média adultos: R$ {convert_to_currency(total_adult/count_adult)}')
print(f'Total de idosos: {count_older}, Gastos totais idosos: R$ {convert_to_currency(total_older)}, , média idosos: R$ {convert_to_currency(total_older/count_older)}')

print(f'\n-----\nOs consumidores na faixa etária dos adultos (26 a 59 anos)'
      'possuem disparadamente o posto de quem mais gastou dentre as demais faixas etárias em todos os anos.'
      'As médias de consumo por faixa etária são próximas mas o que sobressai é'
      f'que a grande maioria dos consumidores são adultos ({(count_adult * 100) / total_person:.2f}%), fazendo com que '
      'o gasto total seja amplamente maior nesta faixa etária.')