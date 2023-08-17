'''
4) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.

'''
import functions_utils as func

vetor_1 = []
vetor_2 = []
vetor_3 = []

print('\nBem vindo ao sistema Gera Vetor intercalado!!!\n')

for i in range(0, 100, 10):
    vetor_1.append(i)
    vetor_2.append(i+1)

print(f'Valores Vetor 1 : {vetor_1}')
print(f'Valores Vetor 2 : {vetor_2}')

for i in range(10):
    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print(f'Valores Vetor 3 : {vetor_3}')