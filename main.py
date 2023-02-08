import psycopg2
from classConexao import Conexao

def createTableCliente(conexao):
    conexao.manipularBanco('''
    CREATE TABLE "Cliente"(
    "idCLIENTE" int GENERATED ALWAYS AS IDENTITY,
    "nomeCLIENTE" varchar(255),
    "cpfCLIENTE" char(11),
    "telefoneCLIENTE" char(11),
    "enderecoCLIENTE" varchar(255),
    PRIMARY KEY ("idCLIENTE")
    );
    ''')

def createTableVeiculo(conexao):
    conexao.manipularBanco('''
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

def createTableAluguel(conexao):
    conexao.manipularBanco('''
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
        menu = input("\nO que fazer?\n\n1- Ver todo o catálogo\n2- Ver carro específico por ID\n3- Ver carros de certa marca\n4- Ver carros pela litragem\n5- Ver carros pelo ano de modelo ou fabricação\n6- Manipular catálogo\n0- Voltar\n\n")
        match menu:
            case "1":
                resultado = con.consultarBanco('''
                SELECT * FROM "Veiculo"
                ORDER BY "refVEICULO" ASC
                ''')
                for veiculo in resultado:
                    print(f"\nREF. VEÍCULO - {veiculo[0]}\nMODELO - {veiculo[1]}\nMARCA - {veiculo[2]}\nVALOR do ALUGUEL (DIÁRIO) - {veiculo[3]}\nANO - {veiculo[4]}/{veiculo[5]}\nLITRAGEM - {veiculo[6]}\nCARROCERIA - {veiculo[7]}")
            case "6":
                manipularVeiculos(con)


            case "0":
                break
            case other:
                print("Ação inválida. Tente novamente.")

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

def delVeiculo(conex):
    ref = input("Insira o código de referência (REF) do veículo que deseja excluir do catálogo: ")
    conex.manipularBanco('''
    DELETE 
    ''')

def manipularVeiculos(conex):
    while True:
        menu = input("\nO que fazer?\n\n1- Adicionar veículo\n2- Remover veículo\n3- Atualizar veículo\n\n")
        match menu:
            case "1":
                addVeiculo(conex)
            case "2":
                delVeiculo(conex)
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
            showMenuClientes()
        case "3":
            showMenuAlugueis()
        case "0":
            print("Encerrando")
            break







