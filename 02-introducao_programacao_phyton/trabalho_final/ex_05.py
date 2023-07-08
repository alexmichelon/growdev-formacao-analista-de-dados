'''5) Duas pessoas possuem respectivamente 1,85 e 1,64 de altura e 56 e
35 anos. A primeira cresce 0,03 cm por ano e a segunda cresce
0,045 cm por ano. Quantos anos serão necessários para que a
segunda pessoa alcance ou supere a altura da primeira?. Levando
em consideração que o limite de idade é de 110 anos para ambas.'''

print('\nBem vindo ao Sistema Comparação de Crescimento de Alturas!\n')

person_1_age = 56
person_2_age = 35
person_1_height = 1.85
person_2_height = 1.64
person_1_grow = 0.03
person_2_grow = 0.045
year = 0
age_limit = 110

while(person_1_height > person_2_height) and (person_1_age < age_limit) and (person_2_age < age_limit):
    person_1_height += person_1_grow
    person_2_height += person_2_grow

    person_1_age += 1
    person_2_age += 1
    year += 1

if(person_1_age >= age_limit) or (person_2_age >= age_limit):
    print(f'A segunda pessoa não alcançou a primeira em altura após passarem-se {year} anos:\n'
          f'Primeira pessoa: {person_1_age} anos de idade e {person_1_height:.2f} m de altura.\n'
          f' Segunda pessoa: {person_2_age} anos de idade e {person_2_height:.2f} m de altura.\n')
else:
    print(f'\nQuantidade de anos: {year}\n'
          f'Primeira pessoa: {person_1_age} anos de idade e {person_1_height:.2f} m de altura.\n'
          f' Segunda pessoa: {person_2_age} anos de idade e {person_2_height:.2f} m de altura.\n')