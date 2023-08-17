'''
9)Uma caixa contém lâmpadas perfeitas ou defeituosas. Retira-se ao
acaso uma lâmpada da caixa. A probabilidade de se obter uma lâmpada
perfeita é dada por (n-82)/50, onde “n” é o número total de lâmpadas da caixa.
Qual é o número mínimo de lâmpadas que a caixa pode ter?
'''
#PE = probabilidade de um evento ocorrer em um universo de eventos: 0 <= PE <= 1
#PE = (n - 82) / 50

'''
 0 <= PE <= 1
 0 <= (n - 82) / 50 <= 1
 0 <= n - 82 <= 50
 82 <= n <= 132
'''

print(f'O número mínimo de lâmpadas é de 82.')