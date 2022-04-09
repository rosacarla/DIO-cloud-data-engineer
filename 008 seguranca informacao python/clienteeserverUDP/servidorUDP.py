import socket ##importa lib socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##criado obj de conexao

print('Socket criado com sucesso.') ##se der certo criação do obj, imprime msg

host = 'localhost' ##variavel armazena o host
port = 5432 ##variavel armazena a porta

s.bind((host, port)) ##bind faz ligacao entre cliente e servidor atraves do host e port
mensagem = '\nServidor: Olá cliente e aí, beleza?' ##\n para pular uma linha antes da msg do servidor

while 1: ##enquanto for verdadeiro (1)
    dados, end = s.recvfrom(4096) ##recebe 4096 bytes atraves do obj de conexao, guarda em dados e endereco

    if dados: ##condicao se dados tiver algo
        print('Servidor enviando mensagem...') ##imprime msg enquanto processa
        s.sendto(dados + (mensagem.encode()), end) ##Resumo: enviam-se e recebem-se dados via pacotes UDP