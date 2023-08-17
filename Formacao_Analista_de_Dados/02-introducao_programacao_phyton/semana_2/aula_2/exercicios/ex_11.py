'''
11) Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja
200000 habitantes com uma taxa de crescimento de 1.5%. Faça um
programa que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.
'''

country_A = 80000
country_B = 200000

tax_country_A = 0.03
tax_country_B = 0.015

amount_years = 0

print('\nBem vindo ao sistema Comparação de Crescimento de Cidades!!!!\n')

while(country_A <= country_B):
    amount_years += 1

    country_A += tax_country_A
    country_B += tax_country_B

    #print(f'Ano {amount_years}: População Cidade A: {country_A:.2f} habitantes, População Cidade B: {city_B:.2f} habitantes.')

print(f'\nSerão necessários {amount_years} anos para o país A (terá {country_A:.2f}m) tenha mais habitantes que o país B (que terá {country_B:.2f}m).')