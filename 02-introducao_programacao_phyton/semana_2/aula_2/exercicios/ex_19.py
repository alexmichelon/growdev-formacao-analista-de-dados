'''
19) Escreva um programa que leia um valor inicial A e uma razão R e imprima
uma sequência em P.A. contendo 10 valores.
'''

import functions_utils as func

amount_number = 10
pa_sequence = []

print("\nBem vindo ao sistema que calcula Progressão Aritmética!!!\n")

inicial_value = func.validate_integer_positive('Informe um valor inicial (A): ')
ratio = func.validate_integer_positive('Informe a razão (R): ')

pa_sequence.append(inicial_value)

for i in range(1, amount_number):
    pa_sequence.append(pa_sequence[i-1] + ratio)

for x in range(len(pa_sequence)):
    print(pa_sequence[x])

print(*pa_sequence, sep=", ")

