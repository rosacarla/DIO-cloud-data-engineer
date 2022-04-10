import hashlib ##requer criaçao de 2 arquivos para comparaçao

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160') ##define algoritmo usado por hash1

hash1.update(open(arquivo1, 'rb').read()) ##hash fará comparacao, abrindo arq em modo binario (rb)

hash2 = hashlib.new('ripemd160') ##define algoritmo usado por hash2

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest(): ##digest resume dados passado pelo update
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}.')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest(),'.') ##resume hash em hexadecimal para mostrar
    print('O hash do arquivo b.txt é: ', hash2.hexdigest(),'.')
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}.')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest(),'.')
    print('O hash do arquivo b.txt é: ', hash2.hexdigest(),'.')