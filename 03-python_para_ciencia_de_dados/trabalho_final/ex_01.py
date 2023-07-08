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

from functions_utils import open_csv_file, convert_data_dict_list

list_keys = {'name': str, 'last_name': str, 'age': int, 'sex': str, 'purchase': float, 'year': int, 'payment': str}

header, data = open_csv_file('compras.csv', 'r')

people = convert_data_dict_list(data, list_keys)

number_person = 0
young = 0
adult = 0
older = 0

for p in people:
    if(p['age'] <= 25):
        young += 1
    elif(p['age'] >= 26) and (p['age'] <= 59):
        adult += 1
    else:
        older += 1
    number_person +=1

print(f'Há {young} jovens na base de dados.')
#print(f'Há {adult} adults na base de dados.')
#print(f'Há {older} idosos na base de dados.')