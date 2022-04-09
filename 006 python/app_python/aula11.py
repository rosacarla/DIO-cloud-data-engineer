# try:
#     divisao = 10 / 0 #erro 1 forçado para tratar excecao
# except ZeroDivisionError: #tratamento da excecao 1
#     print('Não é possível realizar uma divisão por 0.')

lista = [1, 10]
try:
    divisao = 10 / 1 #erro 2 forçado para tratar encadamento de excecoes
    numero = lista[1] #para IndexError, variavel recebeu indice 3
    x = a
except ZeroDivisionError: #tratamento da excecao 1
    print('Não é possível realizar uma divisão por 0.')
#except: #tratamento de erro genérico ou para qualquer tipo de erro
#    print('Erro desconhecido.')
except IndexError: #tratamento da excecao 2
    print('Erro ao acessar um indice invalido da lista.')
except BaseException as ex: #tratmento da excecao 3; BaseException é o pai de todos os erros
    print('Erro desconhecido. Erro: {}'.format(ex)) #imprime msg de erro do BaseException
    #BaseException pode tratar excecoes não previstas sem necessidade de parar o codigo por causa do erro

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0 #erro 1 forçado para tratar excecao
    numero = lista[1]

except ZeroDivisionError: #tratamento da excecao, colocar no topo os filhos da lista de excecoes
    print('Não é possível realizar uma divisão por 0.')
except ArithmeticError: #excecao que agrupa o erro ZeroDivisionError
    print('Houve um erro ao realizar uma operação aritmética.')
except IndexError: #tratamento da excecao
    print('Erro ao acessar um indice invalido da lista.')
    #exception hierarchy: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
except BaseException as ex: #tratamento da excecao com alteracao da árvore de excecoes; pode usar apenas Exception
    print('Erro desconhecido. Erro: {}'.format(ex)) #vai executar e parar com impressao do erro do BaseExc...
    #BaseException é o ultimo porque pega todas as excecoes, nao avança para as demais do codigo
finally: #colocar o que sempre deve ser executado
    print('Sempre executa.\nFechando arquivo.')
    arquivo.close()

try: #trecho de codigo que depende da inexistencia de erro no bloco do try
    divisao = 10 / 1 #erro forçado para tratar excecao com else, se mudar para div 0 tem-se excecao e nao executa else
    numero = lista[1]

except IndexError: #tratamento da excecao
    print('Erro ao acessar um indice invalido da lista.')
except Exception as ex: #tratamento da excecao pode ser apenas com Exception (BaseException)
    print('Erro desconhecido. Erro: {}'.format(ex))
else: #executa mais codigo se não ha excecao
    print('Executa quando não ocorre exceção.')