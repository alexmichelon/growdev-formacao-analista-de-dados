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

print('\nBem vindo ao sistema Cálculo de Ingredientes para biscoitos!')

#48 cookies = 1.5 sugar_coup + 1 butter_coup + 2.75 flour_coup

wanted_cookies = validate_number('\nQuantos biscoitos desejas produzir? ')

sugar_coup  = ( 1.5 * wanted_cookies) / 48
butter_coup = (   1 * wanted_cookies) / 48
flour_coup  = (2.75 * wanted_cookies) / 48

print('\nPara produzir ' + str(float(round(wanted_cookies,2))) + ' biscoitos são necessárias: \n' + str(float(round(sugar_coup,2))) + ' xícaras de açúcar\n' + str(float(round(butter_coup,2))) + ' xícaras de manteirga\n' + str(float(round(flour_coup,2))) + ' xícaras de farinha')