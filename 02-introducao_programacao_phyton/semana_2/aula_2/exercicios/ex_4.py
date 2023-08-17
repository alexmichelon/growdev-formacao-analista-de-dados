'''
4) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando
dados sobre o salário e número de filhos. A prefeitura deseja saber:
    a) média do salário da população;
    b) média do número de filhos;
    c) maior salário;
    d) percentual de pessoas com salário até R$2000,00.
Escreva um programa que receba as informações necessárias de 5 pessoas
conforme a descrição e responda às questões a, b, c e d anteriores.
'''

import functions_utils as func

print('\nBem vindo ao sistema da prefeitura sobre salários e filhos\n')

average_salary = 0
average_number_of_sons = 0
bigger_salary = 0
salary_below_two_hundred = 0
amount_people = 5

for i in range (amount_people):
    salary = func.validate_float_positive('Informe o valor de seu salário: ')
    number_of_sons = func.validate_integer_positive('Informe quantos filhos você tem: ')

    average_salary += salary

    average_number_of_sons += number_of_sons
    
    if(salary > bigger_salary):
        bigger_salary = salary
    
    if(salary <= 2000):
       salary_below_two_hundred += 1

if(average_salary == 0):
    print('\nAs pessoas informadas disseram não possuir salário.')
else: 
    average_salary =(average_salary / amount_people)
    print(f'\nMédia salarial: R$ {average_salary:.2f}.')

if(average_number_of_sons == 0):
    print('As pessoas informadas disseram não possuir filhos.')
else:
    average_number_of_sons = (average_number_of_sons / amount_people) 
    print(f'Média de {average_number_of_sons} filhos por pessoa informada.')

if(average_salary > 0):
    print(f'Maior salário encontrado: R$ {bigger_salary:.2f}.')

if(salary_below_two_hundred > 0):
    salary_below_two_hundred = (salary_below_two_hundred * 100) / amount_people
    print(f'Percentual de pessoas com salário menor ou igual a R$ 2.000,00 é de {salary_below_two_hundred}%')
else:
    print(f'Não há pessoas com salário menor ou igual a R$ 2.000,00.')