#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float, incluindo negativos
def validate_float_negative(order):
    value = input(order)
    while(not value.replace('-','').replace(',','').replace('.', '').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    value = convert_coma_point(value)
    return float((value))

#Valida se o String informado pelo usuário é um float positivos
def validate_float_positive(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}:\n')
    value = convert_coma_point(value)
    return float((value))

#Valida se o String informado pelo usuário é um float positivos menor ou igual a 10
def validate_float_positive_less10(order):
    value = input(order)
    value = convert_coma_point(value)
    while(not value.replace(',', '').replace('.','').isdigit()) or (float(value.replace(',','.')) > 10):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    return float(value)

#Valida se o String informado pelo usuário é um float positivos menor ou igual a 10
def validate_float_positive_whit_range_included(order, initial_range, final_range):
    value = input(order)
    value = convert_coma_point(value)
    while(not value.replace(',', '').replace('.','').isdigit()) or (float(value) < initial_range) or (float(value) < final_range):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    return float(value)

#Valida se o String informado pelo usuário é um inteiro positivo qualquer
def validate_integer_positive(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}:\n')
    return int(value)

#calida se o String informado pelo usuário é um inteiro positivo dentro de faixa passada por parâmetro
def validate_integer_positive_whit_range_included(order, initial_range, final_range):
    value = input(order)
    while (not value.isdigit()) or (int(value) < initial_range) or (int(value) > final_range):
            value = input(f'\nEntrada Inválida!\n{order}\n')
    return int(value)

#Valida se o String informado pelo usuário é um inteiro incluindo negativos
def validate_integer_negative(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    return int(value)

#valida se a opção digitada pelo usuário é valida 'S ou 'N'
def validate_option(order, comparision):
    option = input(order)
    while(option not in (comparision)):
        option = input(f'\nEntrada Inválida!\n{order}\n')
    return option

#Calcula fatorial com for
def factorial_calculate_for(number):
    factorial_result = 1
    for i in range(1, number+1):
        factorial_result *= i
    return factorial_result

#Calcula fatorial com while
def factorial_calculate_while(number):
    i = 1
    factorial_result  = 1
    while(i != (number+1)):
        factorial_result = factorial_result * i
        i = i + 1
    return factorial_result

#valida se o caracter digitado é alfabético
def validate_caracter_is_alpha(order):
    text = input(order).upper() 
    while(not text.isalpha()):
        text = input(f'Entrada informada não é letra!\n{order}').upper() 
    return text

#converte valor float em moeda (Brasil)
def convert_to_currency(value):
    x = "{:,.2f}".format(float(value))
    y = x.replace(',','x')
    z = y.replace('.',',')
    return z.replace('x','.')