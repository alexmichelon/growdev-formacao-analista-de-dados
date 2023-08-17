import matplotlib.pyplot as plt
import numpy as np
import sympy

print('Em estudos realizados biológico, foi constatado que o número de'
      'indivíduos de certa espécie (N) está crescendo em função do tempo t'
      '(dado em anos), segundo a expressão:\n'

      'N(t) = 4 / 2+3 * (2**t)'

      '\na) Qual o domínio da função?'
      '\nb) Obter o gráfico da função.'
      '\nc) A função é crescente ou decrescente?'
      '\nd) Qual o conjunto imagem da função?\n')

#a
print('a)')
print('2 + 3 * (2**t) <> 0')
print('3 * (2**t) <> -2')
print('2**t = -2/3')
print('Não há valores de t que torna o denominador negativo. Então, o domínio da função são todos os números reais. '
      'Por se tratar de tempo, então o domínio será todos os números reais positivos.')

#b
'''x = np.arange(0,10,1)

def f(x):
    return 4 / (2+3*(2**x))

y = f(x)

fig, ax = plt.subplots(figsize=(8,6))
plt.title('Atividade Prática')
plt.plot(x, y, '-b', linewidth=2)
plt.plot(x, y, 'bo', linewidth=5)
plt.xlabel('Anos')
plt.ylabel('Número de Indivíduos')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(x, size=12)
plt.grid()
plt.show()'''

sympy.init_printing()
t = sympy.symbols('t')
N = 600 / (5+3*2**(t))
p = sympy.plot(N, xlim=(-20,20), ylim=(-1,300), show=True)

#c
print('\nc)\nA função é decrescente pois N(t) diminui conforme o valor de t aumenta.')

#d
print('\nd)\nConjunto imagem (valor de N(t) correspondente a cada valor t) desta função são todos os números reais maiores que zero: (0, +∞).')