'''
3) Escreva um programa que receba a idade do usuário e exiba a mensagem
“Maior de idade” caso a idade seja maior ou igual de 18 anos e a mensagem
“Menor de idade” caso a idade seja menor de 18 anos.
'''

#Valida se o String informado pelo usuário é um inteiro positivo
def validate_number(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    return int(value)

print('\nBem vindo ao programa Maior/Menor de Idade!\n')

age = validate_number('Informe a idade: ')

if(age >= 18):
    print('Maior de idade.')
else:
    print('Menor de idade.')