'''
6) No lançamento de duas moedas, qual é a probabilidade de se obter, nas
faces voltadas para cima, pelo menos uma cara?
'''

moeda_1 = {'Cara', 'Coroa'}
moeda_2 = {'Cara', 'Coroa'}
universo = set()

for i in moeda_1:
    for j in moeda_2:
        universo.add((i, j))

contador = 0

for evento in universo:
    for chance in evento:
        if(chance == 'Cara'):
            contador +=1
            break

print(f'Conjunto universo: {universo}.')
print(f'As chances de ao menos uma Cara voltada para coima é de {contador}/{len(universo)} ou {(contador/len(universo))*100:.0f} %.')
