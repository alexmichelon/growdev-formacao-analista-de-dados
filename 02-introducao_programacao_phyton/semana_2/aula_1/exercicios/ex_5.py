'''
5) Uma empresa vende um produto a R$5,40 a unidade. Sabendo-se que existe
um desconto acumulado de 0,5% do valor total da compra a cada centena
comprada deste produto. Escreva um programa que receba a quantidade
comprada desse produto e informe.
a) O valor total da compra (sem o desconto)
b) A quantidade de centenas compradas desse produto
c) O desconto em R$.
d) O valor total da compra (com desconto)
'''

#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float positivo
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    value = convert_coma_point(value)
    return float((value))

#valida se a opção digitada pelo usuário é valida
def validate_option(order, comparision):
    option = input(order)
    while(option not in (comparision)):
        option = input(f'\Entrada Inválida!\n {order} ')
    return option

#variável preço do produto
product_price = 5.4
#percentual de desconto
discount_percent = 0.05
#total de desconto
total_discount = 0
#total de centenas compradas
total_purchased_hundred = 0

print('\nBem vindo ao sistema Valor de Compra com desconto por centena\n')

product_amount_purchased = validate_number('Informe a quantidade comprada do produto: ')
print(f'Quantidade comprada do produto foi de {product_amount_purchased:.2f} unidades.')

#Total comprado sem desconto
total_purchase = product_amount_purchased * product_price
print(f'\nO valor total da compra sem desconto é de: R$ {total_purchase:.2f}.')

#A quantidade de centenas compradas do produto
if(product_amount_purchased < 100):
    print(f'\nA quantidade de produto comprada foi de {product_amount_purchased}, inferior a uma centena.')
else:
    unit = (product_amount_purchased % 10)
    ten = (((product_amount_purchased - unit) / 10) % 10)
    total_purchased_hundred = ((((product_amount_purchased - unit) / 10) - ten) / 10)
    print(f'A quantidade de centenas compradas do produto foi de {total_purchased_hundred} centena(s).')

#O desconto em R$
if(product_amount_purchased < 100):
    print('Desconto: R$ 0.00. Obs.: Quantidade do produto comprada inferior a 100 unidades.')
else:
    total_discount = (total_purchase * (discount_percent * total_purchased_hundred))
    print(f'Desconto por centena(s) compradas: R$ {total_discount:.2f}.')

#O valor total da compra (com desconto)
total_purchase = total_purchase - (total_discount)
print(f'O total da compra com desconto é de R$ {total_purchase:.2f}')