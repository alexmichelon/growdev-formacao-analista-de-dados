'''
5) Escreva um programa para solicitar ao usuário o raio r de uma esfera, e
calcular o volume V da esfera usando uma função, e exibir o resultado. Utilize
a seguinte fórmula para determinar o volume:

v = (4.0 / 3.0) * π * r3
'''
from functions_utils import validate_float_positive

pi = 3.14

def calcula_volume_esfera(raio):
    volume = (4.0 / 3.0) * pi * (raio**3)
    return volume

raio = validate_float_positive('Informe o valor do raio da esfera: ')

volume = calcula_volume_esfera(raio)

print(f' O volume da esfera é: {volume:.2f}.')