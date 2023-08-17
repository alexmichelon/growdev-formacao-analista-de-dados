'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

'''1) Escreva todos os elementos do conjunto:
a) A = {x | x é uma vogal}
b) B = {y | y é um mês do ano}
c) C = {z | z é o número em que z⋅15 = 15}
d) D = {q | q é o número que resulta da divisão de 15 por zero}'''

def encontra_numero():
    z = set()
    for i in range(15):
        if (i * 15) == 15:
            z.add(i)
    return z

def resulta_divisao():
    q = set()
    q.add(15 / 0)
    return q

a = {'a', 'e', 'i', 'o', 'u'}
b = {'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'}
c = encontra_numero()
d = resulta_divisao()

print(a)
print(b)
print(c)
print(d)