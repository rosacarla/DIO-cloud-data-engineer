import requests #nao reconhece e nao importa
#mensagem: ModuleNotFoundError: No module named 'requests'

response = requests.get('https://viacep.com.br/ws/{}/json/'.format('04094000')) #cep 04094000 Parque do Ibirapuera
print(response.status_code)
print(response.text)  # imprime conteudo do json
print(type(response.text))  # mostra <class 'str'>.
print(response.json())  # imprime dicionario json
print(type(response.json()))  # mostra <class 'dict>
dados_cep = response.json()
print(dados_cep['logradouro'])
print(dados_cep['complemento']) #nao tem complemento