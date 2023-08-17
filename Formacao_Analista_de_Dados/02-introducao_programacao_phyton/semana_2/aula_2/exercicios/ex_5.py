'''
5) Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
metro e cresce 3 centímetros por ano. Construa um programa que calcule e
imprima quantos anos serão necessários para que Zé seja maior que Chico.
'''

height_chico = 1.5
height_ze = 1.1

tax_height_chico = 0.02
tax_height_ze = 0.03

amount_years = 0

print('\nBem vindo ao sistema Comparação de Alturas de Chico e Zé!!!!\n')

while(height_chico > height_ze):
    amount_years += 1

    height_chico += tax_height_chico
    height_ze += tax_height_ze

    print(f'Ano {amount_years}: Altura de Chico: {height_chico:.2f}m, Altura de Zé: {height_ze:.2f}m')

print(f'\nSerão necessários {amount_years} anos para que Zé (terá {height_ze:.2f}m) seja maior que Chico (que terá {height_chico:.2f}m).')
    