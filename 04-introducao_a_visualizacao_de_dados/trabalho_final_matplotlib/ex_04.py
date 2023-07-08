'''
Para cada questão da lista de exercícios da última semana, crie uma representação
gráfica para exibir os resultados de uma forma mais agradável. Utilize a biblioteca
matplotlib para tal propósito.
A seguir estão as descrições dos exercícios da semana passada. Se você já
desenvolveu eles basta utilizar o mesmo código adicionando a representação
gráfica dos resultados.

1) Descrição: somando, separadamente, as notas do primeiro semestre e do
segundo semestre. Qual semestre obteve o maior somatório?
a) Para esse exercício crie um gráfico de colunas/barras para representar
os somatórios das notas de ambos os semestres.

2) Qual foi o percentual de alunos que utilizaram e que não utilizaram a
monitoria?
a) Crie um gráfico de pizza para representar os percentuais.

3) Qual foi a média de faltas dos alunos do colégio Pedro II?
a) Modifique esse exercício para calcular a média de alunos de cada
colégio, e exiba os resultados como um gráfico de linha.

4) A média de notas do primeiro semestre foi maior entre alunos do 1 ano ou 3
ano?
a) Exiba as médias dos alunos como um gráfico de barras/colunas.

5) De todos os alunos que obtiveram média final maior ou igual a sete, quantos
ultrapassaram 15 faltas?
a) Crie um gráfico de pizza que representa o total de alunos, a
quantidade desses alunos com média final maior ou igual a 7 e desses
quantos ultrapassaram as 15 faltas. Ex. 100 alunos, 80 deles ficaram
com nota igual ou superior a 7 e 25 desses ficaram com mais de 15
faltas. O gráfico deverá ser então conforme o gráfico a seguir.
'''

from functions_utils import open_csv_file, convert_data_dict_list
import matplotlib.pyplot as plt

header, data = open_csv_file('alunos.csv', 'r')

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

x = ['1º ano', '3º ano']
y = [average_first_semester_grades_age_one, average_first_semester_grades_age_three]
bar_colors = ['tab:blue', 'tab:red']
a = plt.bar(x, y, color=bar_colors)
plt.title('Média de notas do 1º e 3º ano')
plt.xlabel('Ano')
plt.ylabel('Média de Notas')
plt.axis(ymin=4.5, ymax=5.5)
plt.bar_label(a, label_type='edge', fmt='%.2f', padding=2)
plt.show()