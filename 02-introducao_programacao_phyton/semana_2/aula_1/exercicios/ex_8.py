'''
8) Faça um programa para ler a quantidade adquirida e o preço unitário de um
produto.
a) Calcular e escrever o total
   total = quantidade adquirida * preço unitário
b) Leia o desconto sobre a compra e calcule.
      total a pagar = total - desconto
   i) Sabendo-se que:
      (1) Se quantidade <= 5 o desconto será de 2%.
      (2) Se quantidade > 5 e quantidade <=10 o desconto será de 3%.
      (3) Se quantidade > 10 o desconto será de 5%.
'''

#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float, incluindo negativos
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    value = convert_coma_point(value)
    return float((value))

print('\nBem vindo ao Sistema Cálculo de produtos!!\n')

product_amount = validate_number('Informe a quantidade adquirida do produto: ')
product_price = validate_number('Informe o valor unitário do produto: R$ ')
discount = 0
total_purchased = product_amount * product_price
print(f'\nO total da compra é R$ {total_purchased:.2f}')

if(product_amount <= 5):
   discount = 0.02
elif(product_amount > 5) and (product_amount <= 10):
   discount = 0.03
else:
   discount = 0.05
total_purchased = total_purchased - (total_purchased * discount)
print(f'O total a pagar é: R$ {total_purchased:.2f}')
