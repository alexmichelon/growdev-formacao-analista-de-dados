'''
8) Crie uma estrutura bidimensional utilizando listas com sublistas para
representar um tabuleiro (1 lista com 20 elementos e cada elemento é uma
lista de 20 elementos, tabuleiro 20x20). Cada posição irá armazenar 1 valor
numérico que significa:
0 - Água
1 - Navio

Para cada posição escolha esses valores aleatoriamente, respeitando a regra
de que não podem existir mais de 20 navios no tabuleiro. Após os valores
serem distribuídos, o programa deve pedir ao usuário uma posição do
tabuleiro e informar se ele acertou um navio ou água e repetir o procedimento
até que o usuário derrote todos os navios ou chegue ao limite de 35
tentativas.

9) Modifique o programa anterior para exibir as seguintes estatísticas.
a) Acertos em água
b) Acertos em Navios
c) Porcentagem de acertos em água
d) Porcentagem de acertos em Navios
e) Acertos ininterruptos (maior quantidade de acertos em sequência)
'''

import random as r
import functions_utils as func

#tamanho do tabuleiro
board_size = 20
#máximo de tentativas permitidas
max_atempts_permited = 35
#número máximo de navios permitido
max_ships_permited = 20
#valor para água
value_water = 0
#valor para navio
value_ship = 1
#caracter para simbolizar posições não tentadas no tabuleiro
board_view_value = 'X'
#tabuleiro (lista)
list_board = []
#tabuleiro para visualização (lista)
list_board_view = []
#lista das posições dos navios no tabuleiro
list_positions_ships = []
#lista de tentativas: guarda as posições informadas pelo usuário
list_atempts = []
#contador de tentativas acertadas (quando informa uma posição que é um navio)
right_atempts = 0
#maior número de acertos ininterruptos (acertos em navios)
total_uninterrupted_asserts = 0
#contador de número de acertos em sequência (acertos em navios)
count_uninterrupted_asserts = 0
#menor posição permitida a ser informada
min_permited = 1
#maior posição permitida a ser informada
max_permited = 20


#gera randomicamente uma posição no tabuleiro (list_board)
def generate_position_random():
    return r.randint(0,board_size-1) 

#gera o tabuleiro com valores 0 para todas as posições
def generate_all_board_value_water():
    for i in range(board_size):
        list_board.append([])
        list_board_view.append([])
        for j in range(board_size):
            list_board[i].append(value_water)
            list_board_view[i].append(board_view_value)

#encontra randomicamente uma posição (linha e coluna) no tabuleiro para atribuir o navio
def fill_in_ship_positions_board_random():
    for i in range(0, max_ships_permited, 1):
        position_line = generate_position_random() 
        position_column = generate_position_random()
        #atribui navio para a posição (linha e coluna)
        list_board[position_line][position_column] = value_ship
        #adiciona a posição (linha e coluna) na lista de posição de navios do tabuleiro
        list_positions_ships.append((position_line, position_column))

#insere a tentativa informada em uma lista de tentativas
def insert_atempt_in_list_atempts(line, column):
    #adiciona a linha e coluna informada na lista de tentativas
    list_atempts.append((line, column))
    return list_atempts

def compare_atempt_whit_list_atempts(line, column):
    #verifica se a posição informada já foi informada anteriormente (salva na lista de tentativas)
        if((int(line), int(column)) in list_atempts):
            #senão tiver na lista, sai do laço senão pede a informação de uma nova posição
            print('\nPosição já informada!!!\n')
            return False       
        return True

#gera a visualização parcial do tabuleiro
def fill_in_list_board_view_whit_atempt(line, column):
    list_board_view[line][column] = str(list_board[line][column])

#imprime o tabuleiro
def print_list_board(list):
    for i in range(len(list)):
        print(list[i])

#compara se a tentativa informada é um navio
def compare_atempt_whit_position_board(right_atempts, line, column, total_uninterrupted_asserts, count_uninterrupted_asserts):
    try:
        if (list_board[line][column] == value_ship):
            #itera a quantidade de acertos
            right_atempts += 1
            count_uninterrupted_asserts += 1
            if(total_uninterrupted_asserts < count_uninterrupted_asserts):
                total_uninterrupted_asserts = count_uninterrupted_asserts
            print('\nVOCÊ ACERTOU O NAVIO!!!!\n')
        else:
            count_uninterrupted_asserts = 0
            print('\nErrou! Acertou a água!\n')
        #insere a posição informada na lista de tentativas
        insert_atempt_in_list_atempts(int(line), int(column))        
    #trata erro de posição informada inexistente no tabuleiro
    except IndexError: 
        print('\nPosição inexistente no tabuleiro!\n')
    
    fill_in_list_board_view_whit_atempt(line, column)
    #imprime o tabuleiro de visualização (list_board_view) para saber as posições tentadas
    print('SUAS TENTATIVAS')
    print_list_board(list_board_view)
    #imprime o total de tentativas até o momento
    print(f'\nTotal de Tentativas: {len(list_atempts)}')
    #imprime o total de tentativas acertadas até o momento
    print(f'Total de Acertos em Navios: {right_atempts}\n')
    return right_atempts, total_uninterrupted_asserts, count_uninterrupted_asserts

           

print('\nBem vindo ao Jogo Água e Navio 2.0:\n'
      f'O jogo corresponde há um tabuleiro de {board_size} linhas e {board_size} colunas, preenchidos com Água ({value_water}) e Navio ({value_ship}).\n'
      f'Neste tabuleiro há {max_ships_permited} navios. Você deverá informar uma posição (linha e coluna) para acertar o maior número possível de navios.\n'
      'O jogo encerra em duas situações:\n'
      '1 - caso todos os navios sejam acertados\n'
      f'2 - caso sejam fornecidas {max_atempts_permited} tentativas e não sejam acertados todos os navios.\n')

generate_all_board_value_water()
fill_in_ship_positions_board_random()
print('TABULEIRO')
print_list_board(list_board_view)

#verifica se o número de tentativas corrresponde ao total de tentativas permitidas
#ou se o total de acertos corresponde ao número total de navios disponíveis
while(len(list_atempts) < max_atempts_permited) and (right_atempts < max_ships_permited):   
    while True:
        print(f'\n----------\nTentativa nr. {len(list_atempts)+1}')
        #informa a posição desejada no tabuleiro: em razão de linha e coluna começarem de zero,
        #diminui-se 1 do valor de liha e do valor de coluna informado
        line = func.validate_integer_positive_whit_range_included('Informe a linha: ', min_permited, max_permited)-1
        column = func.validate_integer_positive_whit_range_included('Informe a coluna: ', min_permited, max_permited)-1
        #compara se a posião informada já está na lista de tentativas, se estiver segue, senão pede nova posição
        if(compare_atempt_whit_list_atempts(line, column)):
            break
    #verifica se a posição informada corresponde há um navio
    right_atempts, total_uninterrupted_asserts, count_uninterrupted_asserts = compare_atempt_whit_position_board(right_atempts, line, column, total_uninterrupted_asserts, count_uninterrupted_asserts)    
    


print('\n-----------\nRESULTADO DO JOGO:\n-----------')
if(len(list_atempts) == max_atempts_permited):
    print(f'O jogo acabou pois foi atingido o número máximo de {max_atempts_permited} tentativas.')
else:
    print(f'O jogo acabou pois todos os {max_ships_permited} navios existentes no tabuleiro foram acertados.')
print(f'Total de Acertos nos Navios: {right_atempts} ({(right_atempts * 100) / len(list_atempts):.0f}% do total de tentativas.)')
print(f'Total de Acertos na Água: {len(list_atempts) - right_atempts} ({((len(list_atempts) - right_atempts)*100)/len(list_atempts):.0f}% do total de tentativas.)')
print(f'Total de Tentativas Feitas: {len(list_atempts)} tentativas.')
print(f'Maior quantidade de acertos em sequência: {total_uninterrupted_asserts} tentativa(s).')
#print('\n-----------')
#print(f'Lista Posições dos navios: {list_positions_ships}')
#print(f'Lista de tentativas: {list_atempts}')

print('----------\nTABULEIRO ORIGINAL\n----------')
print_list_board(list_board)