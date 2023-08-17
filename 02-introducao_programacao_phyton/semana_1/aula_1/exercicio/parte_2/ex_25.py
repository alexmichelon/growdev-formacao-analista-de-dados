#valida se o número informado é inteiro, não decimal e não texto
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()) or (value.count(',') > 0) or (value.count('.') > 0):
        value = input('\nEntrada Inválida!\n' + order)
    return float(value)

def print_multiplication_table(number):
   print('Tabuada do ' + str(number))
   for i in range (11):
      print(str(int(number)) + ' * ' + str(i) + ' = ' + str(int(number) * int(i)))
    

print('Bem vindo ao sistema Informa Tabuada!')

number = validate_number('Informe um número entre 1 e 9: ')
while (number < 1) or (number > 9):
   number = validate_number('\nEntrada Inválida!\nInforme um número entre 1 e 9: ')

print_multiplication_table(number)