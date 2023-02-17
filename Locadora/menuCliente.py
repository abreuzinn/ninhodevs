def showMenuClientes(conex):
    while True:
        menu = input("\nO que fazer?\n\n1- Ver clientes\n2- Ver cliente específico\n3- Manipular clientes\n0- Voltar\n\n")
        match menu:
            case "1":
                showClientes(conex)
            case "2":
                showClienteEspecifico(conex)
            case "3":
                manipularClientes(conex)
            case "0":
                break
            case other:
                print("Ação inválida.")

def showClientes(conex):
    resultado = conex.consultarBanco('''
    SELECT * FROM "Cliente"
    ORDER BY "idCLIENTE" ASC
    ''')

    while True:
        modoExibicao = input(f"\n1- Visualização básica\n2- Visualização detalhada\n\n")
        match modoExibicao:
            case "1":
                for cliente in resultado:
                    print(f"\nNOME - {cliente[1]}\nCPF - {cliente[2]}")
                break
            case "2":
                for cliente in resultado:
                    print(f"\nID - {cliente[0]}\nNOME - {cliente[1]}\nCPF - {cliente[2]}\nTELEFONE - {cliente[3]}\nENDEREÇO - {cliente[4]}")
                break
            case other:
                print("Ação inválida.")

def showClienteEspecifico(conex):
    idCLIENTE = input("Insira o ID do cliente que deseja visualizar: ")
    resultado = conex.consultarBanco(f'''
    SELECT * FROM "Cliente"
    WHERE "idCLIENTE" = {idCLIENTE}
    ''')

    for cliente in resultado:
        print(f"\nID - {cliente[0]}\nNOME - {cliente[1]}\nCPF - {cliente[2]}\nTELEFONE - {cliente[3]}\nENDEREÇO - {cliente[4]}")

def addCliente(conex):
    nomeCLIENTE = input("Insira o nome do cliente: ")
    cpfCLIENTE = inputCPF()
    telefoneCLIENTE = inputTelefone()
    enderecoCLIENTE = input("Insira o endereço do cliente: ")

    conex.manipularBanco(f'''
    INSERT INTO "Cliente"
    VALUES(default, '{nomeCLIENTE}', '{cpfCLIENTE}', '{telefoneCLIENTE}', '{enderecoCLIENTE}')
    ''')
    print("Cliente adicionado com sucesso.")

def delCliente(conex):
    idCLIENTE = input("Insira o ID do cliente que deseja deletar: ")

    conex.manipularBanco(f'''
    DELETE FROM "Cliente"
    WHERE "idCLIENTE" = '{idCLIENTE}'
    ''')
    print("Caso o ID informado pertença a algum cliente, o mesmo acaba de ser deletado ")

def attCliente(conex):
    idCLIENTE = input("Insira o ID do cliente que deseja alterar: ")
    resultado = conex.consultarBanco(f'''
    SELECT * FROM "Cliente"
    WHERE "idCLIENTE" = '{idCLIENTE}'
    ''')

    for cliente in resultado:
        print(f"\nID - {cliente[0]}\nNOME - {cliente[1]}\nCPF - {cliente[2]}\nTELEFONE - {cliente[3]}\nENDEREÇO - {cliente[4]}")

    novoNomeCLIENTE = input("Insira o novo nome do cliente: ")
    novoCpfCLIENTE = inputCPF()
    novoTelefoneCLIENTE = inputTelefone()
    novoEnderecoCLIENTE = input("Insira o novo endereço do cliente: ")

    conex.manipularBanco(f'''
    UPDATE "Cliente"
    SET
    "nomeCLIENTE" = '{novoNomeCLIENTE}',
    "cpfCLIENTE" = '{novoCpfCLIENTE}',
    "telefoneCLIENTE" = '{novoTelefoneCLIENTE}',
    "enderecoCLIENTE" = '{novoEnderecoCLIENTE}'
    WHERE "idCLIENTE" = '{idCLIENTE}'
    ''')
    print("Caso o ID informado pertença a algum cliente, o mesmo acaba de ser atualizado.")

def inputCPF():
    while True:
        cpfInput = input("Insira o CPF do cliente:").replace(".", "").replace("-", "")
        if cpfInput.isnumeric():
            if len(cpfInput) == 11:
                resultadoCpf = f"{cpfInput[0]}{cpfInput[1]}{cpfInput[2]}.{cpfInput[3]}{cpfInput[4]}{cpfInput[5]}.{cpfInput[6]}{cpfInput[7]}{cpfInput[8]}-{cpfInput[9]}{cpfInput[10]}"
                break
            else:
                print("O tamanho do CPF deve ser de 11 carácteres.")
        else:
            print("O CPF deve ser composto apenas por números.")
    return resultadoCpf

def inputTelefone():
    while True:
        telefoneInput = input("Insira o telefone de contato do cliente:").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        if telefoneInput.isnumeric():
            if len(telefoneInput) == 10:
                resultadoTelefone = f"({telefoneInput[0]}{telefoneInput[1]}) {telefoneInput[2]}{telefoneInput[3]}{telefoneInput[4]}{telefoneInput[5]}-{telefoneInput[6]}{telefoneInput[7]}{telefoneInput[8]}{telefoneInput[9]}"
                break
            if len(telefoneInput) == 11:
                resultadoTelefone = f"({telefoneInput[0]}{telefoneInput[1]}) {telefoneInput[2]}{telefoneInput[3]}{telefoneInput[4]}{telefoneInput[5]}{telefoneInput[6]}-{telefoneInput[7]}{telefoneInput[8]}{telefoneInput[9]}{telefoneInput[10]}"
                break
            else:
                print("O tamanho do número de telefone deve ser de 10 ou 11 carácteres.")
        else:
            print("O número de telefone deve ser composto apenas por números ou deve estar no formato internacional ((xx) xxxxx-xxxx)")
    return resultadoTelefone

def manipularClientes(conex):
    while True:
        menu = input("\nO que fazer?\n\n1- Adicionar cliente\n2- Remover cliente\n3- Atualizar cliente\n0- Voltar\n\n")
        match menu:
            case "1":
                addCliente(conex)
            case "2":
                delCliente(conex)
            case "3":
                attCliente(conex)
            case "0":
                break
            case other:
                print("Ação inválida.")