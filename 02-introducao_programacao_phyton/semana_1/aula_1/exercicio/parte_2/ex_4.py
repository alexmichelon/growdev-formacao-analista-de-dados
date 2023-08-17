type_number = ['PRIMEIRO', 'SEGUNDO','TERCEIRO']

def convert_coma_point(number):
 if(number.count(',') > 0):
    number = number.replace(',', '',number.count(',')-1).replace(',','.')
 if (number.count('.') > 1):     
    number = number.replace('.', '',number.count('.')-1)
 return number

def validate_number(type_number):
  print('\nInforme o ' + type_number + ' número:')
  number = input()
  number = convert_coma_point(number)
  while(not number.replace('-', '').replace(',','').replace('.','').isdigit()):
    print('Entrada inválida! Informe o ' + type_number + ' número: ')
    number = input() 
    number = convert_coma_point(number)
  return number

print('\nBem vindo ao sistema soma de dois números e divisão pelo terceiro número!\n')

first_number  = validate_number(type_number[0])
second_number = validate_number(type_number[1])
third_number  = validate_number(type_number[2])

result = (float(first_number) + float(second_number))/float(third_number)

#print('\nO resultado do primeiro número ' + str(first_number) + ' + segundo número ' + str(second_number) +' dividido pelo terceiro número ' + str(third_number) + ' é = ' + str(float(round(result,2))))
print(f'\nO resultado do primeiro número  {first_number} + segundo número {second_number} dividido pelo terceiro número {third_number} é = {result:.2f}')