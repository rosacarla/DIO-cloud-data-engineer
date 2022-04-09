import ipaddress #biblioteca nativa do python

ip = '192.168.0.1' #lib ipaddress transforma str em um IP

endereco = ipaddress.ip_address(ip) #recebe da lib ipaddress o IP da var transformada

print(endereco)
print('-' * 60)
print(endereco + 100) #é possivel fazer calculos com IP
print(endereco + 257)
print(endereco + 256)
print(endereco + 2000)
print('-' * 60)

ip = '192.168.0.0/24' ##rede 0/24 tem 255 IPs
#ip = '192.168.0.100/24' #100 não seria reconhecido como rede sem o strict false

rede = ipaddress.ip_network(ip, strict=False) ##strict false permite inserir qualquer nro para a rede

print(rede) #para rede .100/24 imprime IP com final "0/24"
print('-' * 60)

for ip in rede: #loop para imprimir todos os IPs da rede
    print(ip)