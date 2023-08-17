import datetime as dt

class Conta_Corrente:
    def __init__(self, numero_conta, nome_correntista_conta):
        self.numero_conta = numero_conta
        self.nome_correntista_conta = nome_correntista_conta
        self.__saldo_conta = 0

    def get_saldo(self):
        return self.__saldo_conta
    
    def set_nome_correntista(self, nome_correntista_conta: str):
        self.nome_correntista_conta = nome_correntista_conta
    
    def deposito_conta(self, valor_deposito: float):
        self.__saldo_conta += valor_deposito
        return self.__saldo_conta

    def saque_conta(self, valor_saque: float):
        if (valor_saque <= self.__saldo_conta):
            self.__saldo_conta -= valor_saque
        else:
            return -1
        return self.__saldo_conta
    
def informa_data_hora_momento():
    momento = dt.datetime.now()
    momento_escrito = momento.strftime("%d/%m/%Y %H:%M:%S")
    return momento_escrito

def converte_valor_monetario(value):
    x = "{:,.2f}".format(float(value))
    y = x.replace(',','x')
    z = y.replace('.',',')
    return z.replace('x','.')

def mostra_comprovante(comprovante, cc: Conta_Corrente, operacao: str, valor: float, legenda: str, mensagem: str = ''):
    if(cc.get_saldo() > 0):
        legenda_saldo = 'C'
    elif(cc.get_saldo() == 0):
        legenda_saldo = ''
    else:
        legenda_saldo = 'D'
    comprovante = (f'Data: {informa_data_hora_momento()}\n'
              f'Operação: {(operacao).upper()}: R$ {converte_valor_monetario(valor)}{legenda}\n'
              f'{mensagem}'
              f'SALDO: R$ {converte_valor_monetario(cc.get_saldo())}{legenda_saldo}.\n\n')
    return comprovante


#Teste
numero_conta = input('Digite o número da Conta:\n')
nome_correntista = input('Digite o Nome do Correntista:\n')

cc = Conta_Corrente(numero_conta, nome_correntista_conta=nome_correntista)

nome_banco = 'Curso Analista de Dados - Growdev'
cabecalho = (f'\n\n-----Banco {nome_banco}-----\n'
              f'Conta nr.: {cc.numero_conta}\n'               
              f'Nome Correntista: {cc.nome_correntista_conta}\n')
comprovante = ''
extrato = cabecalho + '-----\n'



while True:
    try: 
        opt = int(input('\nInforme a opção desejada:\n1 - Depósito\n2 - Saque\n3 - Alterar Nome do Correntista\n4 - Extrato\nQualquer outra Tecla - Sair\n'))
        if(opt == 1):
            operacao = 'Depósito'
            valor_deposito = float(input('\nInforme o valor que irá ser depositado: \n'))
            cc.deposito_conta(valor_deposito)
            comprovante = mostra_comprovante(comprovante, cc, operacao, valor_deposito, 'C')
            extrato += comprovante
            print(cabecalho + comprovante)
        elif(opt == 2):
            operacao = 'Saque'
            valor_saque = float(input('\nInforme o valor que irá ser sacado: \n'))
            if(cc.saque_conta(valor_saque) == -1):
                mensagem = 'Não foi possível concluir a operação: saldo insuficiente para saque.\n'
            else:
                mensagem = ''
            comprovante = mostra_comprovante(comprovante, cc, operacao, valor_saque, 'D', mensagem)
            extrato += comprovante
            print(f'{cabecalho} \n {comprovante}')
        elif(opt == 3):
            novo_nome_correntista = input('\nInforme o novo nome do correntista: \n')
            cc.set_nome_correntista(novo_nome_correntista)
            print(f'\nAlterado o nome do correntista para: {cc.nome_correntista_conta}')
        elif(opt == 4):
            print(f'{extrato}')
        else:
            break  
    except ValueError:
        break