'''
4) Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte
forma:
CENTENA = x
DEZENA = x
UNIDADE = x
Exemplo: 357 tem 3 centenas, 5 dezenas e 7 unidades.
'''

#Valida se o String informado pelo usuário é um inteiro positivo
def validate_number(order):
    value = input(order)
    while(not value.isdigit()):
        value = input(f'\nEntrada Inválida!\n{order}\n')
    return int(value)

print('\nBem vindo ao programa Descreve Centenas, Dezenas e Unidades\n')

number = validate_number('Informe um número (com até três digitos): ')

if(number <= 9):
    #o resto da divisão é a unidade
    unit = number % 10
    print(f'\nO número {number} tem {unit} unidade(s).')
elif (number > 9) and (number < 100):
    #unidade é o resto da divisão entre o número informado e 10
    unit = number % 10
    #dezena é o número informado menos as unidades divido por 10
    ten = (number - unit) / 10
    print(f'\nO número {number} tem {ten} dezena(s) e {unit} unidade(s).')
else:
    #unidade é o resto da divisão entre o número informado e 10
    unit = number % 10
    #dezena é o número informado menos as unidades divido por 10
    ten = (((number - unit) / 10) % 10)
    #centenas é o número informado menos as unidades divido por 10 menos as dezenas dividido novamente por 10
    hundred = ((((number - unit) / 10)  - ten) / 10)
    print(f'\nO número {number:} tem {hundred:.0f} centena(s), {ten:.0f} dezena(s) e {unit} unidade(s).')