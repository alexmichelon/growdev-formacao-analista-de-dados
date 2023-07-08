'''3) Uma empresa que realiza shows planeja realizar 2 shows em uma
determinada cidade. Espera-se que os shows tenham um público
esperado de 150, 180 espectadores respectivamente. E existem 2
possibilidades de cobrança de ingressos.
a) Custo do ingresso: R$ 5,00. Despesas show: R$ 0,30 por pessoa.
b) Custo do ingresso: R$ 5,50. Despesas show: R$ 0,50 por pessoa.
Você pode escolher apenas uma opção. Informe qual a melhor
opção a através da escrita de um programa Python, exibindo qual o total
de faturamento, lucro e despesas gerais em cada um dos shows, em cada
um dos cenários possíveis.'''

def calculate_invoicing(spectators, line):
    invoicing = spectators * ticket_options[line][0]
    return invoicing

def calculate_general_costs(spectators, line):
    general_costs= spectators * ticket_options[line][1]
    return general_costs

def calculate_profit(invoicing, general_costs):
    profit = invoicing - general_costs
    return profit

def index_bigger_profit(list):
    max_value = None
    option = None
    for idx, value in enumerate(list):
        if (max_value is None or value > max_value):
            position = idx
    return position

print('\nBem vindo ao Sistema Escolha do Melhor Show!!\n')

#listas possuem os valores (faturamento, custos gerais, lucro, tipo de ingresso)
show_1 = []
show_2 = []
spectators_1 = 150
spectators_2 = 180
ticket_cost_a = 5
ticket_cost_b = 5.5
concert_expense_a = 0.3
concert_expense_b = 0.5

ticket_options = ([ticket_cost_a, concert_expense_a], [ticket_cost_b, concert_expense_b])

for i in range (2):   
    show_1.append([])
    show_2.append([])
    for j in range (1,2):        
        
        invoicing = calculate_invoicing(spectators_1, i) 
        general_costs = calculate_general_costs(spectators_1, i)
        profit = calculate_profit(invoicing, general_costs)       
        show_1[i].append(invoicing)
        show_1[i].append(general_costs)
        show_1[i].append(profit)
        show_1[i].append(i)


        invoicing = calculate_invoicing(spectators_2, i) 
        general_costs = calculate_general_costs(spectators_2, i)
        profit = calculate_profit(invoicing, general_costs)
        show_2[i].append(invoicing)
        show_2[i].append(general_costs)
        show_2[i].append(profit)
        show_2[i].append(i)

for i in range(2):
    print(f'Show 1: Espectadores {spectators_1}, Faturamento R$ {show_1[i][0]:.2f}, Despesas Gerais R$ {show_1[i][1]:.2f}, Lucro R$ {show_1[i][2]:.2f}.')
    print(f'Show 2: Espectadores {spectators_2}, Faturamento R$ {show_2[i][0]:.2f}, Despesas Gerais R$ {show_2[i][1]:.2f}, Lucro R$ {show_2[i][2]:.2f}.')

bigger_profit_1 = max([value[2] for value in show_1])
bigger_profit_2 = max([value[2] for value in show_2])

if(bigger_profit_1 > bigger_profit_2):
    position = index_bigger_profit(show_1)
    print(f'\nA melhor opção é Show 1, com valor de ingresso R$ {ticket_options[position][0]:.2f}, com custo por pessoa de R$ {ticket_options[position][1]:.2f}. Irá gerar lucro de R$ {bigger_profit_1:.2f}')
else:
    position = index_bigger_profit(show_2)
    print(f'\nA melhor opção é Show 2, com valor de ingresso R$ {ticket_options[position][0]:.2f}, com custo por pessoa de R$ {ticket_options[position][1]:.2f}. Irá gerar lucro de R$ {bigger_profit_2:.2f}')