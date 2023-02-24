import psycopg2
from time import sleep

def sleep(time):
    sleep(time)

class Conexao:
    def __init__(self, parametroDb, parametroUser, parametroPassword, parametroHost, parametroPort):
            self._db = psycopg2.connect(database= parametroDb, user= parametroUser, password= parametroPassword, host= parametroHost, port= parametroPort)

    def consultarBanco(self, sql):
        cursor = self._db.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()

        return resultado

    def manipularBanco(self, sql):
        cursor = self._db.cursor()

        cursor.execute(sql)

        self._db.commit()
        
        cursor.close

    def fechar(self):
        self._db.close()

    def createDatabase(conex):
        conex.manipularBanco('''
        DROP DATABASE IF EXISTS
        CREATE DATABASE "Locadora"
        WITH
        OWNER = postgres
        ENCODING = 'UTF8'
        CONNECTION LIMIT = -1
        IS_TEMPLATE = False;
        ''')

    def createTableCliente(conex):
        conex.manipularBanco('''
        CREATE TABLE "Cliente"(
        "idCLIENTE" int GENERATED ALWAYS AS IDENTITY,
        "nomeCLIENTE" varchar(255),
        "cpfCLIENTE" varchar(14) UNIQUE NOT NULL,
        "telefoneCLIENTE" varchar(15),
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
        "dataALUGUEL" date default null,
        "idCLIENTE" int UNIQUE,
        "refVEICULO" int UNIQUE,
        PRIMARY KEY ("idALUGUEL"),
        CONSTRAINT fk_cliente
            FOREIGN KEY ("idCLIENTE")
            REFERENCES "Cliente"("idCLIENTE")
            ON DELETE CASCADE
            ON UPDATE NO ACTION
        ,
        CONSTRAINT fk_veiculo
            FOREIGN KEY("refVEICULO")
            REFERENCES "Veiculo"("refVEICULO")
            ON DELETE CASCADE
            ON UPDATE NO ACTION
        );
        ''')