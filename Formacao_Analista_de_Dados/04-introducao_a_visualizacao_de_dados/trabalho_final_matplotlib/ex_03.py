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

from functions_utils import open_csv_file, convert_data_dict_list, list_dict_group_by_values_two_keys, list_dict_values_key, list_dict_count_values_key
import matplotlib.pyplot as plt

header, data = open_csv_file('dados/alunos.csv', 'r')

list_keys = {'nome': str, 'ano': int, 'escola': str, 'nota_semestre_1': float, 'nota_semestre_2': float, 'faltas': int, 'nota_exame': float, 'monitoria': bool}

students = convert_data_dict_list(data, list_keys)

missed_by_school = {}
students_by_school = {}
average_missed_by_school = {}
schools = []

for student in students:
    missed_by_school = list_dict_group_by_values_two_keys(missed_by_school, student, 'escola', 'faltas')    
    students_by_school = list_dict_count_values_key(students_by_school, student, 'escola')

print(missed_by_school)
print(students_by_school)

schools = list_dict_values_key(students, 'escola')
x = []
y = []

for i in range (len(schools)):
    average = (missed_by_school.get(schools[i]) / students_by_school.get(schools[i]))
    average_missed_by_school.setdefault(schools[i], average)
    x.append(schools[i].replace(' ', '\n')) 
    y.append(average)

for school in schools:
    average = missed_by_school[school] / students_by_school[school]
    print(f'Escola {school}: {average}')

print(average_missed_by_school.values())
print(schools)

plt.plot(x, y, 'o-g', color='#25BE7B')

for a, b in zip(x, y):
    label = "{:.2f}".format(b)
    plt.annotate(label, (a, b), textcoords="offset points", xytext=(0,10), ha="center")

plt.xlabel('Escolas\n')
plt.ylabel('Média de Faltas')
plt.title('Média de Faltas por Aluno')
plt.show()