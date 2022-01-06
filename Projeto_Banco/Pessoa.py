"""
Classe abstrata que serve de base para outras classes, tal como a classe Cliente

Esta classe não deve gerar objetos, serve apenas ser herdada, ou seja, ser uma Super Classe
"""

from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, cpf, idade):
        # Aqui estamos usando o Setter abaixo construído, isso evita que o construtor baipasse o Setter
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    @property
    def nome(self):
        #print(f'Passei pelo Getter de {self.__class__.__name__}')
        return self.__nome

    @property
    def cpf(self):
        #print(f'Passei pelo Getter de {self.__class__.__name__}')
        return self.__cpf

    @property
    def idade(self):
        #print(f'Passei pelo Getter de {self.__class__.__name__}')
        return self.__idade

    @nome.setter
    def nome(self, nome_informado):
        #print(f'Passei pelo Setter de {self.__class__.__name__}')
        if len(nome_informado) < 6:
            raise ValueError("O nome deve ter pelo menos 5 caracteres")
        self.__nome = nome_informado

    @cpf.setter
    def cpf(self, cpf_informado):
        #print(f'Passei pelo Setter de {self.__class__.__name__}')
        self.__cpf = cpf_informado

    @idade.setter
    def idade(self, idade_informado):
        #print(f'Passei pelo Setter de {self.__class__.__name__}')
        if not isinstance(idade_informado, (int)):
            raise ValueError("A idade deve ser um valor nunérico inteiro")
        self.__idade = idade_informado


