'''
2) Faça um programa que peça o nome e as duas notas de 5 alunos, calcule a
média das notas e armazene nome e média cada uma em uma lista, ao final
imprima o nome e o número de alunos com média maior ou igual a 7.0.
'''

import functions_utils as func

names = []
averages = []
total_iterations = 5
average_grade = 7
none = 1

print('\nBem vindo ao sistema Alunos com média igual ou maior que 7.0!!!\n')

for i in range(total_iterations):
    name = input('\nInforme o nome do aluno: ')
    grade_1 = func.validate_float_positive_less10(f'Informe a primeira nota do aluno {name}: ')
    grade_2 = func.validate_float_positive_less10(f'Informe a segunda nota do aluno {name}: ')
    average = (grade_1 + grade_2) / 2
    names.append(name)
    averages.append(average)

for i in range(total_iterations):
    if(averages[i] >= average_grade):
        print(f'O aluno: {names[i]} possui média {averages[i]:.2f} maior ou igual a 7.0.')
    else:
        none += 1
    if(none == total_iterations):
        print('\nNenhum aluno possui média igual ou superior a 7.0.')