class Tamagochi():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def set_nome(self, nome):
        self.nome = nome
    
    def set_fome(self, fome):
        self.fome = fome

    def set_saude(self, saude):
        self.saude = saude

    def set_idade(self, idade):
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return self.fome
    
    def get_saude(self):
        return self.saude
    
    def get_idade(self):
        return self.idade
    
#Teste
tamagochi = Tamagochi('', '', '', 0)
opt = 1
print('\nBem-vindo ao programa do Tamagochi!!!\n')
while opt == 1:    
    nome = input('Informe o nome: ')
    fome = input('Informe o grau de fome: ')
    saude = input('Informe o status de saúde: ')
    while True: 
        try: 
            idade = int(input('Informe a idade: '))
            break
        except ValueError:
            continue
        
    tamagochi.set_nome(nome)
    tamagochi.set_fome(fome)
    tamagochi.set_saude(saude)
    tamagochi.set_idade(idade)

    print('\n-----\nTamagochi-----')
    print(f'Nome: {tamagochi.get_nome()}')
    print(f'Fome: {tamagochi.get_fome()}')
    print(f'Saude: {tamagochi.get_saude()}')
    print(f'Idade: {tamagochi.get_idade()}\n-----')

    try: 
        opt = int(input('\nDeseja alterar dados do Tamagochi? \nClique 1 para Sim\nQualquer tecla para sair: '))    
    except ValueError :
        break