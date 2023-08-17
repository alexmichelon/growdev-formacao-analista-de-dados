'''
11) Extrai-se, aleatoriamente, uma carta de um baralho de 52 cartas. Qual a
probabilidade de a carta extraída ser valete ou uma carta de paus?
'''

ser_valete = 4 / 52
ser_carta_paus = 13 / 52
interseccao = 1 / 52

probabilidade = ser_valete + ser_carta_paus - interseccao

print(f'A probabilidade de ser um valete ou uma carta de paus é de {probabilidade*100:.2f} %.')