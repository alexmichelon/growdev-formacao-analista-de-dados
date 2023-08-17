print ('\nBem vindo ao Sistema Informa Melhor Show!!!\n')

publico_show_1 = 150
publico_show_2 = 180

custo_ingresso_a = 5
custo_ingresso_b = 5.5

despesa_a = 0.3
despesa_b = 0.5

show = 'Show 1'
faturamento = publico_show_1 * custo_ingresso_a
despesas_gerais = publico_show_1 * despesa_a
lucro = faturamento - despesas_gerais
melhor_show = show
maior_lucro = lucro
custo_ingresso_maior_lucro = custo_ingresso_a
despesa_maior_lucro = despesa_a
print(f'O lucro do {show} com custo do ingresso R$ {custo_ingresso_a:.2f} e despesa por pessoa R$ {despesa_a:.2f} é de R$ {lucro:.2f}.')

faturamento = publico_show_1 * custo_ingresso_b
despesas_gerais = publico_show_1 * despesa_b
lucro = faturamento - despesas_gerais
if(lucro > maior_lucro):
    maior_lucro = lucro
    custo_ingresso_maior_lucro = custo_ingresso_b
    despesa_maior_lucro = despesa_b
print(f'O lucro do {show} com custo do ingresso R$ {custo_ingresso_b:.2f} e despesa por pessoa R$ {despesa_b:.2f} é de R$ {lucro:.2f}.')

show = 'Show 2'
faturamento = publico_show_2 * custo_ingresso_a
despesas_gerais = publico_show_2 * despesa_a
lucro = faturamento - despesas_gerais
print(f'O lucro do {show} com custo do ingresso R$ {custo_ingresso_a:.2f} e despesa por pessoa R$ {despesa_a:.2f} é de R$ {lucro:.2f}.')
if(lucro > maior_lucro):
    melhor_show = show
    maior_lucro = lucro
    custo_ingresso_maior_lucro = custo_ingresso_a
    despesa_maior_lucro = despesa_a

faturamento = publico_show_2 * custo_ingresso_b
despesas_gerais = publico_show_2 * despesa_b
lucro = faturamento - despesas_gerais
print(f'O lucro do {show} com custo do ingresso R$ {custo_ingresso_b:.2f} e despesa por pessoa R$ {despesa_b:.2f} é de R$ {lucro:.2f}.')
if(lucro > maior_lucro):
    melhor_show = show
    maior_lucro = lucro
    custo_ingresso_maior_lucro = custo_ingresso_b
    despesa_maior_lucro = despesa_b

print(f'O maior lucro é R$ {maior_lucro:.2f} do {melhor_show} com custo do ingresso R$ {custo_ingresso_maior_lucro:.2f} e despesa por pessoa R$ {despesa_maior_lucro:.2f}.')    
