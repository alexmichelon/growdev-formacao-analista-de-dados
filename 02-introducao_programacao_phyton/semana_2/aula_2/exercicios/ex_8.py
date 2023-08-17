'''
8) Escreva um programa que leia a idade e salário de 10 pessoas. Informe em
seguida:
    a) Qual é a média de idade entre as pessoas?
    b) Quantas pessoas há por faixa etária, considerando:
        i) jovens < 18
        ii) 18 <= adultos < 60
        iii) idosos >= 60
    c) Em seguida, mostre qual é a faixa etária que acumula o maior salário.
'''
import functions_utils as func

amount_people = 5

average_age = 0
amount_young_people = 0
amount_adult = 0
amount_elderly = 0
salary_young_people = 0
salary_adult = 0
salary_elderly = 0


print('\nBem vindo ao sistema Pessoas, Faixa Etária e Salários!!!\n')

for i in range (amount_people):
    age = func.validate_integer_positive('Informe a idade da pessoa: ')
    salary = func.validate_float_positive('Informe  o valor do salário da pessoa: R$ ')

    average_age += age

    if(age < 18):
        amount_young_people += 1
        salary_young_people += salary
    elif(age >= 18) and (age < 60):
        amount_adult += 1
        salary_adult += salary
    else:
        amount_elderly += 1
        salary_elderly += 1

age_group = [salary_young_people, salary_adult, salary_elderly]

if(age_group.index(max(age_group)) == 0):
    high_salary = 'Jovens'
elif(age_group.index(max(age_group)) == 1):
    high_salary = 'Adultos'
else:
    high_salary = 'Idosos'

average_age = average_age / amount_people
print(f'\nA média de idade entre as pessoas é de : {average_age} anos de idade.')

print('\nPessoas por faixa etária: '
      f'Jovens: {amount_young_people}, '
      f'Adultos: {amount_adult}, '
      f'Idosos: {amount_elderly}\n')

print(f'A faixa etária com maior salário é: {high_salary}.')