'''
14) Desenvolver um programa que efetue a soma de todos os números ímpares
que se encontram no conjunto dos números de 1 até 500.
'''

sum = 0

print('\nBem vindo ao sistema soma de números ímpares!\n')

for i in range(1, 501):
    if(i % 2) != 0:
        sum += i

print(f'A soma dos números ímpares entre 1 e 500 é: {sum}')