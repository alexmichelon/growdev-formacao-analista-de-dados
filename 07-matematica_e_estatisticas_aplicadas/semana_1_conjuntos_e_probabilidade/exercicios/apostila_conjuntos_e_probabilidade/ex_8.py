'''
8) Uma urna contém apenas bolas vermelhas, azuis, brancas e pretas.
Retira-se ao acaso uma bola da urna. A probabilidade de sair uma bola
vermelha é 5/17. Qual a probabilidade de sair uma bola que não seja vermelha?
'''
#PE = probabilidade de ocorrer um evento E (número entre 0 e 1)
#PE1 = probabilidade de ocorrer outro evento diferente de PE
#U = todos os eventos possíveis (1 (um))
#PE1 = U - PE

probabilidade_bola_vermelha = 5/17
probabilidade_bola_nao_ser_vermelha = 1 - probabilidade_bola_vermelha

print(f'A probabilidade da bola sorteada não ser vermleha é de {probabilidade_bola_nao_ser_vermelha * 100:.2f} %.')