'''1) Escreva um programa em Python para receber o nome, a idade e a
altura de 5 pessoas. Informe ao final qual é o nome da pessoa que
tem a maior idade e a menor altura, além da média de idade das 5
pessoas.'''

import functions_utils as func

age_average = 0
max_persons = 5
persons = []
oldest_age = 0
lowest_height = 0.0


print('\nBem vindo ao sistema informações de pessoas!\n')

for i in range (0, max_persons, 1):
    person_name = input('\nInforme o nome da pessoa: ')
    person_age = func.validate_integer_positive('Informe a idade da pessoa: ')
    person_height = func.validate_float_positive('Informe a altura da pessoa: ')

    if(i == 0):
       oldest_age = person_age
       lowest_height =  person_height
       oldest_person_name = person_name
       lowest_person_name = person_name
    else: 
        if(person_age > oldest_age):
            oldest_person_name = person_name
            oldest_age = person_age
        if(person_height < lowest_height):
            lowest_person_name = person_name
            lowest_height = person_height
    age_average += person_age

age_average = age_average / max_persons    


print(f'\n\nA pessoa mais velha é: {oldest_person_name} com {oldest_age} anos de idade.')
print(f'A pessoa de menor altura é: {lowest_person_name} com {lowest_height} m.')
print(f'A média de idade das pessoas informadas é {age_average} anos de idade.')