'''
15) Escreva um programa que imprima na tela para escrever a tabuada de um
número fornecido pelo usuário, de 1 a 10.
'''

import functions_utils as func

amount_numbers = 11

def print_multiplication(number):
   print('Tabuada do ' + str(number))
   for i in range (amount_numbers):
      print(str(int(number)) + ' * ' + str(i) + ' = ' + str(int(number) * int(i)))
    

print('Bem vindo ao sistema informa tabuada 1 a 10!')

number = func.validate_integer_positive_comparision('Informe um número entre 1 e 10: ', '"1","2","3","4","5","6","7","8","9","10"')
  
print_multiplication(number)