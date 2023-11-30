import pandas as pd
import matplotlib.pyplot as plt

# Supondo que o seu DataFrame seja chamado 'df'
df = pd.read_csv('data/Ailton-setembro-Ramal-dos-Coelhos.csv')

# Supondo que o seu DataFrame seja chamado 'df'
# Especificando o formato da data
df['Hora'] = pd.to_datetime(df['Hora'], format='%H:%M:%S')

# Criando uma nova coluna 'Hora do Dia' que contém apenas a parte da Hora
df['Hora do Dia'] = df['Hora'].dt.hour

# Criando um DataFrame com todas as horas do dia
horas_do_dia = pd.DataFrame({'Hora do Dia': range(24)})

# Mesclando o DataFrame com todas as horas do dia com o DataFrame original
df_completo = pd.merge(horas_do_dia, df, on='Hora do Dia', how='left')

# Agrupando os dados pelo 'Hora do Dia' e calculando a média do P10
p10_media_por_hora = df_completo.groupby('Hora do Dia')['PM2.5'].mean()

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(p10_media_por_hora, marker='o', linestyle='-', color='b')

# Adicionando rótulos e título
plt.xlabel('Hora do Dia')
plt.ylabel('Média de PM2.5(μg/m³)')
plt.title('Tendência de PM2.5(μg/m³) ao Longo do Dia')

# Definindo os rótulos do eixo x
plt.xticks(range(24))

# Exibindo o gráfico
plt.grid(True)
plt.savefig('tendencia_p2.5_Abr.png')  # Salvar o gráfico em um arquivo
plt.show()
