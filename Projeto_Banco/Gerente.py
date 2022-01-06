from Projeto_Banco.Pessoa import Pessoa


class Gerente(Pessoa):
    def __init__(self, nome, cpf, idade):
        # Aqui estamos usando o Setter herdado da classe Pessoa
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

