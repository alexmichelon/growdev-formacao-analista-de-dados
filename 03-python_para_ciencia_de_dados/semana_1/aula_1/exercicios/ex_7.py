'''
7) Crie um programa que calcule a folha de pagamento de uma empresa,
conforme as instruções a seguir:

a) O usuário pode inserir continuamente os nomes dos empregados até
que escolha a opção de finalizar o informe de dados;
b) Após informar o nome de cada empregado, o usuário deverá informar
o valor do salário da hora trabalhada desse empregado e quantas
horas ele trabalhou;
c) O programa deve calcular o salário bruto de cada empregado, a
percentagem de imposto retido na fonte (com base na tabela abaixo),
o valor do imposto retido na fonte e o salário líquido (pagamento bruto
menos imposto retido na fonte);
d) Depois que o usuário inserir os dados do último empregado, o
programa deve exibir o salário bruto, salário líquido, percentual de
imposto e valor do imposto para cada funcionário;
e) Por último, o programa deve exibir a soma de todas as horas
trabalhadas, o total da folha de pagamento bruta, o total de imposto e
a folha de pagamento líquida total.

Percentuais de imposto
Salário bruto Percentual
Até R$ 2.999,99 = 10%
Entre R$ 3.000,00 e R$ 5.499,99 = 13%
Entre R$ 5.500,00 e R$ 7.999,99 = 16%
Acima de R$ 8.000,00 = 20%
'''

import functions_utils as func

list_salary_employee = []
employee_name = ''
employee_amount_hours_worked = 0
employee_price_hours_worked = 0
employee_gross_salary = 0
employee_salary_tax = 0
employee_total_tax = 0
employee_net_salary = 0
all_hours_worked = 0
total_gross_payroll = 0
total_tax_payroll = 0
total_net_payroll = 0

#verifica, de acordo com o salário bruto, o percentual do imposto a ser descontado do salário
def calculate_percentual_tax(employee_amount_hours_worked, employee_price_hours_worked):
    employee_gross_salary = employee_amount_hours_worked * employee_price_hours_worked
    if(employee_gross_salary <= 2999.99):
        employee_salary_tax = 0.1
    elif(employee_gross_salary >= 3000) and (employee_gross_salary <= 5499.99):
        employee_salary_tax = 0.13
    elif(employee_gross_salary >= 5500) and (employee_gross_salary <= 7999.99):
        employee_salary_tax = 0.16
    else:
        employee_salary_tax = 0.2
    return employee_salary_tax

print('\nBem vindo ao sistema Folha de Pagamento!!!\n')

option = 'S'

while(option != 'N'):
    employee_name = input('Informe o nome do empregado: ')

    #salário do empregado é criado dentro da lista de salários:
    #employee_name = nome do empregado
    #employee_amount_hours_worked = quantidade de horas trabalhadas do empregado
    #employee_price_hours_worked = valor da hora de trabalho do empregado
    #employee_gross_salary = salário bruto do empregado
    #employee_salary_tax = percentaual de imposto do empregado
    #employee_total_tax = total de desconto de imposto da folha de salário do empregado
    #employee_net_salary = salário líquido do empregado
    list_salary_employee.append([employee_name, employee_amount_hours_worked, employee_price_hours_worked, employee_gross_salary, employee_salary_tax, employee_total_tax, employee_net_salary])

    #opção para continuar informando nomes de empregados ou sair
    option = func.validate_option('Deseja informar novo empregado? S/N\n', '"S","N","s","n"').upper()


for i in range(len(list_salary_employee)):
    #atribui número de horas trabalhadas informada
    list_salary_employee[i][1] = func.validate_float_positive(f'Informe a quantidade de horas trabalhadas pelo empregado {list_salary_employee[i][0]}: ')
    #atribui valor da hora trabalhada informada
    list_salary_employee[i][2] = func.validate_float_positive(f'Informe o valor da hora trabalhada para o empregado {list_salary_employee[i][0]}: ')
    #atribui salário bruto do empregado
    list_salary_employee[i][3] = (list_salary_employee[i][1] * list_salary_employee[i][2])
    #atribui percentual de imposto considerando o salário
    list_salary_employee[i][4] = calculate_percentual_tax(list_salary_employee[i][1], list_salary_employee[i][2])
    #atribui valor total de imposto descontado
    list_salary_employee[i][5] = (list_salary_employee[i][3] * list_salary_employee[i][4])
    #atribui valor do salário líquido (bruto - total de imposto)
    list_salary_employee[i][6] = list_salary_employee[i][3] - list_salary_employee[i][5]

#detalhes da folha de cada empregado
print('\n\n\n--------FOLHA DE PAGAMENTO-------\n')
for i in range(len(list_salary_employee)):
    print(f'Empregado: {list_salary_employee[i][0]}')
    print(f'Quantidade horas trabalhadas: {list_salary_employee[i][1]:.0f} horas')
    print(f'Valor da hora trabalhada: R$ {list_salary_employee[i][2]:.2f}')
    print(f'Salário Bruto: R$ {list_salary_employee[i][3]:.2f}')
    print(f'Percentual imposto: {list_salary_employee[i][4] * 100:.2f}%')
    print(f'Valor imposto: R$ {list_salary_employee[i][5]:.2f}')
    print(f'Salário Líquido: R$ {list_salary_employee[i][6]:.2f}\n')

for i in range(len(list_salary_employee)):
    #Soma todas as horas trabalhadas de todos os empregados
    all_hours_worked += list_salary_employee[i][1]
    #Total folha de pagamento bruta de todos os empregados
    total_gross_payroll += list_salary_employee[i][3]
    #Total imposto folha de pagamento de todos os empregados
    total_tax_payroll += list_salary_employee[i][5]
    #Total folha de pagamento liquida de todos os empregados
    total_net_payroll += list_salary_employee[i][6]

#imprime o obtido no último laço: informações sobre todos os empregados
print(f'----------\nTotal de horas trabalhadas: {all_hours_worked:.2f} horas')
print(f'----------\nTotal folha de pagamento bruta: R$ {total_gross_payroll:.2f}')
print(f'----------\nTotal de imposto: R$ {total_tax_payroll:.2f}')
print(f'----------\nTotal folha de pagamento líquida: R$ {total_net_payroll:.2f}')