import ctypes
#ferramenta tem objetivo de proteger informacoes de uma pasta
pasta = input('Digite o caminho da pasta a ser ocultada, por ex., (C:/pasta): ')
#pode ocultar arquivos e diretorios
atributo_ocultar = 0x02 #recebe atributo em hexadecimal

#retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)
#chama lib windll que permite manipular o arquivo no SO para ocultar
retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)
#SetFileAttributesW configura os atributos do arquivo e reescreve
if retorno: #se houver retorno
    print('Arquivo foi ocultado.')
else: #caso contratrio
    print('Arquivo não foi ocultado.')