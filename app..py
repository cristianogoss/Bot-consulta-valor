from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
from datetime import datetime

# Função para configurar como a página vai ser aberta
def configurar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    return webdriver.Chrome(options=chrome_options)

# função para abrir a página
def abrir_pagina(driver, url):
    driver.get(url)
    sleep(2)

# Função para coletar os dados
def coletar_dados():
    driver = configurar_driver()

    url_um = "https://www.tumelero.com.br/resultado-busca?terms=cimento"
    abrir_pagina(driver, url_um)
    cimento = driver.find_element(By.XPATH, '//*[@id="vitrine-products-smarthint"]/div[1]/ul/li[1]/article/div[3]/p/span[1]').text
    sleep(1)

    url_dois = "https://www.tumelero.com.br/resultado-busca?terms=cal"
    abrir_pagina(driver, url_dois)
    cal = driver.find_element(By.XPATH, '//*[@id="vitrine-products-smarthint"]/div[1]/ul/li[1]/article/div[3]/p/span[1]').text
    sleep(1)

    url_tres = "https://www.tumelero.com.br/resultado-busca?terms=areia"
    abrir_pagina(driver, url_tres)
    areia_grossa = driver.find_element(By.XPATH, '//*[@id="vitrine-products-smarthint"]/div[1]/ul/li[2]/article/div[3]/p/span[1]').text
    sleep(1)
    
    driver.quit()
    return {"Cimento - saco 50kg": (cimento, url_um), "Cal - saco 20kg": (cal, url_dois), "Areia grossa - saco 20kg": (areia_grossa, url_tres)}

# função para salvar os dados no excell
def salvar_para_excel(dados):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Materiais"

    # Data atual
    data_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Cabeçalhos
    sheet.append(["Data", data_atual])
    sheet.append(["Material", "Valor", "URL"])

    # Dados
    for key, value in dados.items():
        valor, url = value
        sheet.append([key, valor, url])
    
    # Configurar largura das colunas
    sheet.column_dimensions['A'].width = 30  # Ajuste conforme necessário
    sheet.column_dimensions['B'].width = 20
    sheet.column_dimensions['C'].width = 60

    workbook.save("materiais.xlsx")

# Coleta os dados
dados = coletar_dados()
print(dados)

# Salva os dados em uma planilha Excel
salvar_para_excel(dados)
