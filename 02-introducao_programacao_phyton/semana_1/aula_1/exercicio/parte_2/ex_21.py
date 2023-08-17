def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

def validate_number(order):
    value = input(order)
    while(not value.replace('-', '').replace(',','').replace('.', '').isdigit()):
        value = input('\nEntrada Inválida!\n' + order)
    value = convert_coma_point(value)
    return float((value))

print('\nBem vindo ao sistema que calcula rendimentos!')

month_application = validate_number('\nInforme o valor da aplicação mensal: $')
tax               = validate_number('Informe a taxa (em percentual): ')
tax               = tax / 100
month_acounts     = validate_number('Informe o número de meses: ')
present_value     = 0

#formula para determinar rendimento em poupança programada, sendo:
#P = valor presente
#M = valor aplicado mensal
#i = taxa
#n = número de meses
#F = P.(1+i)^n + M.[(1+i)^n - 1]/i

income = ((present_value * (1 + (tax  /100) ** month_acounts)) + (month_application * ((1 + tax) ** month_acounts - 1))) / tax

print('\nO valor do rendimento é de : $' + str(float(round(income,2))))