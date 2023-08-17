def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

def validate_number(order):
    value = input('Informe ' + order + ' número:')
    while(not value.replace('-', '').replace(',','').replace('.', '').isdigit()):
        value = input('\nEntrada Inválida!'
                      'Informe ' + order + ' número:')
    value = convert_coma_point(value)
    return float(value)

def plus(value1, value2):
   result = value1 + value2
   return result

def minus(value1, value2):
   result = value1 - value2
   return result

def times(value1, value2):
   result = value1 * value2
   return result

def divided_by(value1, value2):
   result = value1 / value2
   return result

print('\nSeja bem vindo ao Sistema 4 operações matemáticas!!!\n')
value1 = validate_number('primeiro')
value2 = validate_number('segundo')

print('\nA soma dos dois números é: '          + str(plus(value1, value2)))
print('A subtração dos dois números é: '     + str(minus(value1, value2)))
print('A multiplicação dos dois números é: ' + str(float(round(times(value1, value2),2))))
print('A divisão dos dois números é: '       + str(float(round(divided_by(value1, value2),2))))