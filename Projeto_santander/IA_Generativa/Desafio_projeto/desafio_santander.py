import sqlite3 as conector

try:
  # abertura da conexão
  conexao = conector.connect('/home/matheus/Documentos/MeusProjetos/Data-Science/Projeto_santander/IA_Generativa/Desafio_projeto/desafio.db')
# aquisição de um cursor
  cursor = conexao.cursor()

  comando_01 = '''
  CREATE TABLE usuario
  (
  id INT(11) NOT NULL,
  nome VARCHAR(30) NOT NULL,
  PRIMARY KEY (nome)
  )
  '''
  comando_02 = '''
  CREATE TABLE account
  (
  number_account VARCHAR(7) NOT NULL,
  agency VARCHAR(4) NOT NULL,
  balance INTEGRER(10),
  limit_account INTEGRER(10) NOT NULL,
  FOREIGN KEY (nome) REFERENCES usuario (nome),
  FOREIGN KEY (number_card) REFERENCES card (number_card),
  PRIMARY KEY (number_account)
  );
  '''

  comando_03 = '''
  CREATE TABLE card
  (
  number_card VARCHAR(20) NOT NULL,
  limit_card INTEGRER(20) NOT NULL,
  PRIMARY KEY (number_card)
  );
  '''
  # comando_04 = '''
  # CREATE TABLE feactures
  # (
  # number_card VARCHAR(20) ,
  # limit_card INTEGRER(20) ,
  # PRIMARY KEY (number_card)
  # );
  # '''
  # comando_05 = '''
  # CREATE TABLE news
  # (
  # number_card VARCHAR(20) ,
  # limit_card INTEGRER(20) ,
  # PRIMARY KEY (number_card)
  # );
  # '''
  # execução do comando: SELECT, INSERT, CREATE...
  cursor.execute(comando_01)
  cursor.execute(comando_02)
  cursor.execute(comando_03)

# Efetivação do comando
  conexao.commit()

except conector.DatabaseError as erro:
  print('Erro no banco de dados', erro)
finally:
  # fechamento das conexoes
  cursor.close()
  conexao.close()
