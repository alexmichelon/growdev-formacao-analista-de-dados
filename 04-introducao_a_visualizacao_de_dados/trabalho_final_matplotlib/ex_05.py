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
import numpy as np

header, data = open_csv_file('dados/alunos.csv', 'r')

list_keys = {'nome': str, 'ano': int, 'escola': str, 'nota_semestre_1': float, 'nota_semestre_2': float, 'faltas': int, 'nota_exame': float, 'monitoria': bool}

students = convert_data_dict_list(data, list_keys)

aproved_students_whit_more_than_15_missed_classes = 0
aproved_students = 0
total_students = 0

for student in students:
    average = (student['nota_semestre_1'] + student['nota_semestre_2']) / 2
    if(average >= 7):        
        aproved_students += 1
        if(student['faltas'] > 15):
            aproved_students_whit_more_than_15_missed_classes += 1
    total_students += 1

reproved_students = total_students - aproved_students

print(f'Houveram {aproved_students_whit_more_than_15_missed_classes} alunos aprovados (média final maior ou igual a 7) com mais de 15 faltas.')

percentage_aproved_students = ((aproved_students - aproved_students_whit_more_than_15_missed_classes) * 100) / total_students
percentage_aproved_students_whit_more_than_15_missed_classes = (aproved_students_whit_more_than_15_missed_classes * 100) / total_students
percentage_reproved_students = (reproved_students * 100) / total_students

print(percentage_aproved_students)
print(percentage_aproved_students_whit_more_than_15_missed_classes)
print(percentage_reproved_students)

x = [percentage_aproved_students, percentage_aproved_students_whit_more_than_15_missed_classes, percentage_reproved_students]
colors = ['#194B7B', '#EE6908', '#1b7a9a']
labels = ['Média suficiente', 'Mais de 15 faltas', 'Reprovados']

plt.gca().axis("equal")
wedges, texts, autotexts = plt.pie(x, explode=None, colors=colors, autopct='', radius=1, pctdistance=0.6, labeldistance=1.1, startangle=45, counterclock=True)

arrowprops=dict(arrowstyle="-", color= "gray", facecolor="gray", connectionstyle="angle,angleA=0,angleB=90")
kw = dict(xycoords='data',textcoords='data',arrowprops=arrowprops, zorder=0)
adjust_a = 1.8
ha = "right"

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    b = np.sin(ang/180.*np.pi)
    a = 1.35*np.sign(np.cos(ang/180.*np.pi))
    if a < 0 : 
        adjust_a = -1.8
        ha="left"
    kw1 = dict(xycoords='data',textcoords='data', zorder=0, ha=ha)
    plt.gca().annotate(labels[i], xy=(0, 0), xytext=(adjust_a, b+0.01), **kw1)   
    plt.gca().annotate("", xy=(0, 0), xytext=(adjust_a, b), **kw)
    plt.gca().annotate("{:.2f}%".format(x[i]), xy=(0, 0), xytext=(adjust_a, b-0.108), color="gray" , **kw1)

plt.title('Points Scored', loc='left')
plt.show()
