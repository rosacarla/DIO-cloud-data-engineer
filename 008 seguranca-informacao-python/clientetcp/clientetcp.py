import socket  ##fazer relacionamento entre placa de rede e SO
import sys  ##fornece acesso a variaveis e funcoes que tem
##relacao com o interpretador py

def main ():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #objeto de conexao
        ##obj s pega na biblio socket o metodo socket (familia de prot, tipo, prot)
        ##AF_INTET= inf uso de prot IP, SOCK_STREAM= inf uso de TCP, 0= prot TCP)
    except socket.error as e: ##condicao para existencia de erro
        print('A conexão falhou!!!') ##imprime msg sobre ocorrência de erro
        print('Erro: {}'.format(e)) ##imrpime msg descritiva do erro
        sys.exit() ##fecha e sai do programa

    print('Socket criado com sucesso.')

    HostAlvo = input('Digite o Host ou Ip a ser conectado: ') #variavel é str
    PortAlvo = input('Digite a porta a ser conectada: ') #variavel é str
    ##usuario deve digitar um host IP e uma porta TCP para conectar

    try:
        s.connect((HostAlvo, int(PortAlvo))) ##pede address; str PortAlvo é transformada em int porque...
                                             ##a porta não aceita str
        print('Cliente TCP conectado com sucesso no Host: ' + HostAlvo + 'e na Porta: ' + PortAlvo + '.')
        s.shutdown(2) ##desliga conexao apos espera de 2s para não ficar em loop infinito
    except socket.error as e:
        print('Não foi possivel conectar no Host: ' + HostAlvo + '- Porta: ' + PortAlvo + '.')
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == '__main__':
        main()