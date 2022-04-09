from bs4 import BeautifulSoup #soup é uma brincadeira com sopa de letrinhas

import requests

site = requests.get('https://www.climatempo.com.br/').content ##pega html do site passado ao get
#obj site recebe conteudo da requisicao http do site...
soup = BeautifulSoup(site, 'html.parser')
#obj soup baixa do site o html
#print(soup.prettify())
#transforma html em str; print exibe o html

previsao = soup.find("h4", class_="-gray-dark-2 -font-base -bold")

print(previsao.string) #transforma hmtl em str ou texto
print(soup.title) #imprime somente titulo da tag
print(soup.title.string) #imprime titulo convertido em str
print('-' * 60)
print(soup.a) #imprime 1a tag a (ancora)
print(soup.p.string) #imprime 1a tag p
print(soup.find('admin')) #levantamento de informacoes sobre admin da pagina
print('-' * 60)