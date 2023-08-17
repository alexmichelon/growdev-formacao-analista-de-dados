
anual_profit_percentage = 0.23

def validate_value():
    value = input('Informe o valor total de vendas projetado para o ano:\n')
    while(not value.replace(',','').replace('.','').isdecimal()):
        value = input('\nEntrada inválida!\n'
                      'Informe o valor total de vendas projetado para o ano:\n')
    value = value.replace(',', '.')     
    return value

print('\nSeja bem vindo ao Cálculo do lucro sobre o total de vendas projetado para o ano!!!\n')

total_projected_sales_value = validate_value()
profit = (float(total_projected_sales_value) * float(anual_profit_percentage))

print('\nCom o valor total de vendas \n$'+ str(total_projected_sales_value) 
       + '\nprojetado para ano, o lucro obtido neste período será de \n$' + str(float(round(profit,2))))