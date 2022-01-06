from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, agencia, banco, saldo = 0):
        self.numero = numero
        self.agencia = agencia
        self.banco = banco
        self.saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia

    @property
    def banco(self):
        return self.__banco

    @property
    def saldo(self):
        return self.__saldo

    @numero.setter
    def numero(self, numero_informado):
        if not isinstance(numero_informado, (int)):
            raise ValueError("A conta deve ser um valor nunérico inteiro")
        if len(str(numero_informado)) < 5:
            raise ValueError("O número da conta deve ter pelo menos 5 números")
        self.__numero = numero_informado

    @agencia.setter
    def agencia(self, agencia_informada):
        if not isinstance(agencia_informada, (int)):
            raise ValueError("A agencia deve ser um valor nunérico inteiro")
        if len(str(agencia_informada)) < 3:
            raise ValueError("O número da agência deve ter pelo menos 3 números")
        self.__agencia = agencia_informada

    @banco.setter
    def banco(self, banco_informado):
        if not isinstance(banco_informado, (int)):
            raise ValueError("O banco deve ser um valor nunérico inteiro")
        if len(str(banco_informado)) < 3:
            raise ValueError("O número do banco deve ter pelo menos 3 números")
        self.__banco = banco_informado

    @saldo.setter
    def saldo(self, saldo_informado):
        self.__saldo = saldo_informado

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Conta: {self.numero}', end=' ')
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Banco: {self.banco}', end=' ')
        print(f'Saldo: {self.saldo}', )

    @abstractmethod
    def sacar(self, valor):
        pass