'''
7) Escreva uma função que conte o número de espaços em branco em uma
frase passada como parâmetro.
'''

def conta_espaco_em_branco(texto):
    quantidade = texto.count(' ')
    return quantidade

frase = input('Informe uma frase: \n')

qtds = conta_espaco_em_branco(frase)

print(f'Há {qtds} espaços em branco na frase informada.')