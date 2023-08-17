def validate_value(order):
    value = input('Informe a idade da ' + order + ' pessoa: ')
    while(not value.isdigit()):
        value = input('\nEntrada inválida!\n'
                      'Informe a idade da ' + order + ' pessoa: ')  
    return int(value)

print('\nSeja bem vindo ao Cálculo de Somatório de Idades!!!\n')
ages = 0
for i in range (3):
    if(i == 0):
        order = 'primeira'
    elif(i == 1):
        order = 'segunda'
    else:
        order = 'terceira'
    ages = ages + validate_value(order)

print('\nA soma das idades é: ' + str(ages) + ' anos.')
        
