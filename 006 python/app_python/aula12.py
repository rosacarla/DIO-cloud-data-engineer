import requests

def retorna_dados_cep(cep): #request da API Viacep
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)) #cep 22041001 Av Atlântica, de 2174 a 2634 lado par
    print(response.status_code) #retorna codigo de sucesso
    print(response.text) #imprime conteudo do json
    print(type(response.text)) #mostra <class 'str'>.
    print(response.json()) #imprime dicionario json
    print(type(response.json())) #mostra <class 'dict>
    dados_cep = response.json() #primeiro mostrou cep 01001000 Praça da Sé - lado impar
    print(dados_cep ['logradouro'])
    print(dados_cep ['complemento'])

def retorna_dados_pokemon(pokemon): #request da API Pokemon
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url): #request de um site
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://globallabs.academy/')
    print(response) #retorna codigo html da página
    #retorna_dados_cep('22041001')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny']) #retorna link da imagem do pokemon
    #https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png