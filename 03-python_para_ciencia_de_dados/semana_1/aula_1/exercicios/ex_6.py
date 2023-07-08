'''
6) Crie um programa que leia continuamente a altura e o sexo de uma lista de
pessoas salvando todas as informações em listas, até que uma altura
negativa seja fornecida. Ao final, sabendo que a média de altura para as
mulheres brasileiras é de 1.60m e a dos homens brasileiros é de 1.73m,
escreva as seguintes informações:
a) quantas mulheres da lista estão acima da média nacional de altura
para mulheres, e quantas estão abaixo;
b) quantos homens da lista estão acima da média nacional de altura para
homens, e quantos estão abaixo.
'''

import functions_utils as func

people = []
sex = 0
height = 0
option = 'S'
average_woman_heigh = 1.6
average_man_heigh = 1.73
amount_woman_above_average = 0
amount_man_above_average = 0
amount_man_below_average = 0
amount_woman_below_average = 0

print('\nBem vindo ao sistema de média de alturas de homens e mulheres!!!\n'
      'Serão classificados homens e mulheres considerando a média nacional:\n'
      f'- {average_woman_heigh} m para mulheres\n'
      f'- {average_man_heigh} m para homens.\n'
      'Para sair, digite uma altura negativa.\n')

while True:
    #espera o usuário informar o sexo desejado (inteiro 1 ou 0 positivo)
    sex = int(input('Informe o sexo da pessoa:\n'
                '0 - Homem\n'
                '1 - Mulher\n'))

    #valida o sexo informado se foi digitado 0-homem ou 1-mulher, caso algo de diferente tenha sido informado cai dentro do laço
    while(sex != 0) and ( sex != 1):
        #espera o usuário informar o sexo desejado (inteiro 1 ou 0 positivo)
        sex = int(input('\nOpção Inválida!\nInforme o sexo da pessoa:\n'
            '0 - Homem\n'
            '1 - Mulher\n'))
    
    #espera o usuário informar a altura desejada (float positivo)
    height = func.validate_float_negative('Informe a altura da pessoa: \n')

    #se uma altura negativa é informada, encerra a informação de novas pessoas
    if(height < 0):
        break
    
    #adiciona uma tupla (sexo e altura) na lista: 1 tupla com dois valores forma uma posição da lista
    people.append((sex, height))

#verifica se alguma informação foi informada e adicionada na lista
if(len(people) > 0):
    #verifica cada pessoa (tupla) dentro da lista
    for i in range(len(people)):
        for j in range(1,2):
            #verifica se é homem
            if(people[i][0] == 0):
                #verifica se a altura é maior que a média informada para homens
                if(people[i][j] > average_man_heigh):
                    #itera contador de homens com altura acima da média
                    amount_man_above_average += 1
                else:
                    #itera contador de homens com altura abaixo da média
                    amount_man_below_average += 1
            else:
                #verifica se a altura é maior que a média informada para mulheres
                if(people[i][j] > average_woman_heigh):
                    #itera contador de mulheres com altura abaixo da média
                    amount_woman_above_average += 1
                else:
                    #itera contador de mulheres com altura abaixo da média
                    amount_woman_below_average += 1
            
    print(f'Dentre os informados, há {amount_woman_above_average} mulhere(s) com altura acima da média nacional: {average_woman_heigh}m.')
    print(f'Dentre os informados, há {amount_woman_below_average} mulhere(s) com altura abaixo da média nacional: {average_woman_heigh}m.')
    print(f'Dentre os informados, há {amount_man_above_average} homem(s) com altura acima da média nacional: {average_man_heigh}m.')
    print(f'Dentre os informados, há {amount_man_below_average} homem(s) com altura abaixo da média nacional: {average_man_heigh}m.')
else:
    #caso lista vazia (nenhum valor informado)
    print('A lista está vazia: Nenhum dado de pessoa informado!')
