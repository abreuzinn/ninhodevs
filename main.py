import psycopg2
from classConexao import Conexao

def createTableCliente(conex):
    conex.manipularBanco('''
    CREATE TABLE "Cliente"(
    "idCLIENTE" int GENERATED ALWAYS AS IDENTITY,
    "nomeCLIENTE" varchar(255),
    "cpfCLIENTE" char(11),
    "telefoneCLIENTE" char(11),
    "enderecoCLIENTE" varchar(255),
    PRIMARY KEY ("idCLIENTE")
    );
    ''')

def createTableVeiculo(conex):
    conex.manipularBanco('''
    CREATE TABLE "Veiculo"(
    "refVEICULO" int GENERATED ALWAYS AS IDENTITY,
    "modeloVEICULO" varchar(255),
    "marcaVEICULO" varchar(255),
    "valorDiariaVEICULO" money,
    "anoFabVEICULO" char(4),
    "anoModVEICULO" char(4),
    "litragemVEICULO" varchar(3),
    "carroceriaVEICULO" varchar(255),
    PRIMARY KEY ("refVEICULO")
    );
    ''')

def createTableAluguel(conex):
    conex.manipularBanco('''
    CREATE TABLE "Aluguel"(
    "idALUGUEL" int GENERATED ALWAYS AS IDENTITY,
    "dataALUGUEL" date,
    "idCLIENTE" int NOT NULL,
    "refVEICULO" int NOT NULL,
    PRIMARY KEY ("idALUGUEL"),
    CONSTRAINT fk_cliente
        FOREIGN KEY ("idCLIENTE")
        REFERENCES "Cliente"("idCLIENTE")
        ON DELETE SET NULL
        ON UPDATE NO ACTION
    ,
    CONSTRAINT fk_veiculo
        FOREIGN KEY("refVEICULO")
        REFERENCES "Veiculo"("refVEICULO")
        ON DELETE SET NULL
        ON UPDATE NO ACTION
    );
    ''')

def showMenuVeiculos(conex):
    while True:
        menu = input("\nO que fazer?\n\n1- Ver todo o catálogo\n2- Ver veículo específico por ID\n3- Ver veículos de certa marca\n4- Ver veículos pela litragem\n5- Ver veículos pelo ano de modelo ou fabricação\n6- Ver veículos pelo tipo de carroceria\n7- Manipular catálogo\n0- Voltar\n\n")
        match menu:
            case "1":
                showCatalogo(conex)
            case "2":
                showVeiculoEspecifico(conex)
            case "3":
                showVeiculosMarca(conex)
            case "4":
                showVeiculosLitragem(conex)
            case "5":
                showVeiculosAno(conex)
            case "6":
                showVeiculosCarroceria(conex)
            case "7":
                manipularVeiculos(conex)
            case "0":
                break
            case other:
                print("Ação inválida. Tente novamente.")

def showMenuClientes(conex):
    while True:
        menu = input("\nO que fazer?\n\n1- Ver clientes\n2- Ver cliente específico\n3- Manipular clientes\n0- Voltar\n\n")
        match menu:
            case "1":
                showClientes(conex)
            case "0":
                break
            case other:
                print("Ação inválida.")
def showCatalogo(conex):
    resultado = conex.consultarBanco('''
    SELECT * FROM "Veiculo"
    ORDER BY "refVEICULO" ASC
    ''')
    while True:
        modoExibicao = input("\n1- Visualização básica\n2- Visualização detalhada\n\n")
        match modoExibicao:
            case "1":
                for veiculo in resultado:
                    print(f"\n{veiculo[0]}- R$ {veiculo[3]} | {veiculo[2]} {veiculo[1]} {veiculo[7]} {veiculo[6]} {veiculo[5]}")
                break                
            case "2":
                print(f"\nTOTAL DE VEÍCULOS NO CATÁLOGO: {len(resultado)}")
                for veiculo in resultado:
                    print(f"\nREF. VEÍCULO - {veiculo[0]}\nMODELO - {veiculo[1]}\nMARCA - {veiculo[2]}\nVALOR do ALUGUEL (DIÁRIO) - {veiculo[3]}\nANO - {veiculo[4]}/{veiculo[5]}\nLITRAGEM - {veiculo[6]}\nCARROCERIA - {veiculo[7]}\n")
                break
            case other:
                print("Inválido.")

def showVeiculoEspecifico(conex):
    ref = input("Insira o código de referência (REF) de algum veículo do catálogo: ")
    resultado = conex.consultarBanco(f'''
    SELECT * FROM "Veiculo"
    WHERE "refVEICULO" = '{ref}'
    ''')
    for veiculo in resultado:
        print(f"\nREF. VEÍCULO - {veiculo[0]}\nMODELO - {veiculo[1]}\nMARCA - {veiculo[2]}\nVALOR do ALUGUEL (DIÁRIO) - {veiculo[3]}\nANO - {veiculo[4]}/{veiculo[5]}\nLITRAGEM - {veiculo[6]}\nCARROCERIA - {veiculo[7]}\n")

def showVeiculosMarca(conex):
    resultado = conex.consultarBanco('''
    SELECT "marcaVEICULO" FROM "Veiculo"
    ORDER BY "marcaVEICULO" ASC
    ''')
    resultado = list(dict.fromkeys(resultado))
    print("")
    for marcas in resultado:
        print(f"- {marcas[0]}")
    while True:
        marcaVEICULO = input("Insira o nome da marca desejada (utilize 0 para voltar): ")
        match marcaVEICULO:
            case "0":
                break
            case other:
                resultado = conex.consultarBanco(f'''
                SELECT * FROM "Veiculo"
                WHERE "marcaVEICULO" = '{marcaVEICULO}'
                ''')
                for veiculo in resultado:
                    print(f"\nREF. VEÍCULO - {veiculo[0]}\nMODELO - {veiculo[1]}\nMARCA - {veiculo[2]}\nVALOR do ALUGUEL (DIÁRIO) - {veiculo[3]}\nANO - {veiculo[4]}/{veiculo[5]}\nLITRAGEM - {veiculo[6]}\nCARROCERIA - {veiculo[7]}\n")
                break

def showVeiculosLitragem(conex):
    resultado = conex.consultarBanco('''
    SELECT "litragemVEICULO" FROM "Veiculo"
    ORDER BY "litragemVEICULO" ASC
    ''')
    resultado = list(dict.fromkeys(resultado))
    print("")
    for litragem in resultado:
        print(f"- {litragem[0]}")
    while True:
        litragemVEICULO = input("Insira a litragem desejada (utilize 0 para voltar): ")
        match litragemVEICULO:
            case "0":
                break
            case other:
                resultado = conex.consultarBanco(f'''
                SELECT * FROM "Veiculo"
                WHERE "litragemVEICULO" = '{litragemVEICULO}'
                ''')
                for veiculo in resultado:
                    print(f"\nREF. VEÍCULO - {veiculo[0]}\nMODELO - {veiculo[1]}\nMARCA - {veiculo[2]}\nVALOR do ALUGUEL (DIÁRIO) - {veiculo[3]}\nANO - {veiculo[4]}/{veiculo[5]}\nLITRAGEM - {veiculo[6]}\nCARROCERIA - {veiculo[7]}\n")
                break

def showVeiculosAno(conex):
    resultado = conex.consultarBanco('''
    SELECT "anoFabVEICULO", "anoModVEICULO" FROM "Veiculo"
    ORDER BY "anoFabVEICULO" ASC
    ''')
    resultado = list(dict.fromkeys(resultado))
    print("")
    for ano in resultado:
        print(f"- {ano[0]}/{ano[1]}")
        
    while True:
        anoVEICULO = input("Insira o ano desejado (insira 0 para voltar): ")
        match anoVEICULO:
            case "0":
                break
            case other:
                resultado = conex.consultarBanco(f'''
                SELECT * FROM "Veiculo"
                WHERE "anoFabVEICULO" = '{anoVEICULO}' OR "anoModVEICULO" = '{anoVEICULO}'
                ''')
                for veiculo in resultado:
                    print(f"\nREF. VEÍCULO - {veiculo[0]}\nMODELO - {veiculo[1]}\nMARCA - {veiculo[2]}\nVALOR do ALUGUEL (DIÁRIO) - {veiculo[3]}\nANO - {veiculo[4]}/{veiculo[5]}\nLITRAGEM - {veiculo[6]}\nCARROCERIA - {veiculo[7]}\n")
                break

def showVeiculosCarroceria(conex):
    resultado = conex.consultarBanco('''
    SELECT "carroceriaVEICULO" FROM "Veiculo"
    ORDER BY "carroceriaVEICULO" ASC
    ''')
    resultado = list(dict.fromkeys(resultado))
    print("")
    for carroceria in resultado:
        print(f"- {carroceria[0]}")
    while True:
        carroceriaVEICULO = input("Insira o tipo de carroceria desejada (insira 0 para voltar): ")
        match carroceriaVEICULO:
            case "0":
                break
            case other:
                resultado = conex.consultarBanco(f'''
                SELECT * FROM "Veiculo"
                WHERE "carroceriaVEICULO" = '{carroceriaVEICULO}'
                ORDER BY "carroceriaVEICULO"
                ''')
                for veiculo in resultado:
                    print(f"\nREF. VEÍCULO - {veiculo[0]}\nMODELO - {veiculo[1]}\nMARCA - {veiculo[2]}\nVALOR do ALUGUEL (DIÁRIO) - {veiculo[3]}\nANO - {veiculo[4]}/{veiculo[5]}\nLITRAGEM - {veiculo[6]}\nCARROCERIA - {veiculo[7]}\n")
                break

def addVeiculo(conex):
    modeloVeiculo = input("Insira o modelo do veículo: ")
    marcaVeiculo = input("Insira a marca do veículo: ")
    while True:
        anoFabVeiculo = input("Insira o ano de fabricação do veículo: ")
        if anoFabVeiculo.isnumeric():
            break
        else:
            print("Insira o ano de forma numérica (exemplo: 2018)")
    while True:
        anoModVeiculo = input("Insira o ano do modelo do veículo: ")
        if anoModVeiculo.isnumeric():
            break
        else:
            print("Insira o ano de forma numérica (exemplo: 2018)")
    litragemVeiculo = (input("Insira a litragem do veículo (exemplo: 2.0): "))
    carroceriaVeiculo = input("Insira o tipo de carroceria do veículo (exemplo: SUV, Sedã...): ")
    while True:
        try:
            valorDiariaVeiculo = int(input("Insira o valor do aluguel do veículo (diário): "))
            break
        except:
            TypeError(print("Insira o valor de forma numérica. (exemplo: 150)"))

    conex.manipularBanco(f'''
    INSERT INTO "Veiculo"
    VALUES(default, '{modeloVeiculo}', '{marcaVeiculo}', '{valorDiariaVeiculo}', '{anoFabVeiculo}', '{anoModVeiculo}', '{litragemVeiculo}', '{carroceriaVeiculo}')
    ''')
    print("Veículo adicionado com sucesso.")

def delVeiculo(conex):
    ref = input("Insira o código de referência (REF) do veículo que deseja excluir do catálogo: ")
    conex.manipularBanco(f'''
    DELETE FROM "Veiculo"
    WHERE "refVEICULO" = {ref}
    ''')
    print("\nCaso o código de referência informado pertença a algum veículo, o mesmo acaba de ser deletado com sucesso.")

def attVeiculo(conex):
    ref = input("Insira o código de referência (REF) do veículo que deseja excluir do catálogo: ")
    resultado = conex.consultarBanco(f'''
    SELECT * FROM "Veiculo"
    WHERE "refVEICULO" = {ref}
    ''')

    for veiculo in resultado:
        print(f"\nVEÍCULO ESCOLHIDO\n\nREF. VEÍCULO - {veiculo[0]}\nMODELO - {veiculo[1]}\nMARCA - {veiculo[2]}\nVALOR do ALUGUEL (DIÁRIO) - {veiculo[3]}\nANO - {veiculo[4]}/{veiculo[5]}\nLITRAGEM - {veiculo[6]}\nCARROCERIA - {veiculo[7]}\n")

    novoModeloVeiculo = input("Insira o novo modelo do veículo: ")
    novaMarcaVeiculo = input("Insira a nova marca do veículo: ")
    while True:
        novoAnoFabVeiculo = input("Insira o novo ano de fabricação do veículo: ")
        if novoAnoFabVeiculo.isnumeric():
            break
        else:
            print("Insira o novo ano de forma numérica (exemplo: 2018)")
    while True:
        novoAnoModVeiculo = input("Insira o novo ano do modelo do veículo: ")
        if novoAnoModVeiculo.isnumeric():
            break
        else:
            print("Insira o ano de forma numérica (exemplo: 2018)")
    novaLitragemVeiculo = (input("Insira a nova litragem do veículo (exemplo: 2.0): "))
    novaCarroceriaVeiculo = input("Insira o novo tipo de carroceria do veículo (exemplo: SUV, Sedã...): ")
    while True:
        try:
            novoValorDiariaVeiculo = int(input("Insira o novo valor do aluguel do veículo (diário): "))
            break
        except:
            TypeError(print("Insira o valor de forma numérica. (exemplo: 150)"))

    conex.manipularBanco(f'''
    UPDATE "Veiculo"
    SET
    "modeloVEICULO" = '{novoModeloVeiculo}',
    "marcaVEICULO" = '{novaMarcaVeiculo}',
    "valorDiariaVEICULO" = '{novoValorDiariaVeiculo}',
    "anoFabVEICULO" = '{novoAnoFabVeiculo}',
    "anoModVEICULO" = '{novoAnoModVeiculo}',
    "litragemVEICULO" = '{novaLitragemVeiculo}',
    "carroceriaVEICULO" = '{novaCarroceriaVeiculo}'
    ''')
    print("\nCaso o código de referência informado pertença a algum veículo do catálogo, o mesmo acaba de ser atualizado com sucesso.")

def manipularVeiculos(conex):
    while True:
        menu = input("\nO que fazer?\n\n1- Adicionar veículo\n2- Remover veículo\n3- Atualizar veículo\n0- Voltar\n\n")
        match menu:
            case "1":
                addVeiculo(conex)
            case "2":
                delVeiculo(conex)
            case "3":
                attVeiculo(conex)
            case "0":
                break
            case other:
                print("Ação inválida.")

def showClientes(conex):
    resultado = conex.consultarBanco('''
    SELECT * FROM "Cliente"
    ORDER BY "idCLIENTE" ASC
    ''')

    for cliente in resultado:
        print(f"\nID - {cliente[0]}\nNOME - {cliente[1]}\nCPF - {cliente[2]}\nTELEFONE - {cliente[3]}")

def showClienteEspecifico(conex):
    idCLIENTE = input("Insira o ID do cliente que deseja visualizar: ")
    resultado = conex.consultarBanco(f'''
    SELECT * FROM "Cliente"
    WHERE "idCLIENTE" = {idCLIENTE}
    ''')

    for cliente in resultado:
        print(f"\nID - {cliente[0]}\nNOME - {cliente[1]}\nCPF - {cliente[2]}\nTELEFONE - {cliente[3]}")

def addCliente(conex):
    

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

while True:
    try:
        user = input("Insira o usuário: ")
        password = input("Insira a senha: ")
        # login e senha "postgres"

        con = Conexao("Locadora", user, password, "localhost", "5432" )
        print("Connected")
        break

    except (Exception, psycopg2.Error) as error:
        print(f"Something went wrong - {error}")

# createTableCliente(con)
# createTableVeiculo(con)
# createTableAluguel(con)

while True:
    menu = input("\nO que fazer?\n\n1- Menu veículos\n2- Menu clientes\n3- Menu aluguéis\n0- Encerrar\n\n")
    match menu:
        case "1":
            showMenuVeiculos(con)
        case "2":
            showMenuClientes(con)
        case "3":
            showMenuAlugueis(con)
        case "0":
            print("Encerrando")
            break






