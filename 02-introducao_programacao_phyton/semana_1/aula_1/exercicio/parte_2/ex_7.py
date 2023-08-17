type_number = ['ANOS', 'MESES','DIAS']

def validate_number(type_number):
  print('\nInforme os ' + type_number + ' da idade:')
  number = input()
  while(number.isdigit() == False):
    print('\nEntrada inválida: valor informado não é um número inteiro! \nInforme os ' + type_number + ' da idade:')
    number = input() 
  return number 

print('\nBem vindo ao cálculo de dias de idade:\n')

years  = validate_number(type_number[0])
months = validate_number(type_number[1])
days   = validate_number(type_number[2])

days_age = ((int(years) * 365) + (int(months) * 31) + int(days))

print('\nA idade em dias é: ' + str(days_age) + '.')