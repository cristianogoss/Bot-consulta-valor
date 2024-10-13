# Automação de Consulta de Preços

Este projeto é um script em Python que automatiza a consulta de preços de materiais para Construção de um determinado site, e cria uma planilha Excel com os preços coletados 

## Funcionalidades

1. **Consulta Automatizada**:
   - Acessa o site
   - Verifica o preço atual dos materiais de construção (cimento, cal e areia)
   - Guarda o valor do preço (somente o valor numérico).

2. **Manipulação de Planilhas**:
   - Cria uma planilha com as seguintes colunas:
     - Material (nome do produto)
     - Data atual (data da consulta)
     - Valor (preço do produto)
     - Url (link direto para o produto)

## Requisitos

- Python 3.x
- Bibliotecas:
  - `selenium`
  - `datetime`
  - `openpyxl`
  - `schedule`

### Instale as dependências
pip install -r requirements.txt

### Execute o script
python app.py

### Vídeo da automação em funcionamento
https://youtu.be/8pcrWXGOuRw
