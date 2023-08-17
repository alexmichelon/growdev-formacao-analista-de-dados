'''
Utilize o arquivo ‘alunos.csv’ em anexo para realização dos exercícios.
1) Somando, separadamente, as notas do primeiro semestre e do segundo
semestre. Qual semestre obteve o maior somatório?
2) Qual foi o percentual de alunos que utilizaram e que não utilizaram a
monitoria?
3) Qual foi a média de faltas dos alunos do colégio Pedro II?
4) A média de notas do primeiro semestre foi maior entre alunos do 1 ano ou 3
ano?
5) De todos os alunos que obtiveram média final maior ou igual a sete, quantos
ultrapassaram 15 faltas?
'''

from functions_utils import open_csv_file, convert_data_dict_list

header, data = open_csv_file('dados/alunos.csv', 'r')

list_keys = {'nome': str, 'ano': int, 'escola': str, 'nota_semestre_1': float, 'nota_semestre_2': float, 'faltas': int, 'nota_exame': float, 'monitoria': bool}

students = convert_data_dict_list(data, list_keys)

#ver dados notas primeiro semestre ano 1 e ano 3
students_age_one = 0
students_age_three = 0
first_semester_grades_age_one = 0
first_semester_grades_age_three = 0
average_first_semester_grades_age_one = 0
average_first_semester_grades_age_three = 0

for student in students:
    if(student['ano'] == 1):
        students_age_one += 1
        first_semester_grades_age_one += student['nota_semestre_1']
    elif(student['ano'] == 3):
        students_age_three += 1
        first_semester_grades_age_three += student['nota_semestre_1']

average_first_semester_grades_age_one = first_semester_grades_age_one / students_age_one
average_first_semester_grades_age_three = first_semester_grades_age_three / students_age_three

if(average_first_semester_grades_age_one > average_first_semester_grades_age_three):
    print(f'Para as notas do primeiro semestre, a média do 1º ano ({average_first_semester_grades_age_one:.2f}) foi maior que a do 3º ({average_first_semester_grades_age_three:.2f}).')
else:
    print(f'Para as notas do primeiro semestre, a média do 3º ano ({average_first_semester_grades_age_three:.2f}) foi maior que a do 1º ({average_first_semester_grades_age_one:.2f}).')