'''
Utilize as seguintes faixas etárias nos exercícios em que for necessário.
● Jovens, 18 a 25 anos
● Adultos, 26 a 59 anos
● Idosos, igual ou maior que 60 anos

Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
exercícios.

1) Qual a porcentagem de homens e mulheres na base de dados?
2) Qual foi o gasto por ano?
3) Qual foi o ano com maior gasto?
4) Qual foi o ano em que os homens mais usaram o crédito?
5) Procure quem foi a pessoa que mais gastou?
'''

file_name = 'dados/compras.csv'

file = open(file_name, 'r')

content = file.readlines()

header = content[0]
data = content[1:]

people = []

for line in data:
    record = line.split(',')
    person = {
        'name': record[0],
        'last_name': record[1],
        'age': int(record[2]),
        'sex': record[3],
        'purchase': float(record[4]),
        'year': int(record[5]),
        'payment': record[6].replace('\n','')
    }
    
    people.append(person)

amount_records = len(data)


#1) Qual a porcentagem de homens e mulheres na base de dados?
print('\n------\n1) Qual a porcentagem de homens e mulheres na base de dados?')
amount_men = 0
amount_women = 0

for i in range(amount_records):
    person = people[i]
    if(person['sex'] == 'M'):
        amount_men += 1
    else:
        amount_women += 1

percent_men = (amount_men * 100) / amount_records
percent_women = (amount_women * 100) / amount_records

print(f'Existem {amount_records} pessoas na base de dados.')
print(f'Existem {amount_men} homens, correspondendo a {percent_men:.2f}% do total.')
print(f'Existem {amount_women} mulheres, corrrespondendo a {percent_women:.2f}% do total.')


#2) Qual foi o gasto por ano?
print('\n------\n2) Qual foi o gasto por ano?')
spent_per_year = {}

for p in people:
    spent_per_year[p['year']] = spent_per_year.get(p['year'], 0) + p['purchase']

for year in sorted(spent_per_year.keys()):
    print(f'Ano: {year}, Gasto R$: {spent_per_year[year]:.2f}')

total = 0
for p in people:
    total += p['purchase']
print(f'Total gasto em todos os anos R$ {total:.2f}.')


#3) Qual foi o ano com maior gasto?
print('\n------\n3) Qual foi o ano com maior gasto?')
spentest_year = max(spent_per_year, key=spent_per_year.get)
spentest_year_purchase = spent_per_year[max(spent_per_year, key=spent_per_year.get)]
print(f'O ano com maior valor gasto foi {spentest_year}, com gasto de R$ {spentest_year_purchase:.2f}.')


#4) Qual foi o ano em que os homens mais usaram o crédito?
print('\n------\n4) Qual foi o ano em que os homens mais usaram o crédito?')
men_use_credit_per_year = {}
biggest_year_men_use_credit = 0
for p in people:
    if (p['sex'] == 'M') and (p['payment'] == 'credito'):
        men_use_credit_per_year[p['year']] =  men_use_credit_per_year.get(p['year'], 0) + 1

biggest_year_men_use_credit = max(men_use_credit_per_year, key=men_use_credit_per_year.get)
print(f'O ano com maior uso de crédito por homens foi {biggest_year_men_use_credit}.')


#5) Procure quem foi a pessoa que mais gastou?
print('\n------\n5) Procure quem foi a pessoa que mais gastou?')
people_whit_fullname = []

for line in people:
    person = {
        'fullname': line['name'] + ' ' + line['last_name'],
        'birth_year': line['year'] - line['age'],
        'age': line['age'],
        'sex': line['sex'],
        'purchase': line['purchase'],
        'year': line['year'],
        'payment': line['payment']
    }

    people_whit_fullname.append(person)

spent_per_person = {}
for p in people_whit_fullname:
    spent_per_person[p['fullname'], p['birth_year']] = spent_per_person.get(p['fullname'], 0) + spent_per_person.get(p['birth_year'], 0) + p['purchase']

highest_spenter = max(spent_per_person, key=spent_per_person.get)
highest_spenter_purchase = spent_per_person[max(spent_per_person, key=spent_per_person.get)]

print(f'A pessoa que mais gastou foi: {highest_spenter[0]}, nascido no ano de {highest_spenter[1]}, gastou um total de R$ {highest_spenter_purchase:.2f}.')