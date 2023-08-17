import numpy as np

list_purchase = np.array(
    [
    ['',0,0.0,0.0],
    ['',0,0.0,0.0],
    ['',0,0.0,0.0],
    ['',0,0.0,0.0],
    ['',0,0.0,0.0]
    ]
)

tax = 0.06

def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

def validate_number(order):
    value = input('\nInforme ' + order + ' produto:')
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input('\nEntrada Inválida!'
                      'Informe ' + order + ' produto:')
    value = convert_coma_point(value)
    return float(value)

def inform_purchase():
    for i in range(5):
        for j in range(4):
            if (j == 0):
                list_purchase[i,j] = input('Informe o produto: \n')
            elif (j == 1):
                list_purchase[i,j] = validate_number('o quantidade do')
            elif (j == 2):
                list_purchase[i,j] = validate_number('o preço unitário do')
            else:
                list_purchase[i,j] = (float(list_purchase[i,j-1]) * float(list_purchase[i, j-2]))

def invoice():
    for i in range(5):
        for j in range(4):
            if (j == 0):
                print('\nProduto: ' + list_purchase[i,j])
            elif (j == 1):
                print('Quantidade: ' + list_purchase[i,j])
            elif (j == 2):
                print('Preço Unitário: $' + list_purchase[i,j])
            else:
                print('Total Por Produto: $' + list_purchase[i,j])

def calculate_subtotal():
    result = 0
    for i in range(5):
        result = result + float(list_purchase[i, 3])
    return float(result)

def calculate_tax_value(result):
    result = result * tax
    return float(result)

def total_purchase():
    result = calculate_subtotal() + calculate_tax_value(calculate_subtotal())
    return result

print('Bem vindo ao sistema Compra de 5 Produtos!\n')
inform_purchase()
print('\nCUPOM FISCAL')
invoice()
print('----------\nSubtotal: $' + str(float(round(calculate_subtotal(),2))))
print('----------\nImposto (6%): $' + str(float(round(calculate_tax_value(calculate_subtotal()),2))))
print('----------\nValor A Pagar: $' + str(float(round(total_purchase(),2))))