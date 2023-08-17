'''
2) Escreva um programa que receba um número e escreva “Par” caso esse
número seja par e escreva “Impar” caso esse número seja impar
'''

#Valida se o String informado pelo usuário é um inteiro positivo
def validate_number(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    return int(value)

print('\nBem vindo ao programa Número Par e Impar!\n')

number = validate_number('Informe um número: ')

#Calcula se o resto da divisão do número informado é igual a 0
if (number % 2) == 0: 
    #Caso seja igual a zero, é par
    type_number = 'PAR'
else:
   #Caso seja diferente de zero, é impar
   type_number = 'IMPAR'

#Imprime a opção informada e o tipo do número (par ou impar) 
print(f'\nImprimindo com função: O número informado {number} é {type_number}.')
#outra forma de fazer a mesma impressão
print('\nImprimindo com concatenação: O número informado ' + str(number) + ' é ' + type_number + '.')