class Bola:
    def __init__(self):
        self.cor = ''
        self.circunferencia = 0.0
        self.material = ''

    def  set_cor(self, cor:str):
        self.cor = cor
    
    def mostra_cor(self):
        return self.cor    
    
#Teste
bola = Bola()
cor = input('Digite uma cor para a bola: ')
bola.set_cor(cor)
print(f'A cor da bola é: {bola.mostra_cor()}')