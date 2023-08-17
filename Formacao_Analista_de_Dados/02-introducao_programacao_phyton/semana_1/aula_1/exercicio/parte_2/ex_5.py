type_number = ['TIME X', 'TIME Y','TIME Z']

def convert_coma_point(number):
 if(number.count(',') > 0):
    number = number.replace(',', '',number.count(',')-1).replace(',','.')
 if (number.count('.') > 1):     
    number = number.replace('.', '',number.count('.')-1)
 return number

def validate_number(type_number):
  print('\nInforme o número de torcedores do ' + type_number + ':')
  number = input()
  while(not number.replace(',','').replace('.','').isdigit()):
    print('Entrada inválida! \nInforme o número de torcedores do ' + type_number + ':')
    number = input() 
  number = convert_coma_point(number)
  return number

print('\nBem vindo ao sistema Percentual de Torcidas!!\n')

team_X = validate_number(type_number[0])
team_Y = validate_number(type_number[1])
team_Z = validate_number(type_number[2])

total_fans = (float(team_X) + float(team_Y) + float(team_Z))

print('\nO percentual de torcedores do ' + str(type_number[0]) + ' é: %.2f' % ((float(team_X) * 100)/float(total_fans)) + '%.')
print(  'O percentual de torcedores do ' + str(type_number[1]) + ' é: %.2f' % ((float(team_Y) * 100)/float(total_fans)) + '%.')
print(  'O percentual de torcedores do ' + str(type_number[2]) + ' é: %.2f' % ((float(team_Z) * 100)/float(total_fans)) + '%.')
print('Número total de torcedores: ' + str(int(total_fans)) + '.')