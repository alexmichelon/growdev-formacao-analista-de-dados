class BombaCombustivel():
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    #método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    def abastecer_por_valor(self, valor_abastecido):
        quantidade_litros_combustivel_colocado_carro = valor_abastecido / self.valor_litro
        if(quantidade_litros_combustivel_colocado_carro <= self.quantidade_combustivel):
            self.quantidade_combustivel -= quantidade_litros_combustivel_colocado_carro
            return valor_abastecido
        else:
            return False
    
    #método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    def abastecer_por_litro(self, quantidade_litros_combustivel_colocado_carro):
        valor_pago = quantidade_litros_combustivel_colocado_carro * self.valor_litro
        if(quantidade_litros_combustivel_colocado_carro <= self.quantidade_combustivel):
            self.quantidade_combustivel -= quantidade_litros_combustivel_colocado_carro
            return valor_pago
        else:
            return False
    
    #altera o valor do litro do combustível.
    def alterar_valor(self, valor):
        self.valor_litro = valor

    #altera o tipo do combustível.
    def alterar_combustivel(self, tipo):
        self.tipo_combustivel = tipo

    #altera a quantidade de combustível restante na bomba.
    def alterar_quantidade_combustivel(self, quantidade_combustivel):
        self.quantidade_combustivel = quantidade_combustivel

    def mostrar_dados_bomba(self):
        print(f'Tipo de Combustível: {self.tipo_combustivel}\n'
              f'Valor por litro R$ {self.valor_litro:.2f}\n'
              f'Quantidade de Combustível: {self.quantidade_combustivel:.2f} litros.\n\n')


#Teste
tipo_combustivel = 'Gasolina'
valor_litro = 5.70
quantidade_combustivel = 1000.0

bomba = BombaCombustivel(tipo_combustivel=tipo_combustivel, valor_litro=valor_litro, quantidade_combustivel=quantidade_combustivel)

print('Bem vindo ao sistema da Bomba de Combustíveis!')
while True:
    try:
        opt = int(input('Escolha a opção:\n'
                '1 - Abastecer por valor\n'
                '2 - Abastecer por litro\n'
                '3 - Alterar valor do litro do combustível\n'
                '4 - Alterar tipo de combustível\n'
                '5 - Alterar quantidade de Combustível da Bomba\n'
                'Aperte qualquer outra tecla para sair.\n'))
    except ValueError:
        print('Opção Inválida!')
        break

    try:
        if(opt == 1):
            valor = float(input('\nInforme o valor a ser abastecido R$: '))
            if(bomba.abastecer_por_valor(valor) == False):
                print('\nNão há combustível suficiente na bomba.')
            bomba.mostrar_dados_bomba()
        elif(opt == 2):
            quantidade_litros = float(input('\nInforme a quantidade de litros para abastecer: '))
            if(bomba.abastecer_por_litro(quantidade_litros) == False):
                print('\nNão há combustível suficiente na bomba.')
            bomba.mostrar_dados_bomba()
        elif(opt == 3):
            valor_litro = float(input('\nInforme novo valor do combustível por litro R$: '))
            bomba.alterar_valor(valor_litro)
            bomba.mostrar_dados_bomba()
        elif(opt == 4):
            tipo_combustivel = input('\nInforme o tipo de combustível: ')
            bomba.alterar_combustivel(tipo_combustivel)
            bomba.mostrar_dados_bomba()
        elif(opt == 5):
            quantidade_combustivel = float(input('\nInforme quantidade de combustível: '))
            bomba.alterar_quantidade_combustivel(quantidade_combustivel)
            bomba.mostrar_dados_bomba()
        else:
            break
    except ValueError:
        print('\nTipo de dado inválido!\n')
        continue