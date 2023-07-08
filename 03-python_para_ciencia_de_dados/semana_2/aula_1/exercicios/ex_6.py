'''
6) Faça uma função que recebe por parâmetro o tempo de duração da produção
de uma peça em uma fábrica expressa em segundos e exibe esse tempo em
horas, minutos e segundos.
'''
from functions_utils import validate_integer_positive

def duracao(segundos):
    minutos = int(segundos / 60)
    segundos = segundos - (minutos * 60)
    horas = int(minutos / 60)
    minutos = minutos - (horas * 60)
    return horas, minutos, segundos

print('\nBem vindo ao sistema cálculo do tempo de duração de fabricação de peça em uma fábrica!!!\n')

segundos = validate_integer_positive('Informe o tempo de duração da produção da peça (em segundos):\n')

horas, minutos, segundos = duracao(segundos)
print(f'O tempo para fabricação da peça é: {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).')