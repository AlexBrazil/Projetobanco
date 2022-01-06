from Projeto_Banco.Pessoa import Pessoa
from Projeto_Banco.Gerente import Gerente


class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, gerente):
        # Precisamos iniciar a classe Super
        Pessoa.__init__(self,nome, cpf, idade)

        # Aqui estamos usando o Setter abaixo construído, isso evita que o construtor baipasse o Setter
        # Se usássemos self.__nome, etc, ao instanciar um objeto o construtor seria usado e o Setter nem chegaria a ser acessado
        self.gerente = gerente

    @property
    def gerente(self):
        return self.__gerente

    @gerente.setter
    def gerente(self, gerente_informado):
        #print(f'Passei pelo Setter de {self.__class__.__name__}')
        if not isinstance(gerente_informado, (Gerente)):
            raise ValueError("O gerente informado não é do tipo Gerente")
        self.__gerente = gerente_informado



