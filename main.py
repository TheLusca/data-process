'''
Aqui é feita a correção dos dados brutos gerados pelos sensores para armazenamento na base de dados
'''
import os

arquivo = open('data/TEST_19_06_Felipe.TXT','r',encoding='utf-8', errors='ignore')
dados = arquivo.readlines()

temp1 = open('output/temp1.txt','w', encoding='utf-8', errors='ignore')

for linha in dados:
    if not '-----------------------------------------' in linha:        
        linha = linha.replace(':  ',':').replace(';;', ';').replace(' ', '').replace('Â', '').replace('Umidade:', '').replace('Temperatura:', '').replace(' :  ','')                        
        temp1.write(linha)

print('pré-processamento concluído!')
arquivo.close()
temp1.close()

entrada = open("output/temp1.txt", "r")
saida = open("output/temp2.txt", "w")

print('...')

for i, linha in enumerate(entrada):
    # Ignorar as linhas ímpares
    if i % 1 == 2:
        continue
    
    linha1 = linha.strip()
    linha2 = entrada.readline().strip()
    # Concatenar as duas linhas separadas por um espaço
    resultado = linha1 + ";" + linha2
    
    # Escrever o resultado no arquivo de saída
    saida.write(resultado + "\n")

# Fechar os arquivos
entrada.close()
saida.close()


with open('output/temp2.txt', 'r',encoding='utf-8', errors='ignore') as file:
    
    contents = file.read()
    contents = contents.replace('/', '-').replace('%', '').replace('ºC', '').replace('P10','').replace('P2.5:','').replace(';:', ';')

with open('output/final.txt', 'w',encoding='utf-8', errors='ignore') as file:
    file.write(contents)

#os.remove('output/temp1.txt')
#os.remove('output/temp2.txt')

print('pós-processamento concluido!')


