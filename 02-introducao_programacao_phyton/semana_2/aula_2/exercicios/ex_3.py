'''
3) Escrever um programa que lê um valor N inteiro e positivo e que calcula e
escreve o valor de E.
E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + … + 1 / N!
'''

import functions_utils as func

print('\nBem vindo ao cálculo de frações com fatorial (E)!\n')

number = func.validate_integer_positive('Informe o número o qual deseja calcular o fatorial com fração (E):\n')

e_text = '1'
e = 1

for i in range(number):
    e_text = e_text + ' + 1 / '+ str(i+1) +'!'
    e += (1/func.factorial_calculate_while(i+1))
    
print(f'E= {e_text}: {e:.4f}\n')