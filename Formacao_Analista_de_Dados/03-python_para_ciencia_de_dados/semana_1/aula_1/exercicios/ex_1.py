'''
1) Faça um Programa que leia um vetor de 10 números reais e mostre-os na
ordem inversa.
'''

import functions_utils as func

numbers = []
total_numbers_inform = 10

print('\nBem vindo ao sistema imprime números em ordem inversa!!!!\n')

for i in range(0,total_numbers_inform,1):
    number = func.validate_integer_positive('Informe um número real: ')
    numbers.append(number)

#método que inverte as posições da lista
#numbers.reverse()
#print(numbers)

#imprimindo invertido com reversed() uma posição por linha
'''for i in reversed(numbers):
    print(i)

#imprimindo invertido com reversed() todas as posições na mesma linha
print(*reversed(numbers), sep=',')'''

#imprimindo inverso com while()
'''i = 4
while(i >= 0):
    print(numbers[i])
    i -= 1'''

#imprimindo inverso com for()
for i in range(total_numbers_inform-1, -1, -1):
    print(numbers[i])
print('\n')
for i in range(1,11):
    print(numbers[-i])