'''
6) Em uma eleição presidencial existem dois candidatos. Os votos são
informados através de códigos. Os dados utilizados para a contagem dos
votos obedecem à seguinte codificação:
a) 1,2 = voto para os respectivos candidatos
b) 3 = voto nulo
c) 4 = voto em branco;
Elabore um programa que leia o código de votação de 5 eleitores. Calcule
e escreva:
a) total de votos para cada candidato
b) total de votos nulos
c) total de votos em branco
'''

import functions_utils as func

vote = '1'
vote_candidate_A = 0
vote_candidate_B = 0
vote_null = 0
vote_blank = 0


print('\nSeja bem vindo ao Sistema Eleição Presidencial!!\n')

for i in range (5): 
    vote = func.validate_integer_positive_comparision('Informe seu voto:\n'
                                                '1 - Candidato A\n'
                                                '2 - Candidato B\n'
                                                '3 - Voto Nulo\n'
                                                '4 - Voto em Branco\n'
                                                '5 - Fazer Apuração dos Votos\n'
                                                '0 - Sair\n', '"0","1","2","3","4","5"')

    if(vote == '0'):
        break
    elif(vote == '1'):
        vote_candidate_A += 1
    elif(vote == '2'):
        vote_candidate_B += 1
    elif(vote == '3'):
        vote_null += 1
    elif(vote == '5'):
        if(vote_candidate_A == 0) and (vote_candidate_B == 0) and (vote_null == 0) and (vote_blank == 0):
            print('Nenhum voto computado!\n')
            pass
        else:
            print('\n-----Total de votos:-----\n'
            f'Candidato A: {vote_candidate_A} votos.\n'
            f'Candidato B: {vote_candidate_B} votos.\n'
            f'Nulos: {vote_null} votos.\n'
            f'Brancos: {vote_blank} votos.\n-----')
    else:
        vote_blank += 1

if(vote_candidate_A == 0) and (vote_candidate_B == 0) and (vote_null == 0) and (vote_blank == 0):
    print('Nenhum voto computado!\n')
else:
    print('\n-----Total de votos:-----\n'
    f'Candidato A: {vote_candidate_A} votos.\n'
    f'Candidato B: {vote_candidate_B} votos.\n'
    f'Nulos: {vote_null} votos.\n'
    f'Brancos: {vote_blank} votos.\n-----')