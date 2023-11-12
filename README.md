
# Tratamento de dados gerados pelos sensores pertencentes ao Projeto Cuidadores do ar

## 📕 Descrição

Este repositorio contem rotinas realizam limpezas nos dados brutos gerados pelos sensores e os exportam em formatam em .csv prontos para serem visualizados

Características dos dados: data (yyyy-mm-dd), hora (hh-mm-ss), umidade (%), temperatura (°C), presença de gases tóxicos, MP2.5 ($\mu g/m^3$), MP10 ($\mu g/m^3$)


## ⚙️ Instalação

1. Clonar o repositório usando a linha de comando

```bash
git clone https://github.com/TheLusca/data-process.git
```

2. Baixar o zip:
https://github.com/TheLusca/data-process

## 💻 Execução Local

Requisitos:

    Linguagem Python, versão 3 ou superior

    Gerenciador de pacotes pip, versão 3 ou superior 

Instalar bibliotecas utilizando o comando no terminal:
> pip install requirements.txt


## ✳️ Observações

- `main.py` é reponsavel por receber os dados e realizar a limpeza e ele salva na pasta `output`
- `export.py` é onde os dados são exportados para .csv na pasta `datapermonth`


## ✳️ Observações

- No momento, os pesos da rede pré-treinada `output` são utilizados. Posteriormente os pesos serão substituidos pelos treinados durante o desenvolvimento do projeto.
