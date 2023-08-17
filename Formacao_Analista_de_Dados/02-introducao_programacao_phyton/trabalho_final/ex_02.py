'''2) Escreva um programa em Python que receba o valor do
faturamento de uma loja e calcule o lucro sobre esse faturamento,
sabendo que o lucro é 32% do total do faturamento. Além disso uma
taxa de imposto é cobrada sobre o total do lucro.
a) O imposto é de 12% caso o faturamento seja abaixo de 5000.
b) O imposto é de 18% caso o faturamento seja igual ou superior
a 5000 e menor que 15000.
c) O imposto é de 30% caso o faturamento seja de 15000 ou
superior.
Informe qual é o total do lucro, o valor do imposto cobrado e qual o
total do valor restante após o pagamento do imposto.'''

import functions_utils as func

print('\nBem vindo ao sistema Cálculo do Faturamento dqa Loja!!!\n')

invoicing = func.validate_float_positive('Informe o valor (em R$) do faturamento da loja: ')

percent_profit = 0.32

profit = invoicing * percent_profit

if(invoicing < 5000):
    tax = 0.12
elif(invoicing >= 5000) and (invoicing < 15000):
    tax = 0.18
else:
    tax = 0.3

tax_charged = profit * tax
total_value_whitout_tax = profit - tax_charged


print(f'\nO valor total do lucro é R$ {profit:.2f} ({percent_profit*100:.0f}% do faturamento).')
print(f'O valor do imposto cobrado é R$ {tax_charged:.2f} ({tax*100:.0f}% do lucro).')
print(f'O valor total descontado o imposto é R$ {total_value_whitout_tax:.2f}.')