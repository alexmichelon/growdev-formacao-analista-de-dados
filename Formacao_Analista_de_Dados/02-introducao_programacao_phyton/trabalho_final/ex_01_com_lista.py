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
    persons.append([])
    
    person_name = input('\nInforme o nome da pessoa: ')
    person_age = func.validate_integer_positive('Informe a idade da pessoa: ')
    person_height = func.validate_float_positive('Informe a altura da pessoa: ')
    
    persons[i].append(person_name)
    persons[i].append(int(person_age))
    persons[i].append(float(person_height))

#comparações dentro da lista "persons"
for i in range (0, max_persons, 1):
    #verifica se a pessoa checada no momento tem a maior idade até então
    if(persons[i][1] > oldest_age):
        oldest_person_name = persons[i][0]
        oldest_age = persons[i][1]
    #atribui a primeira altura como a mais baixa pois lowest_height inicia de zero
    if(lowest_height == 0):
        lowest_person_name = persons[i][0]
        lowest_height = persons[i][2]
    #verifica se a altura lida neste momento é mais baixa que a mais baixa encontrada até então
    elif(persons[i][2] < lowest_height):
        lowest_person_name = persons[i][0]
        lowest_height = persons[i][2]
    #soma as idade lidas a cada iteração
    average += persons[i][1]
#após sair do laço, divide o somatório das idades pelo númerod e pessoas informadas
average = average / max_persons


'''
#usando função lambda
oldest_person_name, oldest_age, height = max(persons, key=lambda item: item[1])
lowest_person_name, age, lowest_height = min(persons, key=lambda item: item[2])
#compreensão de lista
average = sum([age[1] for age in persons])/len(persons)
'''

print('\nResultado:')
print(f'A pessoa mais velha é {oldest_person_name} com {oldest_age} anos de idade.')
print(f'A pessoa de menor altura é {lowest_person_name} com {lowest_height} m.')
print(f'A média de idade das pessoas informadas é {average} anos de idade.')