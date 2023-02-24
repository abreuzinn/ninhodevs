import psycopg2
from datetime import date
from classConexao import sleep

def showMenuAlugueis(conex):
    while True:
        sleep(1)
        menu = input("\nO que fazer?\n\n1- Ver alugueis\n2- Ver aluguel específico\n3- Manipular alugueis\n0- Voltar\n\n")
        match menu:
            case "1":
                showAlugueis(conex)
            case "2":
                showAluguelEspecifico(conex)
            case "3":
                manipularAlugueis(conex)
            case "0":
                break
            case other:
                sleep(1)
                print("Ação inválida.")

def showAlugueis(conex):
    resultado = conex.consultarBanco('''
    SELECT "idALUGUEL", to_char("dataALUGUEL", 'DD/MM/YYYY'), "idCLIENTE", "refVEICULO"  FROM "Aluguel";
    ''')

    print("\nAguarde...")
    sleep(2)

    for aluguel in resultado:
        consultaCliente = conex.consultarBanco(f'''
        SELECT "nomeCLIENTE" from "Cliente"
        WHERE "idCLIENTE" = {aluguel[2]};
        ''')
        for c in consultaCliente:
            consultaVeiculo = conex.consultarBanco(f'''
            SELECT * from "Veiculo"
            WHERE "refVEICULO" = {aluguel[3]};
            ''')
            for v in consultaVeiculo:
                veiculo = f"{v[2]} {v[1]} {v[7]} {v[6]} {v[5]}"
                print(f"\nID ALUGUEL - {aluguel[0]}\nCLIENTE - {c[0]} | ID - {aluguel[2]}\nVEÍCULO - {veiculo} | REF - {aluguel[3]}\nDATA - {aluguel[1]}\nVALOR ALUGUEL - {v[3]}")

def showAluguelEspecifico(conex):
    sleep(1)
    idALUGUEL = input("\nInsira o ID do aluguel que deseja consultar: ")
    resultado = conex.consultarBanco(f'''
    SELECT * FROM "Aluguel"
    WHERE "idALUGUEL" = {idALUGUEL};
    ''')

    print("\nAguarde...")
    sleep(2)

    for aluguel in resultado:
        consultaCliente = conex.consultarBanco(f'''
        SELECT "nomeCLIENTE" from "Cliente"
        WHERE "idCLIENTE" = {aluguel[2]};
        ''')
        for c in consultaCliente:
            consultaVeiculo = conex.consultarBanco(f'''
            SELECT * from "Veiculo"
            WHERE "refVEICULO" = {aluguel[3]};
            ''')
            for v in consultaVeiculo:
                veiculo = f"{v[2]} {v[1]} {v[7]} {v[6]} {v[5]}"
                print(f"\nID ALUGUEL - {aluguel[0]}\nCLIENTE - {c[0]} | ID - {aluguel[2]}\nVEÍCULO - {veiculo} | REF - {aluguel[3]}\nDATA - {aluguel[1]}\nVALOR ALUGUEL - {v[3]}")

def addAluguel(conex):
    while True:
        sleep(1)
        idCLIENTE = input("\nInsira o ID do cliente que deseja cadastrar em um contrato de aluguel: ")
        refVEICULO = input("Insira o código de referência (REF) do veículo que deseja cadastrar no contrato de aluguel: ")
        dataALUGUEL = inputDataAluguel(conex)

        resultadoCLIENTE = conex.consultarBanco(f'''
        SELECT * FROM "Cliente"
        WHERE "idCLIENTE" = {idCLIENTE};
        ''')
        resultadoVEICULO = conex.consultarBanco(f'''
        SELECT * FROM "Veiculo"
        WHERE "refVEICULO" = {refVEICULO};
        ''')

        for cliente in resultadoCLIENTE:
            print(f"\nCLIENTE SELECIONADO - {cliente[1]}")

        for veiculo in resultadoVEICULO:
            print(f"VEÍCULO SELECIONADO - {veiculo[2]} {veiculo[1]} {veiculo[7]} {veiculo[6]} {veiculo[5]}")

        confirm = input("\nCONTRATO DE ALUGUEL\n\n1- CONFIRMAR\n2- CANCELAR\n\n")
        match confirm:
            case "1":
                try:
                    conex.manipularBanco(f'''
                    INSERT INTO "Aluguel"
                    VALUES(default, '{dataALUGUEL}', '{idCLIENTE}', '{refVEICULO}');
                    ''')
                    sleep(1)
                    print("\nContrato de locação confirmado.")
                    break
                except(Exception, psycopg2.Error):
                    sleep(1)
                    print("\nO ID ou o REF informado não existe na tabela de Clientes.")
                    conex.manipularBanco('''
                    ROLLBACK;
                    ''')
                    break
            case "2":
                break
            case other:
                sleep(1)
                print("\nInválido.")

def inputDataAluguel(conex):
     while True:
        sleep(1)
        dataAluguelInput = input("\nInsira a data do aluguel no formato DD/MM/AAAA (insira 0 para cadastrar a data de hoje): ").replace("/", "")
        match dataAluguelInput:
            case "1":
                if dataAluguelInput.isnumeric():
                    if len(dataAluguelInput) == 8:
                        dataAluguel = f"{dataAluguelInput[0]}{dataAluguelInput[1]}/{dataAluguelInput[2]}{dataAluguelInput[3]}/{dataAluguelInput[4]}{dataAluguelInput[5]}{dataAluguelInput[6]}{dataAluguelInput[7]}"
                        return dataAluguel
                        break
                    else:
                        sleep(1)
                        print("\nA data deve estar no formato DMY (ex.: 25/02/2023).")
                else:
                    sleep(1)
                    print("\nA data deve possuir apenas números ou estar no formato DMY.")
            case "0":
                data = date.today.strftime("%d/%m/%Y")
                return data
                break
            case other:
                sleep(1)
                print("\nInválido.")

def delAluguel(conex):
    sleep(1)
    idALUGUEL = input("\nInsira o ID do aluguel que deseja deletar: ")
    conex.manipularBanco(f'''
    DELETE FROM "Aluguel"
    WHERE "idALUGUEL" = {idALUGUEL};
    ''')
    sleep(1)
    print("\nCaso o ID informado pertença a algum aluguel, o mesmo acaba de ser deletado.")

def attAluguel(conex):
    sleep(1)
    idALUGUEL = input("\nInsira o ID do aluguel que deseja atualizar: ")
    resultado = conex.consultarBanco(f'''
    SELECT * FROM "Aluguel"
    WHERE "idALUGUEL" = {idALUGUEL};
    ''')
    for aluguel in resultado:
        consultaCliente = conex.consultarBanco(f'''
        SELECT "nomeCLIENTE" from "Cliente"
        WHERE "idCLIENTE" = {aluguel[2]};
        ''')
        for c in consultaCliente:
            consultaVeiculo = conex.consultarBanco(f'''
            SELECT * from "Veiculo"
            WHERE "refVEICULO" = {aluguel[3]};
            ''')
            for v in consultaVeiculo:
                veiculo = f"{v[2]} {v[1]} {v[7]} {v[6]} {v[5]}"
                print(f"\nALUGUEL SELECIONADO\n\nID ALUGUEL - {aluguel[0]}\nCLIENTE - {c[0]} | ID - {aluguel[2]}\nVEÍCULO - {veiculo} | REF - {aluguel[3]}\nDATA - {aluguel[1]}\nVALOR ALUGUEL - {v[3]}")

    idCLIENTE = input("\nInsira o ID do novo cliente: ")
    refVEICULO = input("Insira o REF do novo veículo: ")
    dataALUGUEL = inputDataAluguel(conex)
    conex.manipularBanco(f'''
    UPDATE "Aluguel"
    SET
    "dataALUGUEL" = '{dataALUGUEL}',
    "idCLIENTE" = '{idCLIENTE}',
    "refVEICULO" = '{refVEICULO}'
    WHERE "idALUGUEL" = '{idALUGUEL}';
    ''')
    sleep(1)
    print("\nCaso o ID informado pertença a algum aluguel, o mesmo acaba de ser deletado com sucesso.")

def manipularAlugueis(conex):
    while True:
        sleep(1)
        menu = input("\nO que fazer?\n\n1- Adicionar aluguel\n2- Remover aluguel\n3- Atualizar aluguel\n0- Voltar\n\n")
        match menu:
            case "1":
                addAluguel(conex)
            case "2":
                delAluguel(conex)
            case "3":
                attAluguel(conex)
            case "0":
                break
            case other:
                print("Ação inválida.")