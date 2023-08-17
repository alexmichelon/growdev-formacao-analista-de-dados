'''
18) Desenvolver um programa que leia um número não determinado de valores
e calcule e escreva a média aritmética dos valores lidos, a quantidade de
valores positivos, a quantidade de valores negativos e o percentual de
valores negativos e positivos.
'''

import functions_utils as func

amount_numbers = 0
sum_numbers = 0
amount_positive_numbers = 0
amount_negative_numbers = 0
percentual_positive_numbers = 0
percentual_negative_numbers = 0

option = 'S'

print('\nBem vindo ao sistema Informa dados de valores informados!!!!\n')

while(option != 'N'):
    number = func.validate_float_negative('Informe um número: ')
    amount_numbers += 1
    sum_numbers += number
    if(number > 0):
        amount_positive_numbers += 1
    else:
        amount_negative_numbers += 1    
    option = func.validate_option('Deseja Continuar? S/N ','"S","N","s","n"') .upper()

average = (sum_numbers / amount_numbers)
print(f'\nA média aritmética dos valores lidos é: {average:.2f}.')

print(f'Foram informados {amount_positive_numbers} número(s) positivo(s).')

print(f'Foram informados {amount_negative_numbers} número(s) negativos(s).')

percentual_positive_numbers = (amount_positive_numbers * 100) / amount_numbers
print(f'O percentual de número positivos informados foi de {percentual_positive_numbers:.2f}%.')

percentual_negative_numbers = (amount_negative_numbers * 100) / amount_numbers
print(f'O percentual de número negativos informados foi de {percentual_negative_numbers:.2f}%.')