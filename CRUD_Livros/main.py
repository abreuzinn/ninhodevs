# Livro_id
# Livro_nome
# Livro_paginas
# Livro_anoLançamento
# Livro_autor
# - Especificar os tipos de cada atributo e criar função no python createTableLivros
# - Usar o código abaixo para criar um CRUD, sistema de gerenciamento da tabela

import psycopg2 # import da biblioteca

def createTableLivros(curs, conex): # funcao de criar a tabela de livros na database
    curs.execute('''
    CREATE TABLE "Livros"(
    "ID_livro" serial,
    "NOME_livro" varchar(255),
    "PAGINAS_livro" integer,
    "ANO_livro" integer,
    "AUTOR_livro" varchar(255),
    PRIMARY KEY ("ID_livro")
    );
    ''')
    conex.commit()

def showLivros(curs): # lista todos os livros da database
    curs.execute('''
    SELECT * FROM "Livros"
    ''')
    livros = cursor.fetchall()
    for livro in livros:
        print(f"\nID - {livro[0]}\nNOME - {livro[1]}\nPÁGINAS - {livro[2]}\nANO - {livro[3]}\nAUTOR - {livro[4]}")

def showLivroEspecifico(curs): # visualizar livro especifico
    while True:
        try:
            livroEscolhido = int(input("Insira o ID do livro para visualizá-lo: "))
        except:
            TypeError(print("O ID de um livro deve ser um valor númerico. Tente novamente."))
        curs.execute(f'''
        SELECT * FROM "Livros"
        WHERE "ID_livro" = {livroEscolhido};
        ''')
        livro = curs.fetchone()
        try:
            print(f"\nID - {livro[0]}\nNOME - {livro[1]}\nPÁGINAS - {livro[2]}\nANO - {livro[3]}\nAUTOR - {livro[4]}")
            break
        except:
            print(f"Nenhum livro possui esse ID.")
            break

def addLivro(curs, conex): # adicionar um livro na database
    nomeLivro = input("\nInsira o nome do livro: ")
    while True:
        try:
            paginasLivro = int(input("Insira o número de páginas do livro: "))
            break
        except:
            TypeError(print("Insira o valor utilizando apenas números. Tente novamente."))
    while True:
        try:
            anoLivro = int(input("Insira o ano de lançamento do livro: "))
            break
        except:
            TypeError(print("Insira o ano utilizando apenas números. Tente novamente."))
    autorLivro = input("Insira o autor do livro: ")

    curs.execute(f'''
    INSERT INTO "Livros"
    VALUES(default, '{nomeLivro}', {paginasLivro}, {anoLivro}, '{autorLivro}');
    ''')
    conex.commit()
    print("Livro cadastrado com sucesso.")

def attLivro(curs, conex): # atualizar dados de um livro
    while True:
        try:
            idLivro = int(input("Insira o ID do livro que deseja alterar: "))
        except:
            TypeError(print("O ID informado deve ser um número de um livro existente. Tente novamente."))
        curs.execute('''
        SELECT * FROM "Livros";
        ''')
        livroEscolhido = curs.fetchone()
        print(f"Livro escolhido: {livroEscolhido[1]}\nAutor: {livroEscolhido[4]}")
        novoNome = input("Insira o novo nome do livro: ")
        while True:
            try:
                novoPaginas = int(input("Insira o novo número de páginas do livro: "))
                break
            except:
                TypeError(print("Insira o valor utilizando apenas números. Tente novamente."))
        while True:
            try:
                novoAno = int(input("Insira novo o ano de lançamento do livro: "))
                break
            except:
                TypeError(print("Insira o ano utilizando apenas números. Tente novamente."))
        novoAutor = input("Insira o novo autor do livro: ") 
        curs.execute(f'''
        UPDATE "Livros"
        SET
        "NOME_livro" = '{novoNome}',
        "PAGINAS_livro" = {novoPaginas},
        "ANO_livro" = {novoAno},
        "AUTOR_livro" = '{novoAutor}';
        ''')
        conex.commit()
        print("Livro atualizado com sucesso.")

def delLivro(curs, conex): # funcao para deletar um livro da database
    while True:
        try:
            idLivro = int(input("Insira o ID do livro que deseja deletar (insira 0 para cancelar): "))
            match idLivro:
                case 0:
                    break
                case other:
                    while True:
                        curs.execute(f'''
                        SELECT * FROM "Livros"
                        WHERE "ID_livro" = {idLivro};
                        ''')
                        livroEscolhido = curs.fetchone()
                        try:
                            acceptDelete = input(f"\nVocê quer mesmo excluir o seguinte livro?\n\nLIVRO - {livroEscolhido[1]}\nAUTOR - {livroEscolhido[4]}\n\n1- CONFIRMAR\n2- CANCELAR\n\n")   
                        except:
                            TypeError(print("O ID informado não existe. Tente novamente."))
                            break
                        match acceptDelete:
                            case "1":
                                curs.execute(f'''
                                DELETE FROM "Livros"
                                WHERE "ID_livro" = {idLivro};
                                ''')
                                conex.commit()
                                print("Livro deletado com sucesso.")
                                break
                            case "2":
                                print("Ação cancelada.")
                                break
                            case other:
                                print("Ação inválida. Tente novamente.")
        except:
            TypeError(print("O ID tem que ser um número. Tente novamente."))

try: # tentar conectar com o postgres
    con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = con.cursor()
    print("Connected")
except(Exception, psycopg2.Error) as error: # caso algo de errado, fica mais facil ver o erro
    print(f"Something went wrong - {error}")

# createTableLivros() # comentada pq ja foi utilizada

while True: # menu CRUD
    menu = input("\nO que fazer?\n\n1- Mostrar livros\n2- Consultar livro específico\n3- Cadastrar livro\n4- Atualizar informações de um livro\n5- Remover livro\n0- Encerrar programa\n\n")
    match menu:
        case "1": # chamar funcao para listar os livros
            showLivros(cursor)
        case "2": # chamar funcao para visualizar livro especifico
            showLivroEspecifico(cursor)
        case "3": # chamar funcao para cadastrar um livro
            addLivro(cursor, con)
        case "4": # chamar funcao para atualizar dados de um livro
            attLivro(cursor, con)
        case "5": # chamar funcao para deletar um livro
            delLivro(cursor, con)
        case "0": # encerrar o programa
            print("Programa encerrado.")
            break
        case other:
            print("\nAção inválida. Tente novamente.")