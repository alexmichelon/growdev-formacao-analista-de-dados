'''
5) Construa um programa que permita a um usuário informar uma série de
números, até que um número negativo seja fornecido. Ao final, imprima o
somatório desses números, a média, o valor máximo e o mínimo.
Desconsidere o último número (negativo) informado pelo usuário.
'''

import numpy as np
import functions_utils as func

list_number_series = []
number_informed = 0
numbers_sum = 0

print('\nBem vindo ao sistema que pára ao ter um número negativo informado!!!!\n')

number_informed = func.validate_float_negative('Informe um número: ')

#enquanto um número negativo não é informado
while(int(number_informed) >= 0):
    #adiciona o número na lista
    list_number_series.append(number_informed)
    #informa novo número para a lista, caso informado número negativo este não é adicionado a lista
    number_informed = func.validate_float_negative('Informe um número: ')

if(len(list_number_series) > 0):
    #soma todos os valores da lista
    print(f'\nO somatório dos números informados é: {sum(list_number_series):.2f}.')
    #gera a média aritmética dos ítens da lista
    print(f'A média dos números informados é: {np.mean(list_number_series):.2f}.')
    #retorna o maior valor contido na lista
    print(f'O valor máximo dentre os números informados é: {max(list_number_series)}.')
    #retorna o menor valor contido na lista
    print(f'O valor mínimo dentre os números informados é: {min(list_number_series)}.')
else:
    print(len(list_number_series))
    #caso nenhuma informação seja informada, apresenta esta mensagem (lista vazia)
    print('Lista vazia: nenhum número válido (maior que zero) informado.')