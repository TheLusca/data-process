"""
Aqui é feita a correção dos dados brutos gerados pelos sensores para armazenamento na base de dados
Ajuste de codigo para um novo formato de dados geredos pelos sensores 

"""
import os


arquivo = open('data/new format/TEST_04_09.TXT', 'r',
               encoding='utf-8', errors='ignore')
dados = arquivo.readlines()

if not os.path.isdir('output'):
    os.makedirs('output')

temp = open('output/temp.txt', 'w', encoding='utf-8', errors='ignore')
# eliminar cabeçalho, espaços e outras coisas
for linha in dados:
    if not '-----------------------------------------' in linha:
        linha = linha.replace('  ', ';').replace(' ', '').replace('/', '-').replace('Umidade:', '').replace(
            'Temperatura:', '').replace('P2.5:', '').replace('P10', '').replace(';;', ';').replace(':;', ';')
        temp.write(linha)


print('Limpeza inicial concluída!')
arquivo.close()
temp.close()

# segunda varredura
with open('output/temp.txt', 'r', encoding='utf-8', errors='ignore') as file:
    contents = file.read()
    contents = contents.replace('%', '').replace('ºC', '').replace(';;', ';')

with open('output/final.txt', 'w', encoding='utf-8', errors='ignore') as file:
    file.write(contents)

os.remove('output/temp.txt')


print('Limpeza de dados concluída')
print('Dados salvos no arquivo final.txt')
