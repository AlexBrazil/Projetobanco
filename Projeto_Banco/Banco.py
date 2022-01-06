from Projeto_Banco.Cliente import Cliente
from Projeto_Banco.Conta_Corrente import ContaCorrente
from Projeto_Banco.Conta_Poupanca import ContaPoupanca
from time import sleep


class Banco():
    #codigo_banco = 100
    def __init__(self):
        self.__contas = []
        self.__clientes = []
        self.__clienteVconta = {}

    @property
    def contas(self):
        return self.__contas

    def contaVinculadaCliente(self, numero):
        # print(f'self.__clienteVconta.values() {self.__clienteVconta.keys()}')
        # print('RETORNO DA CONTA')
        for cpf, contas in self.__clienteVconta.items():
            for conta in contas:
                if conta == numero:
                    return self.retornaContaPeloNumero(numero)
        return None


    def retornaClientePeloCPF(self, cpf: str):

        for item in self.__clientes:
            if item.cpf == cpf:
                return item
        return None
    def retornaContaPeloNumero(self, numero: int):

        for item in self.__contas:
            # print(f'print(type(item.numero)) - {type(item.numero)} - {item.numero}')
            # print(f'numero - {type(numero)} - {numero}')
            if item.numero == numero:
                return item
        return None


    @property
    def clientes(self):
        return self.__clientes

    def contaJaExiste(self, contaParaAvaliar):
        for conta in self.__contas:
            print(f'conta.numero: {conta.numero} - contaParaAvaliar.numero: {contaParaAvaliar.numero}')
            if conta.numero == contaParaAvaliar.numero:
                return True
        return False

    def clienteJaExiste(self, clienteParaAvaliar):
        for cliente in self.__clientes:
            print(f'Cliente.cpf: {cliente.cpf} - clienteParaAvaliar.cpf: {clienteParaAvaliar.cpf}')
            if cliente.cpf == clienteParaAvaliar.cpf:
                return True
        return False

    def add_conta(self, conta: (ContaCorrente, ContaPoupanca)):
        # print(f'Detalhes da conta recebida: {conta.detalhes()}')
        # print('*' * 80)
        if len(self.__contas) == 0:
            self.__contas.append(conta)
        else:
            if self.contaJaExiste(conta):
                print("Conta já Cadastrada")
                sleep(3)
            else:
                self.__contas.append(conta)

    def add_cliente(self, cliente: Cliente):
        if len(self.__clientes) == 0:
            self.__clientes.append(cliente)
        else:
            if self.clienteJaExiste(cliente):
                print("Cliente já Cadastrado")
                sleep(3)
            else:
                self.__clientes.append(cliente)


    def addClienteXConta(self, clienteParaAdiconar: Cliente, contaParaAdicionar: (ContaCorrente, ContaPoupanca)):
        # Caso o cliente ainda não cadastrado
        if not (clienteParaAdiconar.cpf in self.__clienteVconta):
            self.__clienteVconta[clienteParaAdiconar.cpf] = [contaParaAdicionar.numero]
        else:
            # Vamos procurar se a conta já está cadastrada para o cliente
            if(contaParaAdicionar.numero in self.__clienteVconta[clienteParaAdiconar.cpf]):
                print(f'O cliente {clienteParaAdiconar.nome} já possui a conta {contaParaAdicionar.numero}')
                sleep(3)
            else:
                self.__clienteVconta[clienteParaAdiconar.cpf].append(contaParaAdicionar.numero)

            print(f'contaParaAdicionar.numero - {contaParaAdicionar.numero} \n self.__clienteVconta[clienteParaAdiconar.cpf] - {self.__clienteVconta[clienteParaAdiconar.cpf]}')
            sleep(3)


    def contaClientesComConta(self) -> int:
        return len(self.__clienteVconta)

    def conta_contas(self) -> int:
        return len(self.__contas)


    def conta_clientes(self) -> int:
        return len(self.__clientes)

    def listarContas(self):
        for item in self.__contas:
            print(f'Conta: {item.numero} - Agência: {item.agencia} - {type(item)}')
        input("Pressione ENTER para continuar")

    def listarClientes(self):
        for item in self.__clientes:
            print(f'Nome: {item.nome} - CPF: {item.cpf} - Idade: {item.idade}')
        input("Pressione ENTER para continuar")

    def listarClientesEContas(self):
        for cpf, contas in self.__clienteVconta.items():
            print(f'Nome do Cliente: {self.retornaClientePeloCPF(cpf).nome}'.upper())
            print('Contas deste cliente:')
            for conta in contas:
                print(f'Número: {conta} - Tipo da Conta: {type(self.retornaContaPeloNumero(conta))}')
        input("Pressione ENTER para continuar")