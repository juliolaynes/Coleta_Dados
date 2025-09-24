import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get('https://books.toscrape.com/')
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, "html.parser")

contar_livros = 0
catalogo = []

def truncar_titulo(titulo):
    palavras = titulo.split()
    if len (palavras) > 4:
        return ' '.join(palavras[:4]) + '...'
    return titulo

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    titulo = artigo.find('h3').find('a')['title']
    titulo_truncado = truncar_titulo(titulo)
    preco = artigo.find('p', class_='price_color').text.strip()
    livro['Título'] = titulo_truncado
    livro['Preço'] = preco
    catalogo.append(livro)
    contar_livros += 1

    titulos = [livro['Título'] for livro in catalogo]
    precos = [livro['Preço'] for livro in catalogo]

    print(titulos)
    print(precos)
    contar_livros = len(catalogo)
    print('Total livros:', contar_livros)

