'''
7) Um dado é lançado duas vezes e em cada lançamento é anotado o
valor da face que ficou para cima. Qual a probabilidade de os números
anotados somarem 7?
'''

dado_1 = {1,2,3,4,5,6}
dado_2 = {1,2,3,4,5,6}

universo = set()
for i in dado_1:
    for j in dado_2:
        universo.add((i, j))

print(f'Todas as chances possíveis:\n{universo}')

contador_soma_7 = 0
valores_soma_7 = set()

for possibilidade in universo:
    soma = 0
    for p in possibilidade:
        soma += p
    if(soma == 7):
        contador_soma_7 += 1
        valores_soma_7.add(possibilidade)

print(f'A probabilidade dos números anotados terem a soma 7 é de {contador_soma_7} / {len(universo)} = {(contador_soma_7/len(universo)*100):.2f} %.')
print(f'Pares possíveis que somam 7:\n{valores_soma_7}')