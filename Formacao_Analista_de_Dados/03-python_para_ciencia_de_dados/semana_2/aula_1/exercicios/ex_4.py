'''
4) Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e
colunas, com um número em cada posição e no qual a soma das linhas,
colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de
lado 3, com números de 1 a 9:
8 3 4
1 5 9
6 7 2
Elabore uma função que receba uma estrutura de 3x3 formada por listas, e
diga se é um quadrado mágico ou não.
'''
from functions_utils import validate_integer_positive_whit_range_included

tamanho_quadrado = 3
faixa_inicial = 1
faixa_final = 9
lista = []
lista = [[1,2,3], [3,1,2], [2,3,1]]
#lista = [[8,3,4], [1,5,9], [6,7,2]]
lista = [[1,1,1], [1,1,1], [1,1,1]]

def informa_valores():    
    for i in range(tamanho_quadrado):
        lista.append([])
        for j in range(tamanho_quadrado):
            valor = validate_integer_positive_whit_range_included('Informa o valor: ', faixa_inicial, faixa_final)
            lista[i].append(valor)
    return lista

def compara_soma_linhas(lista):
    soma = 0
    soma_linha = 0
    for i in range(tamanho_quadrado):
        soma = 0
        for j in range(tamanho_quadrado):
            soma += lista[i][j]
        if(i == 0):
            soma_linha = soma
        else:
            if(soma_linha == soma):
                continue            
            else:
                return False    
    return soma
        
def compara_soma_colunas(lista):
    soma = 0
    soma_coluna = 0
    for i in range(tamanho_quadrado):
        soma = 0
        for j in range(tamanho_quadrado):
            soma += lista[j][i]
        if(i == 0):
            soma_coluna = soma
        else:
            if(soma_coluna == soma):
                continue            
            else:
                return False    
    return soma

def compara_soma_diagonais(lista):
    soma_diagonal_principal = 0
    soma_diagonal_inversa = 0
    posicao_invertida = tamanho_quadrado
    for i in range(tamanho_quadrado):
        for j in range(tamanho_quadrado):
            if (i == j):
                soma_diagonal_principal += lista[i][j]
        for i in range(posicao_invertida - i):
                posicao_invertida -= 1
                soma_diagonal_inversa += lista[i][posicao_invertida]
    if(soma_diagonal_principal != soma_diagonal_inversa):
        return False
    return soma_diagonal_principal

lista = informa_valores()

soma_linha = compara_soma_linhas(lista)
soma_coluna = compara_soma_colunas(lista)
soma_diagonais = compara_soma_diagonais(lista)

if(soma_linha == False) or (soma_coluna == False) or (soma_diagonais == False):
    print('Não é um quadrado mágico!')
elif(not(soma_linha == soma_coluna == soma_diagonais)):
    print('Não é um quadrado mágico!')
else:
    print('É um quadrado mágico!')    