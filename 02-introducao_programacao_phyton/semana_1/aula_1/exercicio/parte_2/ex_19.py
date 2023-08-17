def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

def validate_number(order):
    value = input(order)
    while(not value.replace('-', '').replace(',','').replace('.', '').isdigit()):
        value = input('\nEntrada Inválida!\n' + order + '\n')
    value = convert_coma_point(value)
    return float((value))

print('\nBem vindo ao sistema Encontro de Raízes por Meio da Fórmula de Bhaskara:')

a = validate_number('Informe o valor do coeficiente A:')
b = validate_number('Informe o valor do coeficiente B:')
c = validate_number('Informe o valor do coeficiente C:')

x1 =(((float(b) * - 1) + (((float(b) ** 2) - (4 * float(a) * float(c))) ** (1 / 2))) / (2 * float(a)))
x2 =(((float(b) * - 1) - (((float(b) ** 2) - (4 * float(a) * float(c))) ** (1 / 2))) / (2 * float(a)))

print('\nValor das raízes: \nx1: ' + str(float(round(x1,2))) + '\nx2: ' + str(float(round(x2,2))))