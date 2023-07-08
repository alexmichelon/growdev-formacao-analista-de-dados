'''
2) Escrever um programa que lê um valor N inteiro e positivo e que calcula seu
valor fatorial. Ex: 5! = 5 * 4 * 3 * 2 * 1
'''

import functions_utils as func

factorial_result = 0

print('\nBem vindo ao cálculo de fatorial!\n')

number = func.validate_integer_positive('Informe o número o qual deseja calcular o fatorial:\n')
#factorial_result = func.factorial_calculate_begin_number_informed(number)
factorial_result = func.factorial_calculate_begin_1(number)

print(f'O resultado de {number}! é {factorial_result}.')