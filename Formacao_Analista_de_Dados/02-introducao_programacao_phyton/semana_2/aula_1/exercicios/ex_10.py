'''
10)Após construir o programa anterior, crie mais duas versões dele para prever
as seguintes situações:
a) Um aluno pode ficar em recuperação se possuir frequência suficiente
(superior a 75%) e média superior a 5 mas inferior a 7;
b) Caso um aluno reprove por média e faltas, sua situação deve ser
   “Reprovado por Média e Faltas” (ao invés de simplesmente
   “Reprovado por Faltas” como antes).
'''

#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float positivos menores que 10
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()) or (float(convert_coma_point(value)) > 10):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    value = convert_coma_point(value)
    return float((value))

#Valida se o String informado pelo usuário é um inteiro positivo
def validate_integer(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    return int(value)

print('\nBem vindo ao Sistema Situação do Aluno!!\n')

grade_1 = validate_number('\nInforme a nota do 1º bimestre do aluno: ')
grade_2 = validate_number('Informe a nota do 2º bimestre do aluno: ')
grade_3 = validate_number('Informe a nota do 3º bimestre do aluno: ')
grade_4 = validate_number('Informe a nota do 4º bimestre do aluno: ')

average = (grade_1 + grade_2 + grade_3 + grade_4) / 4

total_classes = validate_integer('Informe o número total de aulas do ano: ')
miss_classes  = validate_integer('Informe o número total de faltas do aluno nas aulas do ano: ')
percent_miss_classes = ((miss_classes * 100) / total_classes)

if(percent_miss_classes > 25) and (average <= 5):
   print(f'\nAluno REPROVADO POR MÉDIA E FALTAS. Média final: {average:.2f}')
elif(percent_miss_classes > 25):
    print(f'\nAluno REPROVADO POR FALTAS.')
elif(average < 5):
   print(f'\nAluno REPROVADO POR MÉDIA. Média final: {average:.2f}')
elif(average > 5) and (average < 7):
   print(f'\nAluno EM RECUPERAÇÃO.')
else:
   print(f'\nAluno APROVADO. Média final: {average:.2f}')