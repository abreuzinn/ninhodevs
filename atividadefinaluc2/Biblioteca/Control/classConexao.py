import psycopg2

class Conexao:
  def __init__(self, db, usuario, senha, hospede, porta):
    self._conexao = psycopg2.connect(database=db, user= usuario, password=senha, host=hospede, port=porta)
  
  def consultarBanco(self, sql):
    cursor = self._conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado
  
  def manipularBanco(self, sql):
    cursor = self._conexao.cursor()
    cursor.execute(sql)
    self._conexao.commit()
    cursor.close()
    
  def fecharConexao(self):
    self._conexao.close()

  # def createTableCliente(self):
    # CREATE TABLE Cliente(
    # 	id INT GENERATED ALWAYS AS IDENTITY,
    # 	nome VARCHAR(255) NOT NULL,
    # 	cpf CHAR(11) NOT NULL UNIQUE,
    # 	PRIMARY KEY (id)
    # );

  # def createTableLivro(self)
    # CREATE TABLE Livro(

    # 	id INT GENERATED ALWAYS AS IDENTITY,
    # 	nome VARCHAR(255) NOT NULL,
    # 	autor VARCHAR(255) NOT NULL,
    # 	PRIMARY KEY(id)
    # );
    
  # def createTableAluguel(self)
    # CREATE TABLE Aluguel(
    #         id int GENERATED ALWAYS AS IDENTITY,
    #         id_cliente int NOT NULL,
    #         id_livro int NOT NULL,
    #         data_aluguel TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    #         PRIMARY KEY(id),
    #         Constraint fk_cliente
    #             FOREIGN KEY (id_cliente)
    #             REFERENCES clientes (id)
    #             ON DELETE CASCADE
    #             ON UPDATE NO ACTION
    #             ,
    #         Constraint fk_livro
    #             FOREIGN KEY (id_livro)
    #             REFERENCES livros (id)
    #             ON DELETE SET NULL
    #             ON UPDATE NO ACTION 
    # );