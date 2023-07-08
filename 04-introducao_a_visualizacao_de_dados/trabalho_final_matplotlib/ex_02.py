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

total_students = 0
students_monitoring_true = 0
students_monitoring_false = 0

for student in students:
    if(student['monitoria'] == True):
        students_monitoring_true += 1
    else:
        students_monitoring_false += 1
    total_students += 1

whit_monitoring = students_monitoring_true * 100 / total_students
whitout_monitoring = students_monitoring_false * 100 / total_students

print(f'Percentual de alunos que utilizaram monitoria: {whit_monitoring:.2f}%.')
print(f'Percentual de alunos que não utilizaram monitoria: {whitout_monitoring:.2f}%.')

x = [whit_monitoring, whitout_monitoring]
colors = ['#BAAAC3', '#8FBB78', '#59125C', 'white']
labels = ['Usaram monitoria', 'Não usaram monitoria']
plt.pie(x, explode=None, labels=labels, colors=colors, autopct='%.2f%%', pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=0.75, counterclock=True, wedgeprops={"linewidth": 3, "edgecolor": "white"}, textprops=None, center=(0, 0), frame=False, rotatelabels=False, normalize=True, hatch=None, data=None)
plt.title('Alunos que utilizaram/não utilizaram monitoria')
plt.show()