'''4) Escreva um programa em Python que receba a idade e o peso de 10
pessoas e informe se a média de peso é maior entre pessoas
menores de idade ou maiores de idade.'''

import functions_utils as func

people = []
max_options = 10
legal_age_weight = 0
minor_age_weight = 0
amount_legal_age = 0
amount_minor_age = 0
position_age = 0
position_weight = 1

print('\nBem vindo ao Sistema Média de Pesos Por faixa de idade!\n')

for i in range(max_options):
    people.append([])
    for j in range(1,2):
        age = func.validate_integer_positive('\nInforme a idade da pessoa: ')
        weight = func.validate_float_positive('Informe o peso da pessoa: ')

        people[i].append(age)
        people[i].append(weight)

for i in range(max_options):
    if(people[i][position_age] >= 18):
        legal_age_weight += people[i][position_weight]
        amount_legal_age += 1
    else:
        minor_age_weight += people[i][position_weight]
        amount_minor_age += 1

if(amount_legal_age > 0):
    legal_age_weight = legal_age_weight / amount_legal_age
if(amount_minor_age > 0):
    minor_age_weight = minor_age_weight / amount_minor_age

if(legal_age_weight > minor_age_weight):
    print(f'\nA média de peso das pessoas maiores de idade ({legal_age_weight:.2f}kg) é superior a média de peso das pessoas menores idade ({minor_age_weight:.2f}kg).')
elif(legal_age_weight < minor_age_weight): 
    print(f'\nA média de peso das pessoas menores de idade ({minor_age_weight:.2f}kg) é superior a média de peso das pessoas maiores idade ({legal_age_weight:.2f}kg).')
else:
    print(f'\nA média de peso das pessoas maiores de idade ({legal_age_weight:.2f}) e a média de peso da pessoas menores de idade ({minor_age_weight}kg) são iguais.')