'''
13)Faça um programa que leia um valor N e mostre os N termos da Série a
seguir:
a) S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m
'''

import functions_utils as func

print('\nBem vindo ao sistema N termos de série!\n')

number = func.validate_integer_positive('Informe o número até o qual será calculado a série (N):\n')

n_text = 'N = '
x = 1

for i in range(number):    
    n_text = n_text + str(i + 1) + '/' + str(x)   
    if(i < number-1):
        n_text = n_text + ' + '
    x += 2
    
print(f'{n_text}\n')