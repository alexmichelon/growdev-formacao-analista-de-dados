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

cookie = 1
cookies_bag = 40 * cookie
portion = 4 * cookie
calories = 10 * portion

print('\nSeja bem vindo ao Cálculo de Calorias por Biscoitos consumidos!\n')

cookies_eaten = validate_number('Informe quantos biscoitos você consumiu:\n')

calories = (float(round(cookies_eaten,2)) / 4) * 300

print('\nEstes biscoitos correspondem à ' + str(calories) + ' calorias.')