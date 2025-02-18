import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

extracao = BeautifulSoup(requisicao.text, 'html.parser')
# Exibe os primeiros 2000 caracteres do site

# print(requisicao.text[:2000])

print(extracao.prettify()[:2000])