class MultiplosInputs:
    def __init__(self, mensagens: list, validacoes : list):
        self.__mensagens = mensagens
        self.__validacoes = validacoes
        self.__respostas = []

    def valida(self, resposta_digiada: str, tipoExigido: str, comprimentoExigido: int) -> bool:

        if len(resposta_digiada) < comprimentoExigido:
            print(f'Você deve digitar pelo menos {comprimentoExigido} caracteres')
            return False
        try:
            # print(f'{tipoExigido}(resposta_digiada)')
            exec(f'{tipoExigido}(resposta_digiada)')
        except:
            print(f'Ocorreu um erro de conversão. Você deve entrar algo do tipo {tipoExigido}')
            return False

        return True

    def meuInput(self,vezes: int) -> list:
        if vezes == -1:
            return
        resposta = input(self.__mensagens[vezes])
        if resposta.upper() == "SAIR":
            return
        if not self.valida(resposta, self.__validacoes[vezes][0], self.__validacoes[vezes][1]):
            self.meuInput(vezes)
        else:
            self.__respostas.append(resposta)
            self.meuInput(vezes - 1)

        return self.__respostas