import requests
from bs4 import BeautifulSoup
import operator #implementa operadores + - * /
from collections import Counter #lib ajuda na manipulação de listas, tuplas etc.


def start(url): #define o webcrawler

    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser') #soup baixa codigo html

    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}): #acha html na pagina, procura tudo em div e class
        content = each_text.text #transforma html em texto

        words = content.lower().split() #converte o conteudo em letras minusculas
        #corta cada conteudo em uma linha
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist): #remove qualquer simbolo indesejado da wordlist
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%¨&*()_-+={[]}|\;:"<>?/., ' #removera simbolos, substituindo por nada

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0: #se word maior que 0, limpa a lista
            clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list): #criacao de dicionario e contagem
    word_count = {}

    for word in clean_list:  #exibe a contagem e top 10 de palavras mais utilizadas
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    #contador mostra palavras chave mais frequentes no site
    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print ("% s: % s " % (key, value))

    c = Counter(word_count) #contador do collections
    top = c.most_common(10) #top 10 de palavras + frequentes
    print(top)

if __name__ == '__main__': #chama a funcao mais e passa o site
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')