'''
15)Faça um programa que leia as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição
de conceitos obedece à tabela abaixo:
    Média de Aproveitamento
    Entre 9.0 e 10.0 Conceito A
    Entre 7.5 e 8.9 = B
    Entre 6.0 e 7.4 = C
    Entre 4.0 e 5.9 = D
    Entre 0 e 3.9 = E
O programa deve mostrar na tela as notas, a média, o conceito
correspondente e a mensagem:
    a) APROVADO se o conceito for A, B ou C.
    b) REPROVADO se o conceito for D ou E.
'''

#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float positivos menores que 10
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()) or (float(convert_coma_point(value)) > 10):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    value = convert_coma_point(value)
    return float((value))

print('\nBem vindo ao Sistema Conceito do Aluno!!\n')

grade_1 = validate_number('Informe a primeira nota do aluno: ')
grade_2 = validate_number('Informe a segunda nota do aluno: ')

average = (grade_1 + grade_2) / 2

if((average <= 10) and (average >= 9)):
    print(f'\nAluno com notas {grade_1:.2f} e {grade_2:.2f}, média parcial de {average:.2f}. O aluno está APROVADO com conceito é A.')
elif((average < 9) and (average >= 7.5)):
    print(f'\nAluno com notas {grade_1:.2f} e {grade_2:.2f}, média parcial de {average:.2f}. O aluno está APROVADO com conceito é B.')
elif((average < 7.5) and (average >= 6)):
    print(f'\nAluno com notas {grade_1:.2f} e {grade_2:.2f}, média parcial de {average:.2f}. O aluno está APROVADO com conceito é C.')
elif((average < 6) and (average >= 4)):
    print(f'\nAluno com notas {grade_1:.2f} e {grade_2:.2f}, média parcial de {average:.2f}. O aluno está REPROVADO com conceito é D.')
else:
    print(f'\nAluno com notas {grade_1:.2f} e {grade_2:.2f}, média parcial de {average:.2f}. O aluno está REPROVADO com conceito é E.')