arrozNoPonto = 'N'

input('\nBem vindo ao Sistema "Como preparar Arroz"!!!\nFavor, onde não solicitar entrada, favor teclat ENTER\n')
input('Escolha uma panela e a coloque sobre o queimador (boca) do fogão \n')
input('Pegue o pacote de arroz e o abra \n')
input('Coloque o arroz na panela. Obs.: comumente a medida é de meia xícara de arroz por pessoa \n')
input('Coloque azeite sobre o arroz dentro da panela \n')
input('Acenda o queimador (boca) do fogão sobre o qual está a panela \n')
input('Com uma colher, mexa o arroz com azeite na panela até que os grãos fiquem totalmente banhados pelo azeite \n')
input('Coloque água dentro da panela o suficiente para cobrir o arroz.\nObs.: após a água cobrir o arroz, adicionar preferencialmente uma nova xícara de água e tampe a panela\n')
input('Observe quando a água começar a borbulhar pois é o momento de adicionar sal a gosto \n')
input('Após adicionar o sal, tampe parcialmente a panela deixando uma pequena fresta entre a tampa e a panela\n')
input('Observe que quando a água chegar no mesmo nível do arroz, diminua o fogo do queimador (boca) do fogão até o menor nível \n')
 
while arrozNoPonto not in ('S'): 
  input('Assim que a água secar totalmente na panela, pegue a colher e prove alguns grãos do arroz \n')
  arrozNoPonto = input('O arroz está no ponto desejado? S/N: \n').upper()
  if (arrozNoPonto  == 'S'):
    break
  elif(arrozNoPonto == 'N'):
    input('\nColoque água dentro da panela o suficiente para cobrir o arroz. \n')
  else:
    while (arrozNoPonto not in ('S','N')):
      arrozNoPonto = input(('\nEntrada inválida!\n O arroz está no ponto desejado? S/N: \n')).upper()

input('\nO arroz está pronto!. Obs.: é importante deixar o arroz descansar por 5 minutos antes de comer. \n\n'
      'BOM APETITE!!!')