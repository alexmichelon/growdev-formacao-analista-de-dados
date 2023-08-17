import numpy as np

#
list_products = np.array(
    [
        ['PÃO FRANCES', 0, 0.75],
        ['PÃO DOCE',    0, 0.85],
        ['QUINDIM',     0, 1.5 ]
    ]
)

tax = 0.05
value_to_save = 0.10

def convert_coma_point(number):
    if(number.count(',') > 0):
        number = number.replace(',', '',number.count(',')-1).replace(',','.')
    if (number.count('.') > 1):     
        number = number.replace('.', '',number.count('.')-1)
    return number

def validate_number(data_inform, list_products):
    number = input('\nInforme ' + data_inform + ' ' + list_products + ' vendidos no dia:\n')
    while(not number.replace(',', '').replace('.', '').isdigit()):
        number = input('\nEntrada inválida! \nInforme ' + data_inform + '  de ' + list_products + ' vendidos no dia:\n') 
    number = convert_coma_point(number)
    return float(number)

def amounts_produtcs(list_products):
    data_inform = 'a quantidade de'
    list_products[0,1] = validate_number(data_inform,list_products[0,0])
    list_products[1,1] = validate_number(data_inform,list_products[1,0])
    list_products[2,1] = validate_number(data_inform,list_products[2,0])
    return list_products

def price_informed_produtcs(list_products):
    data_inform = 'o preço unitário do'
    list_products[0,2] = validate_number(data_inform, list_products[0,0])
    list_products[1,2] = validate_number(data_inform, list_products[1,0])
    list_products[2,2] = validate_number(data_inform, list_products[2,0])
    return list_products

def total_billed(list_products):
    value = (float(list_products[0,1]) * float(list_products[0,2])) + (float(list_products[1,1]) * float(list_products[1,2])) + (float(list_products[2,1]) * float(list_products[2,2]))
    return round(float(value),2)

def print_total_billed(list_products):
    print_list_products_bought()
    print('O valor total faturado na padaria no dia foi de', end=': $ ')
    print(total_billed(list_products))

def print_list_products_bought():
    print('\n-----Lista de Produtos Vendidos no dia:-----\n')
    for i in range(3):
                for j in range(3):
                    if (j == 0):
                        print('Produto: ' + list_products[i, j])
                    elif(j == 1):
                        print('Quantidade: ' + list_products[i, j])
                    else:
                        print('Valor Unitário: $' + list_products[i, j] + '\n'
                              '-----------------------------------------------')

def total_to_save(list_products):
    value = (total_billed(list_products) * 0.10)
    return round(float(value),2)

def print_total_to_save(list_products):
    print('\nO valor total a ser poupado referente ao valor faturado no dia foi de', end=': $ ')
    print(total_to_save(list_products))

def total_to_save_whit_tax(list_products):
    value = (total_billed(list_products) - (total_billed(list_products) * (tax))) * value_to_save
    return round(float(value),2)

def print_total_to_save_whit_tax(list_products):
    print('\nO valor total a ser poupado considerando o imposto de "5%" sobre o valor faturado no dia foi de', end=': $ ')
    print(total_to_save_whit_tax(list_products))

def menu_inicial():
    opt_menu = input('\nDigite 1 (Primeira parte): para cálculo do total de produtos vendidos com preços unitários pré-fixados dos produtos\n'
                'Digite 2 (Modificação 1): para cálculo do total de produtos vendidos informando preços unitários dos produtos\n'
                'Digite 3 (Modificação 2): para cálculo do total a ser poupado em caderneta de poupança com base no total de produtos vendidos\n'
                'Digite 4 (Modificação 3): para cálculo do total a ser poupado em caderneta de poupança com base no total de produtos vendidos considerando imposto\n'
                'Digite 0: para sair\n')
    while (opt_menu not in ('0','1', '2', '3', '4')): 
        opt_menu = input('\nEntrada Inválida!\n'
                    'Digite 1 (Primeira parte): para cálculo do total de produtos vendidos com preços unitários pré-fixados dos produtos\n'
                    'Digite 2 (Modificação 1): para cálculo do total de produtos vendidos informando preços unitários dos produtos\n'
                    'Digite 3 (Modificação 2): para cálculo do total a ser poupado em caderneta de poupança com base no total de produtos vendidos\n'
                    'Digite 4 (Modificação 3): para cálculo do total a ser poupado em caderneta de poupança com base no total de produtos vendidos considerando imposto\n'
                    'Digite 0: para sair\n')              
    return int(opt_menu)

def type_price():
    value = 'S'
    value = input('\nDeseja informar o valor unitário de cada produto? S/N\n'
                      'Obs.: os preços unitários existentes dos produtos são:\n'
                      'PÃO FRANCES = $ 0.75\n'
                      'PÃO DOCE    = $ 0.85\n'
                      'QUINDIM     = $ 1.50\n').upper()
    while (value not in ('S', 'N')):
        value = input('\nEntrada Inválida!\n'
                      'Deseja informar o valor unitário de cada produto? S/N\n'
                      'Obs.: os preços unitários existentes dos produtos são:\n'
                      'PÃO FRANCES = $ 0.75\n'
                      'PÃO DOCE    = $ 0.85\n'
                      'QUINDIM     = $ 1.50\n').upper()
    return value

print('\nBem vindo ao sistema PADARIA DO PAULO!')
opt_menu = menu_inicial()

while (opt_menu in (1, 2, 3, 4)):
    if(opt_menu == 1):
        list_products = amounts_produtcs(list_products)
        print_total_billed(list_products)
    elif(opt_menu == 2):
        list_products = price_informed_produtcs(list_products)
        list_products = amounts_produtcs(list_products)
        print_total_billed(list_products)
    elif(opt_menu == 3):
        list_products = amounts_produtcs(list_products)
        opt_type_price = type_price()
        if(opt_type_price == 'S'):
            list_products = price_informed_produtcs(list_products)
        print_total_billed(list_products)
        print_total_to_save(list_products)
    elif(opt_menu == 4):
        list_products = amounts_produtcs(list_products)
        opt_type_price = type_price()
        if(opt_type_price == 'S'):
            list_products = price_informed_produtcs(list_products)        
        print_total_billed(list_products)
        print_total_to_save_whit_tax(list_products)
    else:
        break
    list_products[0,2] = 0.75
    list_products[1,2] = 0.75
    list_products[2,2] = 1.5

    opt_menu = menu_inicial()
