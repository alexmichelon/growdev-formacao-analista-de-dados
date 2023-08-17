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

print('\nBem vindo ao sistema que Cacula a diferença de Ações Compras e Vendidas:\n')

stock_exchange_sold_amount      = validate_number('Informe a quantidade de ações vendidas: ')
stock_exchange_sold_price       = validate_number('Informe o valor unitário da ação vendida: ')
stock_exchange_sold_tax         = validate_number('Informe o percentual da taxa da ação vendida: ')
stock_exchange_purchased_amount = validate_number('Informe a quantidade de ações compradas: ')
stock_exchange_purchased_price  = validate_number('Informe o valor unitário da ação comprada: ')
stock_exchange_purchased_tax    = validate_number('Informe o percentual da taxa da ação comprada: ')

total_stock_exchange_purchased = (float(stock_exchange_purchased_amount) * float(stock_exchange_purchased_price)) * ((float(stock_exchange_purchased_tax) / 100) + 1)
total_stock_exchange_purchased_tax = ((float(stock_exchange_purchased_amount) * float(stock_exchange_purchased_price)) * ((float(stock_exchange_purchased_tax) / 100)))
total_stock_exchange_sold_tax = ((float(stock_exchange_sold_amount) * float(stock_exchange_sold_price)) * ((float(stock_exchange_sold_tax) / 100)))
total_stock_exchange_sold = (float(stock_exchange_sold_amount) * float(stock_exchange_sold_price)) - float(total_stock_exchange_sold_tax)
total_stock_exchange = float(total_stock_exchange_purchased) - float(total_stock_exchange_sold)

print('\nO valor total gasto na compra de ações foi: $ ' + str(total_stock_exchange_purchased))
print('\nO valor pago em taxa durante a compra foi: $ ' + str(total_stock_exchange_purchased_tax))
print('\nO valor total ganho na venda de ações foi: $ ' + str(total_stock_exchange_sold))
print('\nO valor pago em taxa durante a venda foi: $ ' + str(total_stock_exchange_sold_tax))
print('\nO valor da diferença total entre a compra e a venda de ações foi: $ ' + str(total_stock_exchange))