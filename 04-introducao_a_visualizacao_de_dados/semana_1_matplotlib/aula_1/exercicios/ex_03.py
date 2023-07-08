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

missed_classes = 0
students_of_school = 0

for student in students:
    if(student['escola'] == 'Pedro II'):
        students_of_school += 1
        missed_classes += student['faltas']

print(f'Média de faltas por aluno escola Pedro II: {missed_classes / students_of_school:.2f}')