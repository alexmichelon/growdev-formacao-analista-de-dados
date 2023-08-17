'''
7) Faça um programa para ler a temperatura atual e conforme leitura, imprima o
resultado de acordo com a tabela abaixo.
Temperatura Resultado
até 15º Muito frio
de 16º à 22º Frio
de 23º à 26º Agradável
de 27º à 30º Quente
31º ou mais Muito quente
'''

#Valida se o String informado pelo usuário é um inteiro positivo
def validate_number(order):
    value = input(order)
    while(not value.replace('-','').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}')
    return int(value)

print('\nBem vindo ao programa Condição Climática!!!\n')

temperature = validate_number('Informe a temperatura (em graus Celsius): ')

if(temperature <= 15):
    print(f'Temperatura {temperature:.2f}°C: Muito frio.')
elif(temperature > 15) and (temperature <= 22):
    print(f'Temperatura {temperature:.2f}°C: Frio.')
elif(temperature > 22) and (temperature <= 26):
    print(f'Temperatura {temperature:.2f}°C: Agradável.')
elif(temperature > 27) and (temperature <= 30):
    print(f'Temperatura {temperature:.2f}°C: Quente.')
else:
    print(f'Temperatura {temperature:.2f}°C: Muito quente.')