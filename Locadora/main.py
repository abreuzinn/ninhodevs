import psycopg2
from classConexao import Conexao
from menuVeiculo import *
from menuCliente import *
from menuAluguel import *

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

# con.createTableVeiculo()
# con.createTableCliente()
# con.createTableAluguel()

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
        case other:
            print("Ação inválida.")






