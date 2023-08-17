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

aproved_students_whit_more_than_15_missed_classes = 0

for student in students:
    average = (student['nota_semestre_1'] + student['nota_semestre_2']) / 2
    if(average >= 7):        
        if(student['faltas'] > 15):
            aproved_students_whit_more_than_15_missed_classes += 1

print(f'Houveram {aproved_students_whit_more_than_15_missed_classes} alunos aprovados (média final maior ou igual a 7) com mais de 15 faltas.')