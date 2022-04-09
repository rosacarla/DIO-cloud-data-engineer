#ferramenta pingmultiplo percorrera um arquivo txt para verificar
#os hosts que deve varrer ou serem pingados

import os  ##importa biblioteca os e suas dependencias
import time ##importa biblioteca time, fixar tempo de execucao do ping

with open('hosts.txt') as file: ##abre o arquivo txt
    dump = file.read() ##recebe a leitura do arq txt
    dump = dump.splitlines() ##coloca dump em linhas separadas

    for ip in dump: ##percorre arquivo hosts.txt para procurar ips
        print('Verificando o IP: ', ip) #imprime casa ip do arquivo
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip)) #personalizacao do comendo para menos tempo de ping
        print('-' * 60)
        time.sleep(5) #intervalo de 5 seg na execucao de comandos das requisicoes
        #os.system('ping ' + ip)
        #print(ip) ##imprime ips do arquivo txt