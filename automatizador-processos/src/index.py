# importando a biblioteca do pandas que vai ser a responsável por ler o arquivo excel.
import pandas as pd
#Importando a biblioteca selenium que vai ser responsável por controlar e fazer os processos no site utilizando o webdriver por trás
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Abrir o navegador
navegador = webdriver.Chrome()
# Acessar o site para automação
url = "https://projetos.ati.pe.gov.br/redmine/issues/"
navegador.get(url)
# Colocar o navegador em tela cheia
navegador.maximize_window()
# Selecionando o campo de login e preenchendo com os dados
campoLogin = navegador.find_element(By.ID, 'username')
campoLogin.clear()
campoLogin.send_keys('pablo.henrique1')
# Selecionando o campo de senha e preenchendo com os dados
CampoSenha = navegador.find_element(By.ID, 'password')
CampoSenha.clear()
CampoSenha.send_keys("@Tais84671514")
# Selecionando e clicando no botão para realizar o processo de autenticação
botaoSubmit = navegador.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
botaoSubmit.click()

# Expandir a quantidade de processos
containerNavegacao = navegador.find_element(By.CLASS_NAME, 'pagination')
ultimaPag = containerNavegacao.find_element(By.XPATH, "(//a)[4]")
ultimaPag.click()

# Processar a tabela
try:
    # Pega todas as linhas da tabela
    linhas = navegador.find_elements(By.TAG_NAME, 'tr')
    
    # Itera sobre todas as linhas, exceto a primeira (cabeçalho)
    for i, linha in enumerate(linhas):
        if i == 0:  # Ignorar a primeira linha (cabeçalho)
            continue

        # Pega as células (td) da linha
        colunas = linha.find_elements(By.TAG_NAME, 'td')

        # Verifica se a linha tem pelo menos 2 colunas
        if len(colunas) > 1:
            # Pega a segunda coluna (índice 1)
            segunda_coluna = colunas[1]
            
            try:
                # Tenta encontrar um link <a> dentro da segunda coluna
                numeroProcesso = segunda_coluna.find_element(By.TAG_NAME, 'a')
                numeroProcesso.click()
                containerDiv = navegador.find_element(By.CLASS_NAME, 'cf_60')
                appScript = containerDiv.find_element(By.CLASS_NAME, 'value')
                simNao = appScript.text
                navegador.back()

                print(f"{i} Processo encontrado: {numeroProcesso.text} foi usado script? {simNao}")
              
            except Exception as e:
                print("Nenhum link encontrado na segunda coluna.")
        
except Exception as e:
    print(f"Erro ao processar a tabela: {e}")

time.sleep(10)


