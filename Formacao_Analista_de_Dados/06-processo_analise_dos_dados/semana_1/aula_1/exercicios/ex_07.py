class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.__quantidade_litros_combustivel_no_tanque = 0

    def atualizar_consumo(self, consumo):
        self.consumo = consumo

    def andar(self, distancia):
        litros_distancia = distancia / self.consumo
        if(litros_distancia <= self.__quantidade_litros_combustivel_no_tanque):
            self.__quantidade_litros_combustivel_no_tanque -= litros_distancia
            return litros_distancia
        else:
            return False
        
    def obter_gasolina(self):
        return self.__quantidade_litros_combustivel_no_tanque
    
    def adicionar_gasolina(self, quantidade_litros_adicionado):
        self.__quantidade_litros_combustivel_no_tanque += quantidade_litros_adicionado

    def mostrar_estado_carro(self):
        print(f'Consumo: {self.consumo:.2f} quilômetros/litro\n'
              f'Quantidade de Combustível no tanque: {self.__quantidade_litros_combustivel_no_tanque:.2f} litros.\n'
              f'Autonomia: {(self.consumo * self.__quantidade_litros_combustivel_no_tanque):.2f} quilômetros.')


#Teste
consumo = 7
meu_carro = Carro(consumo=consumo)
print('Bem vindo ao programa que simula percorrer distâncias com o Carro!\n')    
abastecer = float(input('O tanque está vazio. É hora de abastecer o carro!.\nInforme a quantidade de litros para abastecer:\n'))
meu_carro.adicionar_gasolina(abastecer)

while True:
    try: 
        opt = int(input('\n1 - Para percorrer quilometragem\n'
                    '2 - Para ver nível de combustível no tanque\n'
                    '3 - Para abastecer\n'
                    '4 - Para atualizar consumo quilômetros/litro\n'
                    'Qualquer outra tecla para sair\n'))
        if(opt == 1):
            distancia = float(input('Quantidade de quilômetros (kms):\n'))
            if(meu_carro.andar(distancia) == False):
               print('Não há combustível suficiente para percorrer a distância informada. Abasteça o carro!')
            meu_carro.mostrar_estado_carro()
        elif(opt == 2):
            print('\nOlhe o status do carro:')
            meu_carro.mostrar_estado_carro()
        elif(opt == 3):
            abastecer = float(input('Informe quantidade de gasolina abastecida (litros):\n'))
            meu_carro.adicionar_gasolina(abastecer)
        elif(opt == 4):
            consumo = float(input('Informe consumo do carro (quilômetros/litro:)\n'))
            meu_carro.atualizar_consumo(consumo)
        else:
            print('Opção Inválida!')
    except ValueError: 
        break