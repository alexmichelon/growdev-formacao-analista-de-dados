'''
10) Uma urna contém cinco bolas vermelhas, três bolas azuis e quatro bolas
brancas. Retira-se, ao acaso, uma bola da urna. Qual é a probabilidade de
sair uma bola vermelha ou uma bola azul?
'''

bolas_vermelhas = 5
bolas_azuis = 3
bolas_brancas = 4

universo = bolas_vermelhas + bolas_azuis + bolas_brancas

probabilidade_bola_vermelha_azul = (bolas_vermelhas/universo) + (bolas_azuis/universo)

print(f'A probabilidade de sair uma bola vertelha é de {bolas_vermelhas + bolas_azuis}/{universo}, {probabilidade_bola_vermelha_azul*100:.2f} %.')