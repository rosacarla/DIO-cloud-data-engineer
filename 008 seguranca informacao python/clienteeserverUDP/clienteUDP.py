import socket ##importar a lib socket
##deve rodar primeiro o programa do servidor

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##criado obje de conexao s; usa IPV4 e UDP

print('Cliente socket criado com sucesso!!!')

host = 'localhost'  ##localhost é rede local ou interna da maquina
porta = 5433 ##porta do cliente para conectar ao servidor
mensagem = 'Olá servidor, firmeza?'

try: ##tentativa de enviar e receber msg
    print('Cliente: ' + mensagem) ##empacota msg para enviar ao host e porta 5432 de onde serv ouve
    s.sendto(mensagem.encode(), (host, 5432)) ##encode empacota msg e envia com pacotes UDP ao servidor

    dados, servidor = s.recvfrom(4096) ##variaveis dados e servidor recebem resposta do servidor
    ##recebe msg de 4096 bytes do servidor
    dados = dados.decode() ##desempacota msg
    print('Cliente: ' + dados) ##imprime dados desempacotados
finally: ##fechamento de conexao
    print('Cliente: Fechando a conexão.') ##mensagem antes de fechar
    s.close() ##fecha pra evitar loop infinito
##é feito signAC (sincronização, reconhecimento, finaliza a conexao)