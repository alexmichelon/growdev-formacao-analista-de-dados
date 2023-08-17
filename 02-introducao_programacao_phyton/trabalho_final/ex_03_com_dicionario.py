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
    if(line == 0):
        invoicing = spectators * ticket_options.get('ticket_cost_a')
        return invoicing, ticket_cost_a
    else:
        invoicing = spectators * ticket_options.get('ticket_cost_b')
        return invoicing, ticket_cost_b
    

def calculate_general_costs(spectators, line):
    if(line == 0):
        general_costs= spectators * ticket_options.get('concert_expense_a')
        return general_costs, concert_expense_a
    else:
        general_costs= spectators * ticket_options.get('concert_expense_b')
        return general_costs, concert_expense_b    

def calculate_profit(invoicing, general_costs):
    profit = invoicing - general_costs
    return profit

shows = []
amount_shows = 2
spectators_show_1 = 150
spectators_show_2 = 180
ticket_cost_a = 5
ticket_cost_b = 5.5
concert_expense_a = 0.3
concert_expense_b = 0.5
bigger_profit = 0.00

ticket_options = {'ticket_cost_a': float(ticket_cost_a),
                   'concert_expense_a': float(concert_expense_a), 
                   'ticket_cost_b': float(ticket_cost_b), 
                   'concert_expense_b': float(concert_expense_b)}

print('\nBem vindo ao Sistema Escolha do Melhor Show!!\n')

for i in range (0, amount_shows, 1):
    #laço para determinar qual show está sendo avaliado e inserido na lista shows
    for j in range(1, amount_shows+1, 1):
        if(j == 1):
            spectators = spectators_show_1
        else:
            spectators = spectators_show_2
        invoicing, ticket_cost = calculate_invoicing(spectators, i) 
        general_costs, concert_expense = calculate_general_costs(spectators, i)
        profit = calculate_profit(invoicing, general_costs)       
        show = {'show': int(j), 
                'spectators': spectators, 
                'ticket_cost': float(ticket_cost), 
                'concert_expense': float(concert_expense), 
                'invoicing': float(invoicing), 
                'general_costs': float(general_costs), 
                'profit': float(profit)}
        shows.append(show)

for show in shows:
    if(show.get('profit') > bigger_profit):
        best_show = show
    print(f'Show: {show.get("show")}, '
          f'{show.get("spectators")} Espectadores, '
          f'Custo do Ingresso R$: {show.get("ticket_cost"):.2f}, ' 
          f'Custo por Pessoa R$: {show.get("concert_expense"):.2f}, ' 
          f'Faturamento R$ {show.get("invoicing"):.2f}, ' 
          f'Despesas Gerais R$ {show.get("general_costs"):.2f}, ' 
          f'Lucro R$ {show.get("profit"):.2f}.')

print('\n\nA opção com melhor lucro é:\n'
     f'Show: {best_show.get("show")}, '   
     f'{best_show.get("spectators")} Espectadores, '
     f'Custo do Ingresso R$: {best_show.get("ticket_cost"):.2f}, '
     f'Custo por Pessoa R$: {best_show.get("concert_expense"):.2f}, '
     f'Faturamento R$ {best_show.get("invoicing"):.2f}, '
     f'Despesas Gerais R$ {best_show.get("general_costs"):.2f}, '
     f'Lucro R$ {best_show.get("profit"):.2f}.')