from psycopg2 import Error
from Control.classConexao import Conexao
from Model.classCliente import Cliente
from Model.classLivro import Livro

while True:
    try:
        con = Conexao("Biblioteca", "postgres", "postgres", "localhost", "5432")
        print("Conectado")
        break

    except (Error) as error:
        print("Ocorreu um erro -", error)


while True:
    try:
        menu = input(f"\nO que fazer?\n\n1- MOSTRAR CLIENTES\n2- MOSTRAR LIVROS\n3- MOSTRAR ALUGUÉIS\n0- SAIR\n\n")
        match menu:
            case "1":
                Cliente.menuClientes(con)
            case "2":
                Livro.menuLivros(con)
            case "3":
                Cliente.menuAlugueis(con)
            case "0":
                print("Saindo da aplicação...")
                con.fechar()
                break
            case other:
                print("Ação inválida.")

    except (Error) as error:
        print("Ocorreu um erro -",error)