'''
9) Escreva um programa que receba o nome de 10 pessoas e para cada pessoa,
o lugar para o qual ela já viajou. Sendo que existem 3 possibilidades: 
    a) Rio de Janeiro
    b) Bahia
    c) Minas Gerais
Após, informar qual foi o destino mais visitado e qual o menos visitado.
'''

import functions_utils as func

amount_people = 5
#contador de visitas Rio de Janeiro
destiny_1 = 0
#contador de visitas Bahia
destiny_2 = 0
#contador de visitas Minas Gerais
destiny_3 = 0

most_visited = ''
less_visited = ''

print('\nBem vindo ao sistema Destino Mais Visitado!!!\n')

for i in range (amount_people):
    #name = input('Informe o nome da pessoa: ')
    destiny = func.validate_integer_positive_comparision('Informe o local visitado:\n'
                                                         '1 - Rio de Janeiro\n'
                                                         '2 - Bahia\n'
                                                         '3 - Minas Gerais\n', '"1","2","3"')

    if(destiny == '1'):
        destiny_1 += 1 
    elif(destiny == '2'):
        destiny_2 += 1
    else:
        destiny_3 += 1

destinations = [destiny_1, destiny_2, destiny_3]


if(destinations.index(max(destinations)) == 0):
    most_visited = 'Rio de Janeiro'
elif(destinations.index(max(destinations)) == 1):
    most_visited = 'Bahia'
else:
    most_visited = 'Minas Gerais'

if(destinations.index(min(destinations)) == 0):
    less_visited = 'Rio de Janeiro'
elif(destinations.index(min(destinations)) == 1):
    less_visited = 'Bahia'
else:
    less_visited = 'Minas Gerais'

print(f'A cidade mais visitada foi é: {most_visited}.')
print(f'A cidade menos visitada foi é: {less_visited}.')
print(destinations.index(max(destinations)))
print(destinations.index(min(destinations)))