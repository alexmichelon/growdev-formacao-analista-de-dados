'''
1) Conversão de graus Celsius para Fahrenheit – Crie um programa que
converta graus Celsius em Fahrenheit. A fórmula é a seguinte: �� =
9
5�� + 32
O programa deve solicitar ao usuário que insira uma temperatura em graus
Celsius e, em seguida, exiba a temperatura convertida em Fahrenheit. Após
construir esse programa, modifique-o para que converta graus Fahrenheit em
graus Celsius.
'''

#Converte em um String vírgula em ponto e caso tenha mais de um ponto, mantêm apenas o último ponto
def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

#Valida se o String informado pelo usuário é um float, incluindo negativos
def validate_number(order):
    value = input(order)
    while(not value.replace('-','').replace(',','').replace('.', '').isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    value = convert_coma_point(value)
    return float((value))

#valida se a opção digitada pelo usuário é valida
def validate_option(order, comparision):
    option = input(order)
    while(option not in (comparision)):
        option = input(f'\Entrada Inválida!\n {order}\n')
    return option


print('\nBem vindo ao sistema conversão de graus Celsius para Fahrenheit e vice e versa\n')

option = validate_option('Informe o tipo de conversão:\n'
                         '1 - Celsius para Fahrenheit\n'
                         '2 - Fahrenheit para Celsius\n'
                         '0 - para sair\n', '"0","1","2"')

while(option in ('0','1','2')):
    if (option == '1'):
        temperature_celsius = validate_number('\nInforme a temperatura em graus Celsius: \n')
        # calcula Celsius para Farenheit F = ((9/5) * C) +32
        temperature_fahrenheit = ((9/5) * temperature_celsius) + 32
        #Imprime a temperatura em Celsius e seu correspondente em Fahrenheit
        print(f'\nA temperatura informada {temperature_celsius:.2f}°C equivale à {temperature_fahrenheit:.2f}°F.\n')
    elif(option == '2'):
        temperature_fahrenheit = validate_number('Informe a temperatura em graus Fahrenheit: \n')
        # calcula Fahrenheit para Celsius C = ((F -32)/1.8)
        temperature_celsius = ((temperature_fahrenheit - 32)/1.8)
        #Imprime a temperatura em Fahrenheit e seu correspondente em Celsius
        print(f'\nA temperatura informada {temperature_fahrenheit:.2f}°F equivale à {temperature_celsius:.2f}°C.\n')
    else:
        #caso usuário digite 0 no menu, encerra o programa
        break
    #Após o cálculo, se quer fazer novo cálculo ou sair
    option = validate_option('Informe o tipo de conversão:\n'
                         '1 - Celsius para Fahrenheit\n'
                         '2 - Fahrenheit para Celsius\n'
                         '0 - para sair\n', '"0","1","2"')