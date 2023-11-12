'''
Aqui é feita a filtragem e a separação de dados por mês para a exportação de arquivos em formato .csv 
'''

import pandas as pd
import os

with open("output/final.txt", "r") as file:
    data_str = file.read()

valid_rows = []

for row in data_str.split("\n"):
    values = row.split(";")[:7]

    if len(values) == 7:
        try:
            data = pd.to_datetime(values[0], format="%Y-%m-%d")
            # Verificar se o ano é razoável (por exemplo, entre 2000 e 2100)
            if 2000 <= data.year <= 2100:
                valid_rows.append(values)
        except ValueError:
            pass  # Ignorar a linha se não for possível converter a data

# Criar o dataframe com as colunas especificadas
colunas = ["DATA", "HORA", "Umi", "Temp", "Gas", "P2.5", "P10"]
df = pd.DataFrame(valid_rows, columns=colunas)

# Converter a coluna "DATA" para o formato datetime
df["DATA"] = pd.to_datetime(df["DATA"])

# Criar uma nova coluna "MES" contendo apenas o mês de cada data
df["MES"] = df["DATA"].dt.month

# Exportar os dados separados por mês para arquivos CSV

if not os.path.isdir('datapermonth'):
    os.makedirs('datapermonth')


for mes in df["MES"].unique():
    df_mes = df[df["MES"] == mes]
    df_mes.to_csv(f"datapermonth/dados_mes_{mes}.csv", index=False)

print("Os dados foram processados, validados, separados por mês e exportados para arquivos CSV.")
