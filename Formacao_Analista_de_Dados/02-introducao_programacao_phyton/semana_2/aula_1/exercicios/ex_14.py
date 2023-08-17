'''
14)As Organizações XTC resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calcula os
reajustes. Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
   a) salários até R$ 280,00 (incluindo): aumento de 20%
   b) salários entre R$ 280,00 e R$ 700,00: aumento de 15%
   c) salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
   d) salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado informe na tela:
   a) o salário antes do reajuste;
   b) o percentual de aumento aplicado;
   c) o valor do aumento;
   d) o novo salário, após o aumento.
'''

#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float positivos
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    value = convert_coma_point(value)
    return float((value))

print('\nBem vindo ao Sistema Cálculo de Reajuste de Salário!\n')

employee_salary_old = validate_number('Informe o valor do salário do colaborador: ')
increase_percentual = 0
increase_value = 0
employee_salary_new = 0

if(employee_salary_old <= 280):
   increase_percentual = 0.20
elif(employee_salary_old > 280) and (employee_salary_old <= 700):
   increase_percentual = 0.15
elif(employee_salary_old > 700) and (employee_salary_old <= 1500):
   increase_percentual = 0.10
else:
   increase_percentual = 0.05

increase_value = employee_salary_old * increase_percentual
employee_salary_new = employee_salary_old + increase_value

print(f'O salário do colaborador antes do reajuste era de: R$ {employee_salary_old:.2f}.')
print(f'O percentual de aumento aplicado foi de {increase_percentual*100:.2f}%.')
print(f'O valor do aumento foi de: R$ {increase_value:.2f}.')
print(f'O salário do colaborador após o reajuste foi de: R$ {employee_salary_new:.2f}.')