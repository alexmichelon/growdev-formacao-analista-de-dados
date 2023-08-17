'''
11)Escreva um programa que peça ao usuário para fornecer um dia, mês e o
ano arbitrários e determine se esses dados correspondem a uma data válida.
Não deixe de considerar que existem meses com 30 e 31 dias, e que
fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto.
Considere que um ano é bissexto quando for divisível por 4.
'''

#Valida se o String informado pelo usuário é um inteiro positivo
def validate_integer(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    return int(value)

print('\nBem vindo ao sistema Data Válida!!\n')

day = validate_integer('Informe o dia: ')
month = validate_integer('Informe o mês: ')
year = validate_integer('Informe o ano: ')

if((day > 0) and (day <= 31)):
    if(month in (1, 3, 5, 7, 8, 10, 12)):
        print(f'A data informada {day}/{month}/{year} É uma data válida!')
    elif(month in (4, 6, 9, 11)) and (day <= 30):
        print(f'A data informada {day}/{month}/{year} É uma data válida!')
    elif(month == 2):
        if((year % 4 == 0)) and (day <= 29):
            print(f'A data informada {day}/{month}/{year} É uma data válida!')
        elif(day <= 28):
            print(f'A data informada {day}/{month}/{year} É uma data válida!')
        else:
            print(f'A data informada {day}/{month}/{year} NÃO É uma data válida!')    
    else:
        print(f'A data informada {day}/{month}/{year} NÃO É uma data válida!')
else:
    print(f'A data informada {day}/{month}/{year} NÃO É uma data válida!')