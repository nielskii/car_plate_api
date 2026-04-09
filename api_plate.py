from bs4 import BeautifulSoup
import requests
import cloudscraper
import json

'''Possiveis sites para raspar:
    https://placafipe.com/placa/{placa_aqui},
    https://placaipva.com.br/placa/{placa_aqui}
'''

def fetch_data(query):
    url = f'https://www.keplaca.com/placa/{query}'
    scraper = cloudscraper.create_scraper(
        browser = {
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        }
    )
    response = scraper.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text,'html.parser')
    tabela= soup.find('table',class_="fipeTablePriceDetail")
    dados = {}
    if tabela:
        for linha in tabela.find_all('tr'):
            colunas = linha.find_all('td')
            if len(colunas) == 2:
                chave = colunas[0].text.strip().replace(':','')
                valor = colunas[1].text.strip()
                dados[chave] = valor
    return dados
    