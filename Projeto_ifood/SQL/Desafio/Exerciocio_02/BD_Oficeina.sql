
--Script para criar o Banco de Dados (BD_Oficina) e suas tabelas, al�m de popul�-las.

CREATE DATABASE BD_Oficina
GO

USE BD_Oficina
GO

CREATE TABLE Departamentos
(
Cod_depa CHAR(2) NOT NULL,
Nome_depa VARCHAR(20) NOT NULL,
Localizacao VARCHAR(20) NOT NULL,
CONSTRAINT PK_Depa PRIMARY KEY (Cod_depa)
)
GO

CREATE TABLE Projetos
(
Cod_proj CHAR(2) NOT NULL,
Nome_proj VARCHAR(20) NOT NULL,
Orcamento money NOT NULL,
CONSTRAINT PK_Proj PRIMARY KEY (Cod_proj)
)
GO

CREATE TABLE Empregados
(
Cod_empr INT NOT NULL,
Pnome_empr VARCHAR(20) NOT NULL,
Unome_empr VARCHAR(20) NOT NULL,
Cod_depa CHAR(2) NOT NULL,
CONSTRAINT PK_Empr PRIMARY KEY (Cod_empr),
CONSTRAINT FK_Empr_Depa FOREIGN KEY (Cod_depa) REFERENCES Departamentos (Cod_depa)
)
GO

CREATE TABLE Empregados_em_Projetos
(
Cod_empr INT NOT NULL,
Cod_proj CHAR(2) NOT NULL,
Funcao VARCHAR(20) NULL,
Data_inicio DATETIME NOT NULL,
CONSTRAINT PK_Empr_Proj PRIMARY KEY (Cod_empr,Cod_proj),
CONSTRAINT FK_Empr_Proj_Empr FOREIGN KEY (Cod_empr) REFERENCES Empregados (Cod_empr),
CONSTRAINT FK_Empr_Proj_Proj FOREIGN KEY (Cod_proj) REFERENCES Projetos (Cod_proj) 
)
GO

INSERT INTO Departamentos VALUES('D1','Operações','Operações')
INSERT INTO Departamentos VALUES('D2','Contabilidade','Administrativo')
INSERT INTO Departamentos VALUES('D3','Marketing','Administrativo')
INSERT INTO Departamentos VALUES('D4','Gestão','Diretoria')
INSERT INTO Departamentos VALUES('D5','Controle','Diretoria')
GO

INSERT INTO Projetos VALUES('P1','Mecanica',120000)
INSERT INTO Projetos VALUES('P2','Eletrica',95000)
INSERT INTO Projetos VALUES('P3','Revisão',185600)
GO

INSERT INTO Empregados VALUES(25348,'Matthew','Smith','D3')
INSERT INTO Empregados VALUES(10102,'Ann','Jones','D2')
INSERT INTO Empregados VALUES(18316,'John','Barrimore','D1')
INSERT INTO Empregados VALUES(29346,'James','James','D2')
INSERT INTO Empregados VALUES(9031,'Elke','Dertoni','D4')
INSERT INTO Empregados VALUES(2581,'Elsa','Hansel','D5')
INSERT INTO Empregados VALUES(28559,'Sybill','Moser','D1')
GO

INSERT INTO Empregados_em_Projetos VALUES(10102,'P1','Analista','01/10/1997')
INSERT INTO Empregados_em_Projetos VALUES(10102,'P3','Gerente','01/01/1999')
INSERT INTO Empregados_em_Projetos VALUES(25348,'P2','Assistente','15/02/1998')
INSERT INTO Empregados_em_Projetos VALUES(18316,'P2',NULL,'01/06/1998')
INSERT INTO Empregados_em_Projetos VALUES(29346,'P2',NULL,'15/12/1997')
INSERT INTO Empregados_em_Projetos VALUES(2581,'P3','Analista','15/10/1998')
INSERT INTO Empregados_em_Projetos VALUES(9031,'P1','Gerente','15/04/1998')
INSERT INTO Empregados_em_Projetos VALUES(28559,'P1',NULL,'01/08/1998')
INSERT INTO Empregados_em_Projetos VALUES(28559,'P2','Assistente','01/02/1999')
INSERT INTO Empregados_em_Projetos VALUES(9031,'P3','Assistente','15/11/1998')
INSERT INTO Empregados_em_Projetos VALUES(29346,'P1','Assistente','04/01/1998')
GO
