import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url) #abre a url e joga dados para resposta

dados = json.load(resposta) #carrega o javascript da requisicao da resposta

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print('IP: {4}\nRegião: {1}\nPaís: {2}\nCidade: {3}\nOrg.: {0}'.format(org, regiao, pais, cid, ip))
#tomar cuidado ao executar porque traz informacoes sigilosas que possibilitam localizar o pc na rede
#copia da tela de execucao (arquivo 042) teve dados modificados para manter a privacidade