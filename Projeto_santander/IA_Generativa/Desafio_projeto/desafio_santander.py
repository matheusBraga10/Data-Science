import sqlite3 as conector
import zipfile 
from pyspark.sql import SparkSession
import os
import findspark


os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"

os.environ["SPARK_HOME"] = "/content/spark-3.1.2-bin-hadoop2.7"


findspark.init()

try:
  path = '/home/matheus/Documentos/MeusProjetos/Data-Science/Projeto_santander/IA_Generativa/Desafio_projeto/'
  spark = SparkSession.buider.master('local[*]').appName('Iniciando com Spark').config('spark.ui.port','4050').getOrCreate()
  zipfile.Zipfile('/home/matheus/Documentos/MeusProjetos/Data-Science/Projeto_santander/IA_Generativa/Desafio_projeto/archive.zip','r').extractall('/home/matheus/Documentos/MeusProjetos/Data-Science/Projeto_santander/IA_Generativa/Desafio_projeto/')

  
  

except conector.DatabaseError as erro:
  print('Erro no banco de dados', erro)
finally:
  # fechamento das conexoes
  cursor.close()
  conexao.close()
