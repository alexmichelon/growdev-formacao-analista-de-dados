import numpy as np

list_coordinates = np.array(
   [
   [0.0,0.0],
   [0.0,0.0]
   ]
)

def convert_coma_point(value):
 if(value.count(',') > 0):
    value = value.replace(',', '',value.count(',')-1).replace(',','.')
 if (value.count('.') > 1):     
    value = value.replace('.', '',value.count('.')-1)
 return value

def validate_number(order):
    value = input(order)
    while(not value.replace(',','').replace('.', '').isdigit()):
        value = input('\nEntrada Inválida!\n' + order + '\n')
    value = convert_coma_point(value)
    return float((value))

 
def inform_coordinate():
    for i in range(2):
        for j in range(2):
            if(i == 0):
                point = 'A'
            else:
               point = 'B'
            if(j == 0):
               coordinate = 'X'
            else:
               coordinate = 'Y'            
            list_coordinates[i, j] = validate_number('Informe a coordenada ' + coordinate + ' para o ponto ' + point + ': ')

def calculate_distance(list_coordinates):
    #fórmula teorema de Pitágoras: Dab² = (Xb - Xa)² + (Yb - Ya)²
    distance_points = (((list_coordinates[1,0] - list_coordinates[0,0]) ** 2) + ((list_coordinates[1,1] - list_coordinates[0,1]) ** 2) ) ** (1/2)
    return distance_points

print('\nBem vindo ao sistema Cálculo da Distância de Dois Pontos em um Plano 2D!\n')

inform_coordinate()
print('\nCoordenadas informadas: \n' + str(list_coordinates))
print('\nA distância entre as coordenadas informadas é: '  + str(float(round(calculate_distance(list_coordinates),4))))


