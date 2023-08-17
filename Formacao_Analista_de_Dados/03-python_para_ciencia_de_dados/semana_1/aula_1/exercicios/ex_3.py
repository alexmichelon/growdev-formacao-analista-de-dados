'''
3) Modifique o programa anterior para que utilize apenas uma lista e em cada
posição da lista armazene um dicionário com o nome e a média.
'''

import functions_utils as func

names = []
total_iterations = 3
average_grade = 7
none = 0

print('\nBem vindo ao sistema Alunos com médis igual ou maior que 7.0!!!\n')

for i in range(total_iterations):
    name = input('\nInforme o nome do aluno: ')
    grade_1 = func.validate_float_positive_less10(f'Informe a primeira nota do aluno {name}: ')
    grade_2 = func.validate_float_positive_less10(f'Informe a segunda nota do aluno {name}: ')
    average = (grade_1 + grade_2) / 2
    names.append({'nome': name, 'media' : average})

for i in range(total_iterations):
    if(names[i]['media'] >= average_grade):
        print(f"\nO aluno: {names[i]['nome']} possui média {names[i]['media']} maior ou igual a 7.0.")
    else:
        none += 1
    if(none == total_iterations):
        print('\nNenhum aluno possui média igual ou superior a 7.0.')