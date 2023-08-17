def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input('\nEntrada Inválida!\n' + order + '\n')
    value = convert_coma_point(value)
    return float((value))

   
print('Bem vindo ao sistema Cálculo de Nota!\n')

grade_1 = validate_number('Informe a primeira nota: \n')
grade_2 = validate_number('Informe a segunda nota: \n')
grade_3 = validate_number('Informe a terceira nota: \n')

percent_grade_1 = validate_number('Informe o peso (em percentual) da primeira nota para o cálculo da média final: \n')
percent_grade_2 = validate_number('Informe o peso (em percentual) da segunda nota para o cálculo da média final: \n')
percent_grade_3 = validate_number('Informe o peso (em percentual) da terceira nota para o cálculo da média final: \n')

total_percent = float(percent_grade_1) + float(percent_grade_2) + float(percent_grade_3)

while(total_percent != 100.00):
    print('\nA soma dos percentuais informados não somam 100%.\n')
      
    percent_grade_1 = validate_number('Informe o peso (em percentual) da primeira nota para o cálculo da média final: \n')
    percent_grade_2 = validate_number('Informe o peso (em percentual) da segunda nota para o cálculo da média final: \n')
    percent_grade_3 = validate_number('Informe o peso (em percentual) da terceira nota para o cálculo da média final: \n')

    total_percent = float(percent_grade_1) + float(percent_grade_2) + float(percent_grade_3)

average_grade = (((float(grade_1) * float(percent_grade_1)) + 
                (float(grade_2) * float(percent_grade_2)) + 
                float(grade_3) * float(percent_grade_3)) 
                / 100)

print('\nA média final do aluno é: ' + str(average_grade))

