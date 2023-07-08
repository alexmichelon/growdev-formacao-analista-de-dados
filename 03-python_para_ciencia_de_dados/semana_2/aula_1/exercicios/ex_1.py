'''
1) Faça um programa, com uma função que necessite de três argumentos, e
que forneça a soma desses três argumentos.
'''

def funcao_soma_tres_argumentos(argumento1, argumento2, argumernto3):
    try:
        soma = float(argumento1) + float(argumento2) + float(argumernto3)
    except ValueError:     
        soma = str(argumento1) + str(argumento2) + str(argumernto3)    
    return soma


print(funcao_soma_tres_argumentos(1,2,3))
print(funcao_soma_tres_argumentos(1,-2,0.625))
print(funcao_soma_tres_argumentos('A','B','C'))
print(funcao_soma_tres_argumentos('%',1,'B'))