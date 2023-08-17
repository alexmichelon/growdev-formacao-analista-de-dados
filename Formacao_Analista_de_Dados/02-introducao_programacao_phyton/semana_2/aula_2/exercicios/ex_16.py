'''
16) Escreva um programa que conte em ordem reversa, de 25 a zero.
'''

print('\nBem vindo ao sistema Conta Número em Ordem Reversa\n')

number = 25

'''#uma forma
for i in range(number):
    print(f'{number}')
    number -= 1'''

for i in range(number, 0, -1):    
    print(f'{i}')