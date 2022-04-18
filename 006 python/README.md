# Introdução à programação com Python

Conteúdos do curso: </br>

* Aprenda o que é a linguagem Python e como configurar o ambiente de desenvolvimento
* O que são variáveis e como manipulá-las através de operadores aritméticos e interação com usuário
* Como criar um código em Python que funcione de acordo com a  relação das variáveis
* Como criar laços de repetição em Python
* Como organizar os dados em uma lista ou tupla e realizar operações com elas 
* Organizando conjuntos e subconjuntos de elementos em Python
* Construindo métodos, funções e classes em Python
* Lidando com módulos, importação de classes, métodos e construção de funções anônimas (_lambda_)
* Gere, copie, mova, escreva e leia informações de arquivos externos
* Aprenda a utilizar informações de data, horário e relacionar datas diferentes
  </br>Ver "Comportamento de `strftime()` e `strptime()`" em [[1]](https://docs.python.org/pt-br/3.7/library/datetime.html#strftime-and-strptime-behavior).
* Gerenciando e criando exceções customizadas com `try`, `except`, `else` e `finally`
  </br>Ver "_Exception hierarchy_" em [[2]](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).
* Instalando e utilizando pacotes em Python e realizar requisição com `requests` </br>
**Ferramentas utilizadas:** </br>
Viacep API: site http://viacep.com.br/ </br>
Pesquisa por CEP (json): http://viacep.com.br/ws/01001000/json/ </br>
API PokeApi: https://pokeapi.co/api/v2/pokemon </br>

---

## Prática: chamada de API com biblioteca _requests_ do Python
Objetivos: consumir API do Pokemon com Python, fazer uma requisição http. 
```
  import requests

  def retorna_dados_pokemon(pokemon):  #define a funcao 
      response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))  #requisicao da API PokeApi
      dados_pokemon = response.json()  #converte resposta em bytes para formato de dicionario em Json
      return dados_pokemon  #retorna o resultado da funcao

  if __name__ == '__main__':
      dados_pokemon = retorna_dados_pokemon('pikachu')  #variavel recebe dados do Pikachu
      print(dados_pokemon['sprites']['front_shiny'])  #parametro do print é conteudo filtrado da variável dados_pokemon
      #retorna link da imagem do Pikachu

  # saida esperada: #https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png
  # fim do codigo
```

<p align="center"><img src="https://github.com/rosacarla/DIO-cloud-data-engineer/blob/main/006%20python/images/image%20pikachu.jpg" width="750"></p>

---

## Links úteis

Download [Python](https://www.python.org/downloads/) </br>
Download [IDE PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows) </br>
Estudar Python em [GeeksForGeeks](https://www.geeksforgeeks.org/python-programming-language/?ref=shm)
