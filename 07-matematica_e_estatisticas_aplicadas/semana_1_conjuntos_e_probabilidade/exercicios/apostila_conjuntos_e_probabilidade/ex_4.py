'''4) São dados os conjuntos

A = {x∈Z | −4<x≤2}
B = {y∈N| x≤3}
C = {w∈Z | −2<x<5}
E = {z∈Z |3≤x≤8}

Determine:
a) A∪B
b) A∩C
c) B−C
d) E∪B
e) A∩(B∪E)
f) B−A
g) E−(C∩B)
h) C∩(A−B)
i) (A∩E)−B
j) (A∪E)−C'''

import numpy as np

a = set(np.arange(-3, 3, 1))
b = set(np.arange(0, 4, 1))
c = set(np.arange(-1, 5, 1))
e = set(np.arange(3, 9, 1))

print(f'Conjunto A = {a}')
print(f'Conjunto B = {b}')
print(f'Conjunto C = {c}')
print(f'Conjunto E = {e}')

#a) A∪B
conjunto = set(a.union(b))
print(f'a) Conjunto A∪B = {conjunto}')

#b) A∩C
conjunto = set(a.intersection(c))
print(f'b) Conjunto A∩C = {conjunto}')

#c) B−C
conjunto = set(b.difference(c))
print(f'c) Conjunto B-C = {conjunto}')

#d) E∪B
conjunto = set(e.union(b))
print(f'd) Conjunto E∪B = {conjunto}')

#e) A∩(B∪E)
conjunto = set(a.intersection(b.union(e)))
print(f'e) Conjunto A∩(B∪E) = {conjunto}')

#f) B−A
conjunto = set(b.difference(a))
print(f'f) Conjunto B−A = {conjunto}')

#g) E−(C∩B)
conjunto = set(e.difference(c.intersection(b)))
print(f'g) Conjunto E−(C∩B) = {conjunto}')

#h) C∩(A−B)
conjunto = set(c.intersection(a.difference(b)))
print(f'h) Conjunto C∩(A−B) = {conjunto}')

#i) (A∩E)−B
conjunto = set((a.intersection(e).difference(b)))
print(f'i) Conjunto (A∩E)−B = {conjunto}')

#j) (A∪E)−C
conjunto = set(a.union(e).difference(c))
print(f'j) Conjunto (A∪E)−C = {conjunto}')