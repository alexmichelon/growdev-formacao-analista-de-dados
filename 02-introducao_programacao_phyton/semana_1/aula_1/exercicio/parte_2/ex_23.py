#utiliza interpolação linear
first_interval_inicial_value  = 0
first_interval_final_value    = 1000
second_interval_inicial_value = -1
second_interval_final_value   = 1

def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

def validate_number(isInterval, order):
    value = input(order)
    if(isInterval == False):
        while(not value.replace(',','').replace('.', '').isdigit()) or (float(convert_coma_point(value)) < first_interval_inicial_value) or (float(convert_coma_point(value)) > first_interval_final_value):
            value = input('\nEntrada Inválida!\n' + order)  
            print(value + ' Primeiro While')
    else:
        while(not value.replace(',','').replace('.', '').isdigit()):
            value = input('\nEntrada Inválida!\n' + order) 
            print(value + ' Segundo While')
    value = convert_coma_point(value)
    return float((value))

print('\nBem vindo ao sistema Conversão de valor 0 e 1000 em -1 e 1!')

option = input( 'Desejas informar os intervalos a serem comparados? S/N\n'
                'Caso não seja informado, os intervalos utilizados serão:\n'
                'Valor de início do primeiro intervalo (x1) = 0\n'
                'Valor final do primeiro intervalo     (x2) = 1000\n'
                'Valor de início do segundo intervalo  (y1) = -1\n'
                'Valor final do segundo intervalo      (y2) = 1\n').upper()

while(option not in ('S', 'N')):
    option = input('\nEntrada Inválida!\n'
                   'Desejas informar os intervalos a serem comparados? S/N\n'
                   'Caso não seja informado, os intervalos utilizados serão:\n'
                   'Valor de início do primeiro intervalo (x1) = 0\n'
                   'Valor final do primeiro intervalo     (x2) = 1000\n'
                   'Valor de início do segundo intervalo  (y1) = -1\n'
                   'Valor final do segundo intervalo      (y2) = 1\n').upper()
    
if(option == 'S'):
    first_interval_inicial_value  = validate_number(True, '\nInforme o valor de início para o primeiro intervalo (x1): ')
    first_interval_final_value    = validate_number(True, 'Informe o valor final para o primeiro intervalo     (x2): ')
    second_interval_inicial_value = validate_number(True, 'Informe o valor de início para o segundo intervalo  (y1): ')
    second_interval_final_value   = validate_number(True, 'Informe o valor final para o segundo intervalo      (y2): ') 

first_interval_number_informed = validate_number(False, '\nInforme um número dentro o intervalo ' + str(first_interval_inicial_value) + ' e ' + str(first_interval_final_value) + ': ')

"""""
- Interpolação linear
y = y1 + ((x - x1)/(x2 - x1))*(y2 - y1)
onde:
x = número informado dentro do conjunto x1 e x2
y = número retornado correspondente a x no intervalo y1 e y2
"""

second_interval_number_corresponding = second_interval_inicial_value + ((first_interval_number_informed - first_interval_inicial_value) / (first_interval_final_value - first_interval_inicial_value)) * (second_interval_final_value - second_interval_inicial_value)

print('\nO número informado ' + str(first_interval_number_informed) + ' (do intervalo x1='+ str(first_interval_inicial_value) + ' e x2=' + str(first_interval_final_value) +') tem como corrrespondente entre o intervalo (y1=' + str(second_interval_inicial_value) +' e y2=' + str(second_interval_final_value) + ') o número ' + str(second_interval_number_corresponding))
