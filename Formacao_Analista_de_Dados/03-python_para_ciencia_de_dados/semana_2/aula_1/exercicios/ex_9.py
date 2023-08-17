'''
9) Implemente um programa onde o usuário deve adivinhar as letras de uma
palavra por meio de palpites. A palavra deve ser mostrada inicialmente com
as letras substituídas por underlines, conforme exemplo abaixo.

dados => _ _ _ _ _

O usuário deve então palpitar sobre as letras que ele julga estarem na frase.
A cada letra que errar, ele perde 1 ponto. A cada letra que ele acertar a
mesma deve ser exibida na tela, exemplo:

Palpite: d
Saída: d _ d _ _

Se completar a frase o usuário ganha o jogo, se sua pontuação zerar ele
perde o jogo. Ao iniciar o jogo, a pontuação é de 4 pontos.
'''

from functions_utils import validate_caracter_is_alpha

pontos = 4
palpite = ''
palavra = 'AAAAAAA'
vetor_palavra = []
tentativas = []

def gera_palavra_sem_letras():    
    for i in range (len(palavra)):
        vetor_palavra.append('_')
    return vetor_palavra

def verifica_palpite(palpite, vetor_palavra, pontos):
    qtd = palavra.count(palpite)
    if(qtd > 0):
        vetor_palavra = mostra_palavra_tela(qtd, palpite, vetor_palavra)
    else:
        pontos -= 1
    tentativas.append(palpite)
    return vetor_palavra, pontos

def mostra_palavra_tela(qtd, palpite, vetor_palavra):
    indice = 0
    inicio = 0
    for i in range(qtd):
        indice = palavra.find(palpite, inicio)        
        vetor_palavra[indice] = palpite
        inicio = indice + 1
    return vetor_palavra

def gera_palavra_tela(vetor_palavra):
    texto_tela = ''
    for i in range(len(vetor_palavra)):
        texto_tela += vetor_palavra[i]
    return texto_tela

print('\nBem vindo ao sistema advinhe a palavra!\n')

gera_palavra_sem_letras()

while(pontos > 0):
    texto = gera_palavra_tela(vetor_palavra)
    if(texto == palavra):
        break
    print(f'-----\ndados => {texto}')
    palpite = validate_caracter_is_alpha('Informe uma letra: \n').upper() 
    vetor_palavra, pontos = verifica_palpite(palpite, vetor_palavra, pontos)    
    print(f'Número de pontos: {pontos}') 
    print(f'Palpites: {tentativas}\n')   

if (pontos == 0):
    print('Você perdeu o jogo! O número de pontos chegou a zero. A palavra era: \n {palavra}')
else:
    print(f'\nVocê acertou a palavra: {texto}')