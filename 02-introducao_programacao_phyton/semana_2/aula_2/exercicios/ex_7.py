'''
7) Escreva um programa que leia 10 valores e encontre o maior e o menor deles.
Mostre o resultado.
'''

import functions_utils as func

print('\nBem vindo ao sistema maior e menor valor informado!!!!\n')

bigger_value = 0
smaller_value = 0

for i in range(10):
    value = func.validate_float_negative('Informe um número: ')
    if(i == 0):
        bigger_value = value
        smaller_value = value
    else:
        if(value > bigger_value):
            bigger_value = value
        if(value < smaller_value):
            smaller_value = value

print(f'\nMaior valor informado: {bigger_value:.2f}\n'
      f'Menor valor informado: {smaller_value:.2f}\n')
