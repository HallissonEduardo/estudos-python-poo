"""Criando classe conta_bancaria"""

class Conta_bancaria:

    """Metodo construtor com saldo e nome do titular da conta bancaria"""
    def __init__(self, titular, saldo):

        # Atributos
        self.titular = titular
        self.saldo = saldo
        self.valor = 0

    # Método Deposito
    def depositar(self,valor):
        self.saldo = self.saldo + valor
        if self.saldo:
            self.saldo += valor
            print(f'Titular: {self.titular}, Saldo: {self.saldo}')

        else:
            print('VALOR INVALIDO! DEPOSITOS SÓ SÃO PERMITIDOS A CIMA DE R$ 1 REAL')

    def sacar(self,valor):
        self.saldo = self.saldo - valor
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Titular: {self.titular}, Saldo: {self.saldo}')

        else:
            print(f'Saldo insuficiente!')

if __name__ == '__main__':

    cliente = Conta_bancaria('Gabriel', 100)

    cliente.depositar(888)
    cliente.depositar(200)
    cliente.depositar(300)

    cliente.sacar(100)

    #cliente.sacar(600)
