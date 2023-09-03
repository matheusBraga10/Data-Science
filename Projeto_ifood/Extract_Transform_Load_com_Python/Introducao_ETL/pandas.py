'''
Pandas é uma biblioteca de Python que trabalha com a manipulação de dados 
estruturada como é feito no excel

 - Serie - é uma matriz unidimensional que contém uma sequencia de valores que representam uma indexação, muito parecida com uma única coluna no excel

 - DataFrame - é uma estrutura de dados tabular, semelhante a planilha de dados do excel, em que tanto as linhas quanto colunas apresentam rótulos
 
 * DataFrames são junção de series
'''

import pandas as pd

url_01 = 'https://raw.githubusercontent.com/Mutalimekala/python/master/Resp2.csv'
df_01 = pd.read_csv(url_01)

url_02 = 'https://raw.githubusercontent.com/Mutalimekala/python/master/Salaries.csv'
sf_01 = pd.read_csv(url_02)

sf_01.head()