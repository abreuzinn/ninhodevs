import psycopg2
from time import sleep
from classConexao import Conexao
from menuVeiculo import *
from menuCliente import *
from menuAluguel import *

while True:
    try:
        user = input("Insira o usuário: ")
        password = input("Insira a senha: ")
        sleep(1)
        # login e senha "postgres"

        con = Conexao("Locadora", user, password, "localhost", "5432" )
        print(f"Conectado com sucesso.")
        break

    except (Exception, psycopg2.Error) as error:
        print(f"oops - {error}")

while True:
    sleep(1)
    createDb = input(f'\nDeseja criar o banco de dados "Locadora" e as tabelas necessárias?\n\n1- Sim\n2- Não\n\n')
    match createDb:
        case "1":
            try:
                con.createDatabase()
                con.createTableVeiculo()
                con.createTableCliente()
                con.createTableAluguel()
                sleep(1)
                print("\nO banco de dados e as tabelas foram criados com sucesso.")
                con.fechar()
                break
            except(psycopg2.Error) as error:
                print(f"\noops - {error}")
                con.fechar()
        case "2":
            break
        case other:
            print("\nAção inválida.")

while True:
    sleep(1)
    menu = input("\nO que fazer?\n\n1- Menu veículos\n2- Menu clientes\n3- Menu aluguéis\n0- Encerrar\n\n")
    match menu:
        case "1":
            showMenuVeiculos(con)
        case "2":
            showMenuClientes(con)
        case "3":
            showMenuAlugueis(con)
        case "0":
            sleep(1)
            print("\nEncerrando...")
            break
        case other:
            sleep(1)
            print("\nAção inválida.")






