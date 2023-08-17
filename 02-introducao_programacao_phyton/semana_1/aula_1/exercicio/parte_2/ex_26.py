#valida se o número informado é inteiro, não decimal e não texto
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()) or (value.count(',') > 0) or (value.count('.') > 0):
        value = input('\nEntrada Inválida!\n' + order)
    return int(value)

print('\nBem vindo ao Sistema Conversão de Minutos em Horas e Dias!')

minutes = validate_number('Informe o número de minutos: ')
hours = (int(minutes) / 60)
days  = (int(minutes) / 1440)

print(str(minutes) + ' minutos corresponde há:\n' + str(float(round(hours,2))) + ' horas\n' + str(float(round(days,2))) + ' dias')

