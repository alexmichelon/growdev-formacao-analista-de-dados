'''
12) A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

import functions_utils as func

fibonacci = []

print('\nBem vindo ao Sistema Sequência de Fibonacci!\n')

number = func.validate_integer_positive('Informe um número até onde a série de Fibonacci será apresentada: ')

for i in range (number):
    if(i == 0):
        fibonacci.append(0)
    elif (i == 1):
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

#outra forma de imprimir
for x in range(len(fibonacci)):
    print(fibonacci[x])

print(*fibonacci, sep=", ")
