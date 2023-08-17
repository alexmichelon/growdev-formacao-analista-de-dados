'''
Desafio
Crie um programa que funcione como um jogo de loteria, conforme as seguintes
regras:
    a) O programa deve gerar três números aleatórios entre 0 e 9;
    b) O usuário deve fornecer um palpite com três números, também entre 0 e 9; c)
Cada um dos palpites do usuário deve ser comparado com os números
aleatórios, de acordo com a tabela abaixo:
Números Correspondentes                     Número de pontos
Nenhum número coincidente                       0

Acertar um número                               10

Acertar dois números                            100

Acertar os três números, mas não na 
mesma ordemem que foram gerados                 1000

Acertar três números na mesma ordem que os
números aleatórios                              1.000.000
'''

import random

number_informed_1 = 0
number_informed_2 = 0
number_informed_3 = 0

random_number_1 = 0
random_number_2 = 0
random_number_3 = 0

asserts = 0

option = 'S'

#Valida se o String informado pelo usuário é um inteiro positivo
def validate_integer(order):
    value = input(order)
    while(not value.isdigit()) or (int(value) > 9):
        value = input(f'\nEntrada Inválida!\n{order}: ')
    return int(value)

#valida se a opção digitada pelo usuário é valida
def validate_option(order, comparision):
    option = input(order)
    while(option not in (comparision)):
        option = input(f'\nEntrada Inválida!\n{order}\n')
    return option



while(option != 'N'):

    print('\nBem vindo ao Programa Jogo de Loteria!\n')
    print('Informe três número dentre 0 e 9 os quais serão comparados com número aleatórios gerados pelo sistema.\n'
          'A pontuação, conforme acertos, se dá da seguinte forma:\n'
          ' - Nenhum número coincidente = 0 pontos\n'
          '- Acertar um número = 10 pontos\n'
          '- Acertar dois números = 100 pontos\n'
          '- Acertar os três números, mas não na mesma ordem que foram gerados = 1000 pontos\n'
          '- Acertar os três números na mesma ordem que os números aleatórios = 1.000.000 pontos\n')

    #Usuário informa três valores diferentes entre si
    number_informed_1 = validate_integer('Informe o primeiro número: ') 

    number_informed_2 = validate_integer(' Informe o segundo número: ')  
    while(number_informed_1 == number_informed_2):
        number_informed_2 = validate_integer('\nNúmero já escolhido!\nFavor, informe o segundo número: ')

    number_informed_3 = validate_integer('Informe o terceiro número: ')
    while(number_informed_3 == number_informed_1 ) or (number_informed_3 == number_informed_2):
        number_informed_3 = validate_integer('\nNúmero já escolhido!\nInforme o terceiro número: ')


    #O sistema gera três números randômicos diferentes entre si
    random_number_1 = random.randint(0,9)

    random_number_2 = random.randint(0,9)
    while(random_number_2 == random_number_1):
        random_number_2 = random.randint(0,9)

    random_number_3 = random.randint(0,9)
    while(random_number_3 == random_number_1) or (random_number_3 == random_number_2):
        random_number_3 = random.randint(0,9)

    '''
    print(f'  Números aleatórios gerados | números informados:\n'
          f'1º número: {random_number_1} | {number_informed_1}\n'
          f'2º número: {random_number_2} | {number_informed_2}\n'
          f'3º número: {random_number_3} | {number_informed_3}')
    '''

    input(f'\nNúmeros sorteados: ') 
    input(f'Primeiro número sorteado: {random_number_1} ')
    input(f' Segundo número sorteado: {random_number_2} ')
    print(f'Terceiro número sorteado: {random_number_3} ')

    #Comparação dos números informados pelo usuário com os números gerados aleatoriamente pelo sistema
    if(number_informed_1 == random_number_1) or (number_informed_1 == random_number_2) or  (number_informed_1 == random_number_3):
        if(number_informed_1 == random_number_1):
            asserts = 5
        elif(number_informed_1 == random_number_2):
            asserts = 1
        else:
            asserts = 1

    if(number_informed_2 == random_number_1) or (number_informed_2 == random_number_2) or  (number_informed_2 == random_number_3):
        if(number_informed_2 == random_number_1):
            asserts = asserts + 1
        elif(number_informed_2 == random_number_2):
            asserts = asserts + 5
        else:
            asserts = asserts + 1
    if(number_informed_3 == random_number_1) or (number_informed_3 == random_number_2) or  (number_informed_3 == random_number_3):
        if(number_informed_3 == random_number_1):
            asserts = asserts + 1
        elif(number_informed_3 == random_number_2):
            asserts = asserts + 1
        else:
            asserts = asserts + 5
    #asserts: 
    #         0 - nenhum
    #    1 ou 5 - acertou um número
    # 2, 6, 10  - acertou dois números
    # 3, 7, 11  - acertou todos os números fora da ordem
    #        15 - acertou todos os números na ordem


    #Informa a quantidade de acertos
    if(asserts == 0):
        print('\nERRRROUUUUU!! Infelizmente você não acertou NENHUM dos números!')
    elif(asserts == 1) or ( asserts == 5):
        print('\nFEZ BONITO!!! Você acertou UM dos números! Fez 10 PONTOS!')
    elif(asserts == 2) or (asserts == 6) or (asserts == 10):
        print('\nQUE ISSO HEIN!!! Você acertou DOIS dos números! Fez 100 PONTOS!')
    elif(asserts == 3) or (asserts == 7) or (asserts == 11):
        print('\nUAAAAUUUU!!! Você acertou TRÊS dos números fora da ordem! Fez 1.000 PONTOS!')
    elif(asserts == 15):
        print('\nO LOKO MEUUUUU! QUEM É ESSA FERA BIXXOOOO!! VOCÊ ACERTOU OS TRÊS NÚMEROS NA ORDEM!! Fez 1.000.000 PONTOS!')
    else:
        print(f'\nOH! Erro a ser tratado! Valor do <<asserts: {asserts}>>.')

    asserts = 0
    option = validate_option('Deseja jogar novamente? S/N  ','"S","s","N","n"').upper()