class Cliente:
    def __init__(self, id, nome, cpf):
        self._id = id
        self._nome = nome
        self._cpf = cpf
    
    def imprimirCliente(self):
        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        CPF - {self._cpf}
        ''')

    def consultarClientePorID(self):
        sql = f'''
        SELECT * FROM "Cliente"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID_Cliente" = '{self._id}'
        '''
        return sql

    def inserirCliente(self):
        sql = f'''
        INSERT INTO "Cliente"
        VALUES(default, '{self._nome}', '{self._cpf}')
        '''
        return sql
    
    def menuClientes(conexao):
        print("Lista de clientes: ")
        resultado = conexao.consultarBanco('''
        Select * FROM Cliente
        ORDER BY id ASC
        ''')
        print("ID | Nome")
        for cliente in resultado:
            print(f"{cliente[0]} | {cliente[1]}")

        print(f'''
        Escolha uma das opções:
        1. Ver cliente específico
        2. Inserir novo cliente
        0. Voltar para o menu principal
        ''')
        opcoes = int(input("Digite o número da opção desejada:"))
        match opcoes:
            case 1:
                while True:
                    clienteID = input("Digite o ID do cliente")
                    clienteEscolhido = Cliente(clienteID, None, None)
                    resultado = conexao.consultarBanco(clienteEscolhido.consultarClientePorID())
                    if resultado != []:
                        clienteEscolhido._nome = resultado[0][1]
                        clienteEscolhido._cpf = resultado[0][2]
                        clienteEscolhido.imprimirCliente()

                        while True:
                            print(f'''
                            Escolha uma das opções:
                            1. Ver alugueis
                            0. Voltar para o menu principal
                            ''')
                            opcoes = input("Digite o numero da opção:")
                            match opcoes:
                                case "1":
                                    resultado = conexao.consultarBanco(clienteEscolhido.consultarAlugueis())
                                    if resultado != []:
                                        print("ID | Data")
                                        for aluguel in resultado:
                                            print(f"{aluguel[0]} | {aluguel[3]}")
                                    else:
                                        print("Esse usuário não possui alugueis")
                                    input("Tecle ENTER para continuar")
                                case "0":
                                    print("Saindo do menu cliente.")
                                    break
                                case other:
                                    print("Você escolheu uma opção inválida")

                        break
                    else:
                        print("Você escolheu um ID inválido")