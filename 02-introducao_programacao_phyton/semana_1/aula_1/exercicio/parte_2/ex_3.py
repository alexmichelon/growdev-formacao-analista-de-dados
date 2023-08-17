option = 'N'
measurement_type  = ['LARGURA', 'COMPRIMENTO', 'ALTURA']

def calculate_volume(box_lenght, box_width, box_height):
    volume = float(box_lenght) * float(box_width) * float(box_height)
    print('\nO valor do volume da caixa é: ' + str(volume) + 'm³.\n\n')

def validade_option():
    print('Encerrar sistema? S/N')
    option = input().upper()
    while(option not in ('S', 'N')):
        print('Entrada Inválida. Encerrar sistema? S/N')
        option = input().upper()
    return option

def convert_coma_point(number):
 if(number.count(',') > 0):
    number = number.replace(',', '',number.count(',')-1).replace(',','.')
 if (number.count('.') > 1):     
    number = number.replace('.', '',number.count('.')-1)
 return number

def validate_measurements(measurement_type):
  number = input('Informe o valor de ' + measurement_type + ' da caixa (em metros(m)): ')
  while(not number.replace(',','').replace('.','').isdigit()):
    number = input('\nEntrada inválida! Informe o valor de ' + measurement_type + ' da caixa (em metros(m)): ')     
  number = convert_coma_point(number)
  return number


print('\nBem Vindos ao Programa Cálculo do Valor do Volume de Caixa Retangular!\n')

while(option == 'N'):
  box_lenght = validate_measurements(measurement_type[0])
  box_width  = validate_measurements(measurement_type[1])
  box_height = validate_measurements(measurement_type[2])

  calculate_volume(box_lenght, box_width, box_height)  
    
  option = validade_option()
    
