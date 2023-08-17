'''
13)Construa um programa que, a partir do valor do comprimento dos três lados
de um triângulo, classifique-o em equilátero, isósceles ou escaleno. Lembre,
um triângulo é equilátero quando o comprimento de todos os seus lados for
igual, é isósceles quando apenas um dos lados tiver comprimento diferente e
é escaleno quando todos os lados tiverem comprimentos diferentes dos
demais lados.
'''

#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float positivos
def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    value = convert_coma_point(value)
    return float((value))

print('\nBem vindo ao Sistema Qual é o Tipo do Triângulo!\n')

side_1 = validate_number('Informe o valor do lado 1 do triângulo: ')
side_2 = validate_number('Informe o valor do lado 2 do triângulo: ')
side_3 = validate_number('Informe o valor do lado 3 do triângulo: ')

if (side_1 == side_2) and (side_2 == side_3):
    print('\nÉ um triângulo EQUILÁTERO.')
elif(side_1 != side_2 ) and (side_1 != side_3) and (side_2 != side_3):
    print('\nÉ um triângulo ESCALENO.')
else:
   print('\nÉ um triângulo ISÓSCELES')