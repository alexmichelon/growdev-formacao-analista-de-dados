import matplotlib as pl
import seaborn as sns
import pandas as pd


print('Semana 3\n'

'A temperatura máxima do dia em uma cidade foi anotada durante'
'vinte e um dias. Os dados foram tabulados em uma matriz, na qual as'
'linhas correspondem a semana e colunas aos dias, sendo que a'
'coluna 1 corresponde ao domingo. Os dados estão em °C:\n'

'[30 32 31.5 31 33 34 33]\n'
'[32 30 28 29 30.5 31 29]\n'
'[33 34 35 35 34.5 34 33]\n\n' 

'a) Organize uma tabela de frequência para as classes.\n'
'b) Para cada semana, faça um gráfico de linha, para acompanhar a evolução da temperatura.\n'
'c) Calcule a média de toda a série.\n'
'd) Calcule a média para cada semana.\n'
'e) Obter o box-plot para toda série e para cada semana.\n')

dia_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
semana_1 = [30,32,31.5,31,33,34,33]
semana_2 = [32,30,28,29,30.5,31,29]
semana_3 = [33,34,35,35,34.5,34,33]

#a
print(semana_1)
print(semana_2)
print(semana_3)

#b
x = semana_1
x = pd.DataFrame(x, columns=dia_semana)
x