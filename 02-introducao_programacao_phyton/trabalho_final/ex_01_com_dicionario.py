'''1) Escreva um programa em Python para receber o nome, a idade e a
altura de 5 pessoas. Informe ao final qual é o nome da pessoa que
tem a maior idade e a menor altura, além da média de idade das 5
pessoas.'''

import functions_utils as func

age_average = 0
max_persons = 5
persons = []
oldest_person_name = '' 
oldest_age = 0
lowest_person_name = ''
lowest_height = 0.0
average = 0.0

print('\nBem vindo ao sistema informações de pessoas!\n')

#preenche a lista de pessoas (persons) com informações informadas pelo usuário
for i in range(max_persons):
    
    person_name = input('\nInforme o nome da pessoa: ')
    person_age = func.validate_integer_positive('Informe a idade da pessoa: ')
    person_height = func.validate_float_positive('Informe a altura da pessoa: ')
    
    #adiciona as informações do usuário em formato didcionário dentro da lista persons
    persons.append({'name': person_name, 'age': int(person_age), 'height': float(person_height)})

#comparações dentro da lista "persons"
#person é um dicionário (uma posição) dentro da lista persons
for person in persons:
    #verifica se a pessoa checada no momento tem a maior idade até então
    if(person.get('age') > oldest_age):
        oldest_person_name = person.get('name')
        oldest_age = person.get('age')
    #atribui a primeira altura como a mais baixa pois lowest_height inicia de zero
    if(lowest_height == 0):
        lowest_person_name = person.get('name')
        lowest_height = person.get('height')
    #verifica se a altura lida neste momento é mais baixa que a mais baixa encontrada até então
    elif(float(person.get('height')) < lowest_height):
        lowest_person_name = person.get('name')
        lowest_height = person.get('height')
    #soma as idade lidas a cada iteração
    average += person.get('age')
#após sair do laço, divide o somatório das idades pelo número de pessoas informadas
average = average / max_persons

print('\nResultado:')
print(f'A pessoa mais velha é {oldest_person_name} com {oldest_age} anos de idade.')
print(f'A pessoa de menor altura é {lowest_person_name} com {lowest_height} m.')
print(f'A média de idade das pessoas informadas é {average} anos de idade.')