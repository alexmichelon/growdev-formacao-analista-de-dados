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

from functions_utils import open_csv_file, convert_data_dict_list, sum_column_values_whitout_conditions
import matplotlib.pyplot as plt

header, data = open_csv_file('alunos.csv', 'r')

list_keys = {'nome': str, 'ano': int, 'escola': str, 'nota_semestre_1': float, 'nota_semestre_2': float, 'faltas': int, 'nota_exame': float, 'monitoria': bool}

students = convert_data_dict_list(data, list_keys)

grades_first_semester = sum_column_values_whitout_conditions(students, 'nota_semestre_1')
grades_second_semester = sum_column_values_whitout_conditions(students, 'nota_semestre_2')

if(grades_first_semester > grades_second_semester):
    print(f'Somatório das notas do primeiro semestre: {grades_first_semester:.2f} foi maior que o somatório das notas do segundo semestre: {grades_second_semester:.2f}.')
else:
    print(f'Somatório das notas do segundo semestre: {grades_second_semester:.2f} foi maior que o somatório das notas do primeiro semestre: {grades_first_semester:.2f}.')

x = ['1º Semestre', '2º Semestre']
y = [grades_first_semester, grades_second_semester]
bar_colors = ['#25BE7B', 'tab:red']
a = plt.bar(x, y, color=bar_colors, width=0.6, align='center')
plt.axis(ymin=20000, ymax=30000)
plt.xticks(x)
plt.title('Somatórios das notas dos semestres')
plt.ylabel('Somatório')
plt.xlabel('Semestre')
plt.bar_label(a, label_type='edge', fmt='%.2f', padding=2)
plt.show()