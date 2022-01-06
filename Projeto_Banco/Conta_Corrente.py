from Projeto_Banco.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, banco, saldo=0, limite = 100):
        # Precisamos iniciar a classe Super
        Conta.__init__(self, numero, agencia, banco, saldo=0)
        self.limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor_limite):
        self.__limite = valor_limite

    def sacar(self, valor_solicitado):
        if ((self.saldo + self.limite) - valor_solicitado) == 0 or ((self.saldo + self.limite) - valor_solicitado) < 0:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor_solicitado
            self.detalhes()
            input("Pressione ENTER para continuar")

