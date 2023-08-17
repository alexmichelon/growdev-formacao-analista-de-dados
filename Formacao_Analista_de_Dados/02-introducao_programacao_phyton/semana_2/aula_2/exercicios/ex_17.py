'''
17) Crie um programa para que retorne o somatório de todos os números entre 1
e um valor fornecido pelo usuário. Por exemplo, se o usuário fornecer o
número 4, o computador deverá calcular o somatório 1+ 2 + 3 + 4 = 10.
'''

import functions_utils as func

sum = 0

print('\nBem vindo a soma de valores entre o número informado e 1\n')

number = func.validate_integer_positive('Informe um número: ')

for i in range (number):   
    sum += number
    number -= 1
    print(sum)

print(f'A soma dos números é: {sum}')