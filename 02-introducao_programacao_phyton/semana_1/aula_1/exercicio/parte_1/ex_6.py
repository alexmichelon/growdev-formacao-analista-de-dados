#valida se o número informado é maior que zero e não é decimal
def validaNumero(order):
  number = input(order)
  while(not number.replace(',','').replace('.', '').isdigit()) or (number.count(',') > 0) or (number.count('.') > 0):
    number = input('\nEntrada inválida!\n' + order)
  return number

print('\nBem vindo ao Sistema de Verificação de Idade Maior que 18 Anos!!!\n')

for counter in range (10):
    name = input('Informe o nome completo: ')
    age = validaNumero('Informe a idade: ')
    if(int(age) > 18):
        print (name + ' é maior de 18 anos. Sua idade é: ' + str(age) + ' anos.\n')