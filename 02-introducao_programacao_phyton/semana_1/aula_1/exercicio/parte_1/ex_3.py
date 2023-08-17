import numpy as np

#Matriz para indicar todos os caminhos disponíveis
#O = Início
#B = Opção disponível
#' ' = Opção indisponível
#R = Opção indisponível
#G = Ponto de chegada
array_all_path = np.array(
    [
[' ', ' ', ' ', ' ', 'B', 'B', 'B', 'G', 'B', 'B', 'B', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', 'R', ' '],
[' ', 'R', ' ', ' ', ' ', ' ', 'B', 'B', ' ', 'B', 'B', 'B', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', 'B', 'B', 'B', 'R', 'B', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', 'B', 'R', 'B', ' ', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', 'B', 'B'],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'R', 'B', 'B', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', 'B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
)

#Matriz para indicar o todo o caminho percorrido do início ao fim
#X = Indica os pontos visitados
array_all_visited_points = np.array(
    [
[' ', ' ', ' ', ' ', 'B', 'B', 'B', 'G', 'B', 'B', 'B', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', 'R', ' '],
[' ', 'R', ' ', ' ', ' ', ' ', 'B', 'B', ' ', 'B', 'B', 'B', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', 'B', 'B', 'B', 'R', 'B', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', 'B', 'R', 'B', ' ', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', 'B', 'B'],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'R', 'B', 'B', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', 'B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
)

#Matriz para o menor caminho a ser percorrido do início ao fim
#X = Indica os pontos visitados
array_visited_points_short_path = np.array(
    [
[' ', ' ', ' ', ' ', 'B', 'B', 'B', 'G', 'B', 'B', 'B', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', 'R', ' '],
[' ', 'R', ' ', ' ', ' ', ' ', 'B', 'B', ' ', 'B', 'B', 'B', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', 'B', 'B', 'B', 'R', 'B', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', 'B', 'R', 'B', ' ', 'B', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', ' ', 'B', 'B', 'B', 'B'],
[' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'R', 'B', 'B', 'B', ' ', ' ', ' '],
[' ', 'B', ' ', ' ', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', 'B', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
)

#variável para obter o índice na matriz a cada iteração
line = 17
#variável para obter o índice na matriz a cada iteração
column = 0
#lista dos pontos visitados ordenadas por ordem de visita
list_visited_points = []
#lista dos pontos para percorrer o menor caminho por ordem de visita
list_points_shorter_path = []


#Função para verificar se o ponto acima do ponto atual está disponível para ser visitado
def check_up(line, column):
    #valida se o ponto acima está na lista de pontos visitados e se este ponto está disponível para ser visitado
    if ([line-1,column] not in list_visited_points) and (array_all_path[line-1,column] not in ('R',' ')):
    #Ponto de cima não foi visitado e é ponto disponível
        #Marca na matriz de todos os pontos visitados o ponto de cima com um X
        array_all_visited_points[line-1,column] = 'X'
        #Adiciona o ponto de cima do ponto atual na lista de pontos visitados
        list_visited_points.append([line-1,column]) 
        #Marca na matriz do menor caminho possível com um X o ponto de cima
        array_visited_points_short_path[line-1,column] = 'X'
        #Adiciona o ponto de cima do ponto na lista de menor caminho possível
        list_points_shorter_path.append([line-1,column])
        #Retorna verdadeiro para que seja possível iterar posteriormente o indice da linha (line)                  
        return True
    else:
        #Adiciona o ponto de cima do ponto atual na lista de pontos visitados
        #Adiciona novamente mesmo que este ponto já esteja na lista de todos os pontos visitados
        #Necessário para que seja possível saber quantas vezes passou no mesmo ponto
        list_visited_points.append([line,column])
        #Verifica se o último ponto adicionado é igual ao penúltimo ponto adicionado
            #Isso é necessário pois a verificação do algoritmo é na sequência:
                #- no ponto de cima
                #- ponto da direita
                #- ponto da esquerda
                #- ponto de baixo
            #e a cada verificação adiciona o mesmo ponto que pode ser igual ao último
        if(list_visited_points[-1] == list_visited_points[-2]):
            #Caso o último ponto for igual ao penúltimo, excluir o último
            list_visited_points.pop(-1)
            #Retorna falso para que não seja possível iterar posteriormente o indice da linha (line)
        return False


#Função para verificar se o ponto da direita do ponto atual está disponível para ser visitado
def check_right(line, column):
    #valida se o ponto da direita está na lista de pontos visitados e se este ponto está disponível para ser visitado
    if([line,column+1] not in list_visited_points) and (array_all_path[line,column+1] not in ('R',' ')):
    #Ponto da direita não foi visitado e é ponto disponível
        #Marca na matriz de todos os pontos visitados o ponto da direita com um X
        array_all_visited_points[line,column+1] = 'X'
        #Adiciona o ponto da direita do ponto atual na lista de pontos visitados
        list_visited_points.append([line,column+1])
        #Marca na matriz do menor caminho possível com um X o ponto da direita
        array_visited_points_short_path[line,column+1] = 'X'     
        #Adiciona o ponto da direita do ponto na lista de menor caminho possível      
        list_points_shorter_path.append([line,column+1])
        #Retorna verdadeiro para que seja possível iterar posteriormente o indice da coluna (column)
        return True
    else:
        #Adiciona o ponto da esquerda do ponto atual na lista de pontos visitados
        #Adiciona novamente mesmo que este ponto já esteja na lista de todos os pontos visitados
        #Necessário para que seja possível saber quantas vezes passou no mesmo ponto
        list_visited_points.append([line,column])
        #Verifica se o último ponto adicionado é igual ao penúltimo ponto adicionado
            #Isso é necessário pois a verificação do algoritmo é na sequência:
                #- no ponto de cima
                #- ponto da direita
                #- ponto da esquerda
                #- ponto de baixo
            #e a cada verificação adiciona o mesmo ponto que pode ser igual ao último
        if(list_visited_points[-1] == list_visited_points[-2]):
            #Caso o último ponto for igual ao penúltimo, excluir o último
            list_visited_points.pop(-1)
            #Retorna falso para que não seja possível iterar posteriormente o indice da coluna (column)
        return False

#Função para verificar se o ponto da esquerda do ponto atual está disponível para ser visitado
def check_left(line, column):
    #valida se o ponto da esquerda está na lista de pontos visitados e se este ponto está disponível para ser visitado
    if([line,column-1] not in list_visited_points) and (array_all_path[line,column-1] not in ('R',' ')):
    #Ponto da esquerda não foi visitado e é ponto disponível
        #Marca na matriz de todos os pontos visitados o ponto da esquerda com um X
        array_all_visited_points[line,column-1] = 'X'
        #Adiciona o ponto da esquerda do ponto atual na lista de pontos visitados
        list_visited_points.append([line,column-1])
        #Marca na matriz do menor caminho possível com um X o ponto da esquerda
        array_visited_points_short_path[line,column-1] = 'X'
        #Adiciona o ponto da direita da esquerda na lista de menor caminho possível
        list_points_shorter_path.append([line,column-1])
        #Retorna verdadeiro para que seja possível iterar posteriormente o indice da coluna (column)
        return True
    else:
        #Adiciona o ponto da esquerda do ponto atual na lista de pontos visitados
        #Adiciona novamente mesmo que este ponto já esteja na lista de todos os pontos visitados
        #Necessário para que seja possível saber quantas vezes passou no mesmo ponto
        list_visited_points.append([line,column])
        #Verifica se o último ponto adicionado é igual ao penúltimo ponto adicionado
            #Isso é necessário pois a verificação do algoritmo é na sequência:
                #- no ponto de cima
                #- ponto da direita
                #- ponto da esquerda
                #- ponto de baixo
            #e a cada verificação adiciona o mesmo ponto que pode ser igual ao último
        if(list_visited_points[-1] == list_visited_points[-2]):
            #Caso o último ponto for igual ao penúltimo, excluir o último
            list_visited_points.pop(-1)
            #Retorna falso para que não seja possível iterar posteriormente o indice da coluna (column)
        return False

#Função para verificar se o ponto de baixo do ponto atual está disponível para ser visitado
def check_down(line, column):
    #valida se o ponto de baixo está na lista de pontos visitados e se este ponto está disponível para ser visitado
    if([line+1,column] not in list_visited_points) and (array_all_path[line+1,column] not in ('R',' ')):
    #Ponto de baixo não foi visitado e é ponto disponível
        #Marca na matriz de todos os pontos visitados o ponto de baixo com um X
        array_all_visited_points[line+1,column] = 'X'
        #Adiciona o ponto de baixo do ponto atual na lista de pontos visitados
        list_visited_points.append([line+1,column])
        #Marca na matriz do menor caminho possível com um X o ponto de baixo
        array_visited_points_short_path[line+1,column] = 'X'
        #Adiciona o ponto de baixo da esquerda na lista de menor caminho possível
        list_points_shorter_path.append([line+1,column])
        #Retorna verdadeiro para que seja possível iterar posteriormente o indice da linha (line)
        return True
    else:
        #Adiciona o ponto de baixo do ponto atual na lista de pontos visitados
        #Adiciona novamente mesmo que este ponto já esteja na lista de todos os pontos visitados
        #Necessário para que seja possível saber quantas vezes passou no mesmo ponto
        list_visited_points.append([line,column])
        #Verifica se o último ponto adicionado é igual ao penúltimo ponto adicionado
            #Isso é necessário pois a verificação do algoritmo é na sequência:
                #- no ponto de cima
                #- ponto da direita
                #- ponto da esquerda
                #- ponto de baixo
            #e a cada verificação adiciona o mesmo ponto que pode ser igual ao último
        if(list_visited_points[-1] == list_visited_points[-2]):
            #Caso o último ponto for igual ao penúltimo, excluir o último
            list_visited_points.pop(-1)
            #Retorna falso para que não seja possível iterar posteriormente o indice da linha (line)
        return False

#Função para retornar ao último ponto visitado
def return_last_point_visited(line, column):
    #Tratamento de erro para evitar casos em que o índice (linha e coluna) 
    # aponte para um índice inexistente na lista de menor caminho possível
    # por exemplo, um ponto antes adicionado e após retirado desta lista
    try:
        #Retira da lista de menor caminho possível o ponto atual
        # pois todas as checagens ou deram ponto indisponível ou ponto já visitado
        list_points_shorter_path.pop(list_points_shorter_path.index([line, column]))
        #Na matriz de menor caminho possível, marca como disponível um ponto anteriormente visitado
        array_visited_points_short_path[line, column] = 'B'
        #Trata a exceção indicando que caso ocorra erro, que o sistema apenas continue  
    except ValueError:
        pass
    #fornece o índice (valor da linha e coluna) do último ponto antes do ponto atual
    # dentro da lista de todos os pontos visitados
    # volta o índice para a última bifurcação encontrada 
    # local onde foi feita a checagem (considerando a ordem para cima, direita, esquerda ou para baixo)
    [line, column] = list_visited_points[list_visited_points.index([line, column])-1]     
    #Retorna o novo índice (linha e coluna) para realizar nova iteração
    return [line, column]


#Enquanto o ponto visitado não é o final
while(array_all_path[line, column] != 'G'):
    #Enquanto o ponto visitado não é o final (feito para permitir a saída negativa de cada checagem)
    while(array_all_path[line, column] != 'G'):
        #Checagem do ponto de cima
        if(check_up(line,column) == True):
            #Caso a checagem do ponto de cima seja verdadeira, itera o índice da linha (diminui)
            line = line - 1
            #sai do laço de repetição para que seja feita nova checagem do próximo ponto
            break
        #Checagem do ponto da direita
        elif(check_right(line, column) == True):
            #Caso a checagem do ponto de cima seja verdadeira, itera o índice da coluna (aumenta)
            column = column + 1
            #sai do laço de repetição para que seja feita nova checagem do próximo ponto
            break
         #Checagem do ponto da esquerda
        elif(check_left(line, column) == True):
            #Caso a checagem do ponto de cima seja verdadeira, itera o índice da coluna (diminui)
            column = column - 1
            #sai do laço de repetição para que seja feita nova checagem do próximo ponto
            break
         #Checagem do ponto de baixo
        elif(check_down(line, column) == True):
            #Caso a checagem do ponto de cima seja verdadeira, itera o índice da linha (aumenta)
            line = line + 1
            #sai do laço de repetição para que seja feita nova checagem do próximo ponto
            break
        else:
            #Retorna o índice (linha e coluna) do último ponto visitado antes do ponto atual
            [line, column] = return_last_point_visited(line, column)

    if (array_all_path[line, column] == 'G'):
        #Atribui o valor do ponto de chegada final na matriz de todos os pontos visitados para demonstração em tela
        array_all_visited_points[line, column] = 'G'
        #Atribui o valor do ponto de chegada final na matriz do menor cainho possível para demonstração em tela
        array_visited_points_short_path[line, column] = 'G'

        #Impressão em tela em dois formatos da Matriz de todos os caminhos disponíveis
        #print('\n\nTOTAL PATH\n' + str(array_all_path))
        print(f'\nTOTAL PATH\n {array_all_path}')

        #Impressão em tela em dois formatos da Matriz de todos os caminhos visitados
        #print('\n\nPATH TRAVELLED\n' + str(array_all_visited_points))
        print(f'\n\nPATH TRAVELLED\n {array_all_visited_points})')

        #Impressão em tela em dois formatos da lista de todos os pontos visitados
        #print('\nPOSITIONS VISITED (BESIDE)\n' + str(list_visited_points))        
        print(f'\nPOSITIONS VISITED (BESIDE)\n {list_visited_points}')

        #Impressão em tela os pontos da lista de pontos visitados um ponto abaixo do ooutro
        #print('\nPOSITIONS VISITED (UNDER)')
        #[print(point_list) for point_list in list_visited_points]

        #Impressão em dois formatos da Matriz dos pontos do menor caminho possível
        #print('\n\nSHORT PATH POSSIBLE\n' + str(array_visited_points_short_path))
        print(f'\n\nSHORTER PATH POSSIBLE\n {array_visited_points_short_path}')

        #Impressão em dois formatos da lista dos pontos do menor caminho possível
        #print('\nSHORT WAY POSSIBLE (BESIDE)\n' + str(list_points_shorter_path))
        print(f'\nSHORTER PATH POSSIBLE (BESIDE)\n {list_points_shorter_path}')    
        break