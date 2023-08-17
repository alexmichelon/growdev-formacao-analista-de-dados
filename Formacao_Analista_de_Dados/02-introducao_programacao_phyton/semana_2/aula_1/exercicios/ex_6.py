'''
6) Escreva um programa que receba dois números, exiba as opções:
a) 1 - adição
b) 2 - subtração
Então peça ao usuário para escolher uma das opções. Caso escolha a opção
1 o programa deve realizar a soma dos dois números lidos e exibir. Caso
escolha a opção 2 o programa deve realizar a subtração dos dois números
lidos e exibir.
'''

#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float, incluindo negativos
def validate_number(order):
    value = input(order)
    while(not value.replace('-','').replace(',','').replace('.', '').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    value = convert_coma_point(value)
    return float((value))

#valida se a opção digitada pelo usuário é valida
def validate_option(order, comparision):
    option = input(order)
    while(option not in (comparision)):
        option = input(f'\Entrada Inválida!\n {order}')
    return option

def plus(value1, value2):
   result = value1 + value2
   return result

def minus(value1, value2):
   result = value1 - value2
   return result

print('\nSeja bem vindo ao sistema soma/subtração de valores:\n')

value1 = validate_number('Informe o primeiro número: ')
value2 = validate_number('Informe o segundo número: ')

option = validate_option('Informe:\n'
                         '1 - adição\n'
                         '2 - subtração\n', '"1", "2"')

if(option == '1'):
   result = plus(value1, value2)
   signal = '+'
else:
   result = minus(value1, value2)
   signal = '-'

print(f'\n({value1:.2f}) {signal} ({value2:.2f}) = {result:.2f}')