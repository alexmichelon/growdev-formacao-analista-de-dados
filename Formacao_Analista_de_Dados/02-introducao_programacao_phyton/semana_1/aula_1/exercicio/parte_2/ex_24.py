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

 
print('\nBem vindo ao sistema Cálculo de Nota!\n')

grade_1 = validate_number('Informe a primeira nota: ')
grade_2 = validate_number('Informe a segunda nota: ')
grade_3 = validate_number('Informe a terceira nota: ')

percent_grade_1 = 20
percent_grade_2 = 30
percent_grade_3 = 50

average_grade = (((float(grade_1) * float(percent_grade_1)) + 
                (float(grade_2) * float(percent_grade_2)) + 
                float(grade_3) * float(percent_grade_3)) 
                / 100)

print('A média final do aluno é: ' + str(average_grade))
