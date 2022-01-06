class DesenhaMenu:
    @staticmethod
    def imprime():
        cabecalho = """"
        Hello, o nosso Banco de Todo Dia!
        ┏┓┏┳━━┳┓┏┓┏━━┓
        ┃┗┛┃━━┫┃┃┃┃ ╭╮ ┃
        ┃┏┓┃━━┫┃┫┗┫ ╰╯ ┃
        ┗┛┗┻━━┻━┻━┻━━┛    
        Escolha sua opção:
            [ 1  ] Cadastrar novo cliente
            [ 2  ] Cadastrar nova conta corrente
            [ 3  ] Cadastrar nova conta poupança
            [ 4  ] Vincular clienta a uma conta
            [ 5  ] Listar contas cadastradas
            [ 6  ] Listar clientes cadastrados
            [ 7  ] Listar clientes e suas contas
            [ 8  ] Depositar
            [ 9  ] Sacar
            [ 10 ] Sair
            
        """
        print(cabecalho)