CREATE TABLE "Alunos"(
    matALUNO int GENERATED ALWAYS AS IDENTITY,
    nomeALUNO varchar(255),
    cpfALLUNO char(14) UNIQUE,
    enderecoALUNO varchar(255),
    telefoneALUNO varchar(15),
    nascimentoALUNO date,
    PRIMARY KEY (matALUNO)
);

INSERT INTO "Alunos"
VALUES(
    'default',
    'Abreu',
    '123.456.789-10',
    'Rua mansao maromba foda muito foda 666',
    '(12) 34567-8910',
    '18-01-2004'
);

CREATE TABLE "Disciplina"(
    codDISCIPLINA INT GENERATED ALWAYS AS IDENTITY,
    nomeDISCIPLINA VARCHAR(255),
    codCURSO INT,
    PRIMARY KEY (codDISCIPLINA)
);

INSERT INTO "Disciplina"
VALUES(
    'default',
    'Matemática',
    '3'
);

CREATE TABLE "Matricula"(
    numMATRICULA INT GENERATED ALWAYS AS IDENTITY,
    semestre INT,
    ano INT,
    numFALTAS INT,
    PRIMARY KEY (numMATRICULA)
);

INSERT INTO "Matricula"
VALUES(
    'default',
    '1',
    '2023',
    '2'
);