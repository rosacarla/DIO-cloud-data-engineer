import hashlib

string = input("Digite o texto para ser gerado o hash: ")

#resultado = hashlib.md5(b'Python Security') #b antes do texto converte str em bytes
#print('O hash da string é: ', resultado.hexdigest()) #hex... converte variavel em hexadecimal

menu = int(input('''### MENU - ESCOLHA O TIPO DE HASH ###  
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: ''')) #menu para usuario escolher tipo de hash

if menu  == 1:
    resultado = hashlib.md5(string.encode('utf-8')) #resultado impresso como hash MD5
    print('A hash MD5 da string: ', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))  # resultado impresso como SHA1
    print('A hash SHA1 da string: ', string, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))  # resultado impresso como SHA256
    print('A hash SHA256 da string: ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))  # resultado impresso como SAH512
    print('A hash SHA512 da string: ', string, 'é: ', resultado.hexdigest())
else:
    print('Algo de errado não deu certo, tente novamente.') #msg de erro