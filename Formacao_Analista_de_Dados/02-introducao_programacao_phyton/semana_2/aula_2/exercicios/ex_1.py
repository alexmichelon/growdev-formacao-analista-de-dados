'''
1) Escrever um programa que lê 5 valores para a, um de cada vez, e conta
quantos destes valores são negativos, escrevendo esta informação.
'''

import functions_utils

print('\nBem vindo ao sistema Verifica Números negativos')

negative_amount = 0

for i in range(5):
    a = functions_utils.validate_float_negative('Informe o número: ')
    if(a < 0):
        negative_amount = negative_amount + 1

print(f'\nForam informados {negative_amount} número(s) negativo(s).')