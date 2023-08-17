def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input('\nEntrada Inválida!\n' + order + '\n')
    value = convert_coma_point(value)
    return float((value))

print('Bem vindo ao sistema Cálculo de Hipotenusa!\n')

opposite_leg = validate_number('Informe o valor do Cateto Oposto: ')
adjacent_leg = validate_number('Informe o valor do Cateto Adjacente: ')

hypotenuse = ((opposite_leg ** 2) + (adjacent_leg ** 2)) ** (1/2)
print('\nO valor da hipotenusa é: ' + str(float(round(hypotenuse,2))))