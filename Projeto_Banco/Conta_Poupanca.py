from Projeto_Banco.Conta import Conta

class ContaPoupanca(Conta):

    def sacar(self, valor_solicitado):
        if (self.saldo - valor_solicitado) == 0 or (self.saldo - valor_solicitado) < 0:
            print("Saldo insuficiente")
            input("Pressione ENTER para continuar")
        else:
            self.saldo -= valor_solicitado
            self.detalhes()
            input("Pressione ENTER para continuar")
