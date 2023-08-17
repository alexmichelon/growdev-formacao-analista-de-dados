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

#Valida se o String informado pelo usuário é um inteiro positivo qualquer
def validate_integer_positive(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}:\n')
    return int(value)

#Valida se o String informado pelo usuário é um inteiro positivo dentro de opções passadas
def validate_integer_positive_comparision(order, comparision):
    value = input(order)
    while(not value.isdigit()) or (value not in (comparision)):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    return value

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

