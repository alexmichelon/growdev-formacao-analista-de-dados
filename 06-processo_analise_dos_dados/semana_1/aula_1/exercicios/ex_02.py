class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def set_base(self, base):
        self.base = base

    def set_altura(self, altura):
        self.altura = altura        

    def get_base(self):
        return self.base
        
    def get_altura(self):
        return self.altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (self.base + self.altura) * 2
    
#Teste
base = float(input('Digite a medida da base: '))
altura = float(input('Digite a medida da altura: '))
retangulo = Retangulo(base=base, altura=altura)
print(f'A medida da base do local é: {retangulo.get_base()} mts.')
print(f'A medida da altura do local é: {retangulo.get_altura()} mts.')
print(f'A quantidade de pisos (1m²) necessários para o local é de {round(retangulo.calcular_area())} unidades. ')
print(f'A quantidade de rodapés (1m) necessários para o local é de {round(retangulo.calcular_perimetro())} unidades. ')