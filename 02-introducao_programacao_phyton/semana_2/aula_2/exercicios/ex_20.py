'''
20) Escreva um programa que leia um valor inicial A e uma razão R e imprima
uma sequência em P.G. contendo 10 valores.
'''

import functions_utils as func

amount_number = 10
pg_sequence = []

print("\nBem vindo ao sistema que calcula Progressão Geométrica!!!\n")

inicial_value = func.validate_integer_positive('Informe um valor inicial (A): ')
ratio = func.validate_integer_positive('Informe a razão (R): ')

pg_sequence.append(inicial_value)

for i in range(1, amount_number):
    pg_sequence.append(pg_sequence[i-1] * ratio)

for x in range(len(pg_sequence)):
    print(pg_sequence[x])

print(*pg_sequence, sep=", ")