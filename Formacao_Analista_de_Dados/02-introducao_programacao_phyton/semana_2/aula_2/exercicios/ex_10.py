'''
10)Escreva um programa que recebe 10 valores e imprima o somatório dos
elementos.
'''

import functions_utils as func

amount_numbers = 10
sum = 0
print('\nBem vindo ao sistema recebe 10 números e imprime somatório\n')

for i in range(amount_numbers):
    numero = func.validate_float_negative('Informe o número: ')
    sum += numero

print(f'O somatório dos números informados é: {sum:.2f}.')