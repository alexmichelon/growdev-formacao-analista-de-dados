print('\nSeja bem vindo ao Sistema Troca de Valores!!!\n')

a = input('Informe um valor para a variável A:\n')
b = input('Informe um valor para a variável B:\n')

#utilizando variável auxiliar
c = a
a = b
b = c

print('O valor inicial de A era: ' + b + ' mas agora é ' + a + '.')
print('O valor inicial de B era: ' + a + ' mas agora é ' + b + '.\n')

#utilizando lista
"""
[a, b] = [b, a]

print('O valor inicial de A era: ' + b + ' mas agora é ' + a + '.')
print('O valor inicial de B era: ' + a + ' mas agora é ' + b + '.')
"""
