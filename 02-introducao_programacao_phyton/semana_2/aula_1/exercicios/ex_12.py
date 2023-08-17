'''
12)Construa um programa que leia uma data qualquer (dia, mês e ano) e calcule
a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro
tem 29 dias. Lembre-se que um ano é bissexto quando for divisível por 4.
'''

day = 0
month = 0
year = 0

#Valida se o String informado pelo usuário é um inteiro positivo
def validate_integer(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    return int(value)

def is_valid_date(day, month, year):
    if((day > 0) and (day <= 31)):
        if(month in (1, 3, 5, 7, 8, 10, 12)):
            return True
        elif(month in (4, 6, 9, 11)) and (day <= 30):
            return True
        elif(month == 2):
            if((year % 4 == 0)) and (day <= 29):
                return True
            elif(day <= 28):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print('\nBem vindo ao sistema Data do Próximo Dia!!\n')

day   = validate_integer('Informe o dia: ')
month = validate_integer('Informe o mês: ')
year  = validate_integer('Informe o ano: ')

while True:
    if(is_valid_date(day, month, year) == True):
        break
    else:
        print('\nData Inválida!\n')
        day   = validate_integer('Informe o dia: ')
        month = validate_integer('Informe o mês: ')
        year  = validate_integer('Informe o ano: ')

day = day + 1

while(is_valid_date(day, month, year) == False):
    if(month in ((1, 3, 5, 7, 8, 10, 12)) and (day > 31)):
        day = 1
        month = month + 1
        if(month > 12):
            day = 1
            month = 1
            year = year + 1
    elif(month in (4, 6, 9, 11)) and (day > 30):
        day = 1
        month = month + 1
    elif(month == 2):
        if((year % 4 == 0)) and (day > 29):
            day = 1
            month = month + 1
        elif(day > 28):
            day = 1
            month = month + 1

print(f'A próxima data válida é {day}/{month}/{year}.')