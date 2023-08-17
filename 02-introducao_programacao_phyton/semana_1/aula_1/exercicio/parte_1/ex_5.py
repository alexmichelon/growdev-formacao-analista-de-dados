
resultado = 0
valorInformado = 0
operacao = ''
texto = ''

def adicao(resultado, valorInformado):
 resultado = (float(resultado) + float(valorInformado))
 return resultado

def substracao(resultado, valorInformado):
 resultado = (float(resultado) - float(valorInformado))
 return resultado

def multiplicacao(resultado, valorInformado):
 resultado = (float(resultado) * float(valorInformado))
 return resultado

def divisao(resultado, valorInformado):
 resultado = (float(resultado) / float(valorInformado))
 return resultado


def validaOperacao(operacao):
 operacao = input('Informe a operação desejada: +, -, *, / ou X para sair:  ').upper()
 while(operacao not in ('+','-', '*', '/', 'X')):
  operacao = input('Entrada inválida! Informe a operação desejada: +, -, *, /  ou X para sair:  ').upper()
 return operacao

def converte_virgula_ponto(numero):
 if(numero.count(',') > 0):
    numero = numero.replace(',', '',numero.count(',')-1).replace(',','.')
 if (numero.count('.') > 1):     
    numero = numero.replace('.', '',numero.count('.')-1)
 return numero

def validaNumero():
  numero = input('Informe o número: ')
  while(not numero.replace('-','').replace(',','').replace('.','').isdigit()):
    print('Entrada inválida! Informe um número válido: ')
    numero = input() 
  numero = converte_virgula_ponto(numero)
  return numero 
 

print('\nBem vindo ao sistema Calculadora Digital!\n')
resultado = validaNumero()
texto = resultado

while(operacao != 'X'):
  operacao = validaOperacao(operacao).upper()
  if (operacao == 'X'):
    break
  valorInformado = validaNumero()
  texto = str(texto) + ' ' + operacao + ' ' + valorInformado

  if(operacao == '+'):
    resultado = adicao(resultado, valorInformado)
    texto = texto + ' = ' + str(resultado)
    print(texto)
  elif(operacao == '-'):
    resultado = substracao(resultado, valorInformado)
    texto = texto + ' = ' + str(resultado)
    print(texto)
  elif(operacao == '*'):
    resultado = multiplicacao(resultado, valorInformado)
    texto = texto + ' = ' + str(resultado)
    print(texto)
  elif(operacao == '/'):
    resultado = divisao(resultado, valorInformado)
    texto = texto + ' = ' + str(resultado)
    print(texto)
  else: 
    break

