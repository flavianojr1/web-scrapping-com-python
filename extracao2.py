import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    for h3 in artigo.find('h3'):
        titulo = h3.text
        livro['Título'] = titulo
    for price in artigo.find('p', class_='price_color'):
        preco = price.text
        livro['Preço'] = preco
    # print('Nome do livro: "{}".Valor do livro: {}\n\n'.format(titulo, preco))
    catalogo.append(livro)
    contar_livros += 1


print('Total livros:', contar_livros)