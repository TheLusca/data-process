'''
Aqui é feita a transformação da nossa base de dados em dataframes e 
é feita a exportação para o arquivo final em csv
'''

import pandas as pd

# Lendo os dados do arquivo
with open("output/final.txt", "r") as file:
    data_str = file.read()

# Separar os valores em cada linha e criar uma lista de listas com os valores
rows = [line.split(";")[:7] for line in data_str.split("\n")]

# Criar o dataframe com as colunas especificadas
columns = ["Data", "Hora", "Umidade", "Temperatura", "Gas", "P2.5", "P10"]
df = pd.DataFrame(rows, columns=columns)

# Exibir o dataframe
df.to_csv("output/dados_exportados.csv", index=False)
print('Dados exportados!')