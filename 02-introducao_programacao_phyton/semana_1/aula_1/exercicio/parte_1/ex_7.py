close_purchase = 'N'
total_purchase = 0
invoice = ''
tax = 0.1
discount = 0.07
total_tax = 0
total_discount = 0


#no valor informado substitui vírgulas por pontos e mantem o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#valida se o valor informado é número e não texto (inclui números negativos)
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input('\nEntrada Inválida!\n' + order + '\n')
    value = convert_coma_point(value)
    return float((value))

def validate_close_purchase():
  close_purchase = input('Deseja finalizar a compra? S/N ').upper()
  while(close_purchase not in ('S', 'N')):
    close_purchase = input('Entrada inválida! Deseja finalizar a compra? S/N ').upper()
  return close_purchase  

print('\nBem vindo ao programa Total de Uma Compra em uma Loja de Roupas\n')

while(close_purchase == 'N'):
  purchased_item = input('Informe o produto (descrição): ')
  quantity_purchased_item = validate_number('Informe a quantidade do produto: ')
  value_purchased_item = validate_number('Informe o preço unitário do produto: $')
  invoice = invoice + '\nItem: ' + str(purchased_item)  + '\n' + 'Quantidade do Item: '  + str(quantity_purchased_item) + '\n' + 'Valor Unitário: $' + str(float(round(value_purchased_item,2))) + '\n' + 'Valor dos itens: $' + str(float(round(quantity_purchased_item * value_purchased_item,2))) + '\n'
  total_purchase = total_purchase + (float(quantity_purchased_item) * float(value_purchased_item))
 
  close_purchase = validate_close_purchase()

  if(close_purchase == 'S'):
  
    if(float(total_purchase) > 300):
      #se compra maior que $300, ganha desconto 
      total_discount = (float(total_purchase) * discount)
      
      if(float(total_purchase) > 400):
        #se compra maior que $400, paga imposto 
        total_tax = (float(total_purchase) * tax)
    
    total_purchase = float(total_purchase) - float(total_discount) + float(total_tax)

    invoice = '\n-----CUPOM FISCAL-----' + invoice + '----------\nDesconto: $' + str(float(round(total_discount,2))) + '\n----------\nImposto: $' + str(float(round(total_tax,2))) + '\n----------\nTotal da Compra: $' + str(float(round(total_purchase,2))) + '\n'
    print(str(invoice)) 

    break
