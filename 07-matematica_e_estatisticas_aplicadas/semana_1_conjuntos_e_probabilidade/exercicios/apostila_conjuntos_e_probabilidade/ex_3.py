'''
3) Escreva todos os elementos do conjunto:
a) A = {x∈N| x≤5}
b) B = {y∈Z | −5≤y≤5}
c) C = { (x, y)| x∈N e y∈R, x < 5 e y = x }
d) D = {q∈Q| 2q² - q - 1 = 0}
e) F = {n∈ N | n² = 2}

'''

import numpy as np

def calcula_baskhara(tipo_conjunto: str, a: float, b: float, c: float):
    conjunto = set() 
    delta = (b**2)-4*a*c
    if a == 0:
        print("valor de a deve ser diferente de zero")
    elif delta < 0:
        print("Não há raízes reais")
    else:
        x1 = (-b+delta**(1/2))/(2*a)
        x2 = (-b-delta**(1/2))/(2*a)
    if(tipo_conjunto == 'N'):
        if(x1 >= 0):
            conjunto.add(x1)
        if(x2 >= 0):
            conjunto.add(x2)
    else: 
        conjunto.add(x1)
        conjunto.add(x2)
    return conjunto

def equacao_2(numeros: list):
    conjunto = set()
    for i in range(len(numeros)):
        if(numeros[i] ** 2) == 2:
            conjunto.add(i)
    return conjunto

#a)
a = set(np.arange(0,6,1))
print(f'Conjunto A = {a}')

#b)
b = set(np.arange(5,-6,1))
print(f'Conjunto B = {b}')

#c)
x = set(np.arange(0,5,1))
y = set()
c = set()
for i in x:
    j = i ** (1/2)
    y.add(j)
    c.add((i, j))
print(f'Conjunto C = {c}')

#d
a1 = 2
b1 = -1
c1 = -1
tipo_conjunto = 'Q'
d = calcula_baskhara(tipo_conjunto, a1, b1, c1)
print(f'Conjunto D = {d}')

#e
a1 = 1
b1 = 0
c1 = -2
tipo_conjunto = 'N'
e = calcula_baskhara(tipo_conjunto, a1, b1, c1)
print(f'Conjunto E = {e}')