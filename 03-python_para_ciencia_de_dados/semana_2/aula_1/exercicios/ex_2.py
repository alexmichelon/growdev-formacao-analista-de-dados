'''
2) Faça um programa, com uma função que necessite de um argumento. A
função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’,
se seu argumento for zero ou negativo.
'''
from functions_utils import validate_float_negative

def retorna_positivo_ou_negativo(argumento):
    if(argumento >= 0):
        return 'P'
    else:
        return 'N'
    
argumento = validate_float_negative('Informe o argumento: ')

print(retorna_positivo_ou_negativo(argumento))