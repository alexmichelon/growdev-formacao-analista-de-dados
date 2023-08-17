class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_x_y(self):
        print(f'Ponto x: {self.x}\nPonto y: {self.y}')

class Retangulo():
    def __init__(self, largura, altura, vertice_partida):
        self.largura = largura
        self.altura = altura
        self.vertice_partida = vertice_partida

    def encontrar_centro(self):
        centro_x = self.vertice_partida.x + (self.largura / 2)
        centro_y = self.vertice_partida.y + (self.altura/ 2)
        ponto = Ponto(centro_x, centro_y)
        return ponto


#Teste
ponto1 = Ponto(0, 0)
retangulo1 = Retangulo(largura=4, altura=2, vertice_partida=ponto1)
ponto2 = Ponto(2, 3)
retangulo2 = Retangulo(largura=5, altura=7, vertice_partida=ponto2)
ponto3 = Ponto(10, 5)
retangulo3 = Retangulo(largura=25, altura=15, vertice_partida=ponto3)
ponto4 = Ponto(1, 12)
retangulo4 = Retangulo(largura=95, altura=26, vertice_partida=ponto4)
ponto5 = Ponto(50, 68)
retangulo5 = Retangulo(largura=1125, altura=951, vertice_partida=ponto5)

ponto_centro = Ponto(0, 0)
ponto_centro = retangulo1.encontrar_centro()
print('Imprimir ponto vértice de partida:')
retangulo1.vertice_partida.imprimir_x_y()
print('Imprimir ponto do centro:')
ponto_centro.imprimir_x_y()