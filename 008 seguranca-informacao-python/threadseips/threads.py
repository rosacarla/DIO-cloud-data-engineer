from threading import Thread  ##do modulo threading importa classe Thread
import time

#def carro1(velocidade):
def carro(velocidade, piloto):
    trajeto = 0 ##começa no marco 0
    while trajeto <= 100: ##loop até velocidade 100
        #print('Carro1: ', trajeto) ##imprime carro e a velocidade
        trajeto += velocidade ##incremento para contagem da velocidade
        time.sleep(0.5) ##espera 0.5 seg para imprimir o outro carro
        print('Piloto: {} km: {} \n'.format(piloto, trajeto))

# def carro2(velocidade):
#     trajeto = 0 ##começa em velocidade 0
#     while trajeto <= 100: ##loop até velocidade 100
#         print('Carro2: ', trajeto) ##imprime carro e a velocidade
#         trajeto += velocidade ##incremento para contagem da velocidade

#carro1(10) usado antes de criar a classe Thread
#carro2(20) execucao sequencial dos trajetos, nao foi simultanea
_carro1 = Thread(target=carro, args=[1, 'Bruno'])
_carro2 = Thread(target=carro, args=[1.5, 'Python'])

_carro1.start()
_carro2.start()