from Projeto_Banco.Cliente import Cliente
from Projeto_Banco.Gerente import Gerente
from Projeto_Banco.Conta_Corrente import ContaCorrente
from Projeto_Banco.Conta_Poupanca import ContaPoupanca
from Projeto_Banco.Banco import Banco
from Projeto_Banco.Desenha_Menu import DesenhaMenu
from Projeto_Banco.MultiplosInputs import MultiplosInputs
import os
from time import sleep


#Limpa a tela do console
#print("\n" * 130)

def cadastra_cliente():
    respostas = []
    # Defina as perguntas a serem realizadas no input
    mensagens = ["Digite o nome do cliente: ", "Digite a idade: ", "Digite o CPF: "]
    # Defina o tipo e o tamanho de cada entrada
    validacoes = [['str', 5], ['int', 2], ['int', 11]]

    # Inverte as listas para aparecerem na otdem certa
    mensagens.reverse()
    validacoes.reverse()
    inputs = MultiplosInputs(mensagens, validacoes)
    retorno = inputs.meuInput(2)
    gerente = Gerente("Carlos", 69122059091, 50)
    novo_cliente = Cliente(retorno[0], retorno[2], int(retorno[1]), gerente)
    banco.add_cliente(novo_cliente)

def cadastra_conta_corrente():
    respostas = []
    # Defina as perguntas a serem realizadas no input
    mensagens = ["Digite o número da conta: ", "Digite a agência: "]
    # Defina o tipo e o tamanho de cada entrada
    validacoes = [['int', 5], ['int', 3]]

    # Inverte as listas para aparecerem na otdem certa
    mensagens.reverse()
    validacoes.reverse()
    inputs = MultiplosInputs(mensagens, validacoes)
    retorno = inputs.meuInput(1)
    nova_conta = ContaCorrente(int(retorno[0]), int(retorno[1]), 100)
    banco.add_conta(nova_conta)

def cadastra_conta_poupanca():
    respostas = []
    # Defina as perguntas a serem realizadas no input
    mensagens = ["Digite o número da conta: ", "Digite a agência: "]
    # Defina o tipo e o tamanho de cada entrada
    validacoes = [['int', 5], ['int', 3]]

    # Inverte as listas para aparecerem na otdem certa
    mensagens.reverse()
    validacoes.reverse()
    inputs = MultiplosInputs(mensagens, validacoes)
    retorno = inputs.meuInput(1)
    nova_conta = ContaPoupanca(int(retorno[0]), int(retorno[1]), 100)
    banco.add_conta(nova_conta)

def vincula_cliente_conta():
    respostas = []
    # Defina as perguntas a serem realizadas no input
    mensagens = ["Digite o CPF do cliente: ", "Digite o número da conta: "]
    # Defina o tipo e o tamanho de cada entrada
    validacoes = [['int', 11], ['int', 5]]

    # Inverte as listas para aparecerem na otdem certa
    mensagens.reverse()
    validacoes.reverse()
    inputs = MultiplosInputs(mensagens, validacoes)
    retorno = inputs.meuInput(1)
    cliente_retornado = banco.retornaClientePeloCPF(retorno[0])
    conta_retornada = banco.retornaContaPeloNumero(int(retorno[1]))
    if cliente_retornado == None or conta_retornada == None:
        print('CPF de cliente ou conta não cadastrada')
    else:
        # Vincula cliente a conta
        banco.addClienteXConta(cliente_retornado, conta_retornada)
    input("Pressione ENTER para continuar")

def depositar():
    respostas = []
    # Defina as perguntas a serem realizadas no input
    mensagens = ["Digite o número da conta para depósito: ", "Digite o valor: "]
    # Defina o tipo e o tamanho de cada entrada
    validacoes = [['int', 5], ['float', 3]]

    # Inverte as listas para aparecerem na otdem certa
    mensagens.reverse()
    validacoes.reverse()
    inputs = MultiplosInputs(mensagens, validacoes)
    retorno = inputs.meuInput(1)
    # Para que possamos depositar na conta, ela tem que estar vinculada a algum cliente
    if banco.contaVinculadaCliente(int(retorno[0])):
        conta = banco.retornaContaPeloNumero(int(retorno[0]))
        conta.depositar(float(retorno[1]))
        input("Pressione ENTER para continuar")
    else:
        print('Esta conta não possui um cliente vinculado a ela')
        input("Pressione ENTER para continuar")

def sacar_valor():
    respostas = []
    # Defina as perguntas a serem realizadas no input
    mensagens = ["Digite o número da conta para sacar: ", "Digite o valor: "]
    # Defina o tipo e o tamanho de cada entrada
    validacoes = [['int', 5], ['float', 3]]

    # Inverte as listas para aparecerem na otdem certa
    mensagens.reverse()
    validacoes.reverse()
    inputs = MultiplosInputs(mensagens, validacoes)
    retorno = inputs.meuInput(1)
    # Para que possamos depositar na conta, ela tem que estar vinculada a algum cliente
    if banco.contaVinculadaCliente(int(retorno[0])):
        conta = banco.retornaContaPeloNumero(int(retorno[0]))
        conta.sacar(float(retorno[1]))
    else:
        print('Esta conta não possui um cliente vinculado a ela')
        input("Pressione ENTER para continuar")

banco = Banco()
menu_opcoes = ['1', '2', '3', '4', '5','6', '7', '8', '9','10']
entrada = None

while entrada != '10':
    DesenhaMenu.imprime()
    entrada = input('Digite sua opção:')
    if entrada not in menu_opcoes:
        print('Opção invalida!')
        sleep(2)
    if entrada == '1':
        cadastra_cliente()
    elif entrada == '2':
        cadastra_conta_corrente()
    elif entrada == '3':
        cadastra_conta_poupanca()
    elif entrada == '4':
        vincula_cliente_conta()
    elif entrada == '5':
        banco.listarContas()
    elif entrada == '6':
        banco.listarClientes()
    elif entrada == '7':
        banco.listarClientesEContas()
    elif entrada == '8':
        depositar()
    elif entrada == '9':
        sacar_valor()
print('\nRESUMO DOS RESULTADOS')
print(f'Total de clientes: {banco.conta_clientes()}')
print(f'Total de contas: {banco.conta_contas()}')
print(f'Total de contas vinculadas a clientes: {banco.contaClientesComConta()}')


# gerente = Gerente("Carlos", 69122059091, 50)
# cliente1 = Cliente("Alexandre", 99999999999, 30, gerente)
# cliente2 = Cliente("Simone", 66699966699, 30, gerente)
#
#
# conta_corrente = ContaCorrente(123450, 122, 100,0,500)
# conta_corrente2 = ContaCorrente(654320, 122, 100,0,500)
# conta_corrente3 = ContaCorrente(654321, 122, 100,0,500)
#
#
# banco.add_conta(conta_corrente)
# banco.add_conta(conta_corrente2)
# banco.add_conta(conta_corrente3)
# banco.add_cliente(cliente1)
# banco.add_cliente(cliente1)
#
# print(f'"Clientes com conta cadastrada: {banco.contaClientesComConta()}')
#
# banco.addClienteXConta(cliente1, conta_corrente)
# banco.addClienteXConta(cliente1, conta_corrente2)
# banco.addClienteXConta(cliente1, conta_corrente3)
#
# print(f'Total de contas: {banco.conta_contas()}')
# print(f'Total de clientes: {banco.conta_clientes()}')
# print(f'"Clientes com conta cadastrada: {banco.contaClientesComConta()}')






