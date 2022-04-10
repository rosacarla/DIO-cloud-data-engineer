import os #importa modulo o bliblioteca os (integra programas e
#recursos do SO. Inicialmente fica cinza porque lib não foi usada

print('#' * 60) #imprime # 60x
ip_ou_host = input('Digite o IP ou host a ser verificado: ')
#criada variavel que recebera do usuario um IP
print("-" * 60) #imprime - 60x
os.system('ping -n 6 {}'.format(ip_ou_host)) #chama metodo system da biblioteca OS
#chama tambem comando ping que tera nro de pacotes (-n = 6)
print("-" * 60) ##imprime - 60x
