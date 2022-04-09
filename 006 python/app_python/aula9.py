import shutil #biblioteca para copiar arq com mesmo nome (nao poe nada) ou novo nome (inclui no fim do link)

# arquivo = open('teste.txt', 'w') #criar arq ou abrir arq existente
# #arquivo.write('Minha primeira escrita.') #w é para escrita (nova ou sobrescrita) no arquivo
# arquivo.write('Segunda linha.') #sobrescreveu no arquivo
# arquivo.close() #fecha abertura do arquivo

# arquivo = open('teste.txt', 'a') #pode criar arq e atualizar arq existente
# arquivo.write('\nTerceira linha.') #a é para autalizar sem sobrescrever
# arquivo.close()

def escrever_arquivo(texto): #criado metodo escrever
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto): #criado metodo atualizar
    arquivo = open(nome_arquivo, 'a') #nome_arquivo grava texto da variavel aluno (ver main abaixo)
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo): #criado metodo ler
    arquivo = open(nome_arquivo, 'r') #r é para leitura do arq
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo): #criado metodo calcula media de notas
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') #transforma string em lista com split (depois poderá acessá-los/manipulá-los)
    #print(aluno_nota)                   #split quebra a cada \n e cria itens da lista

    lista_media = [] #gera lista que conterá dicionario
    for x in aluno_nota:
        #print(x) #tinha item em branco ' ', eliminado ao deletar linha no arq notas.txt
        lista_notas = x.split(',') #novo split separa alunos e suas notas pelas virgulas
        #print(lista_notas) #imprime lista de strings
        aluno = lista_notas[0] #separa itens na posição 0
        lista_notas.pop(0) #gera lista sem itens em posicao 0
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4 #calcula media de notas convertidas em int
        print(media(lista_notas)) #imprime aluno, lista notas, media
        lista_media.append({aluno:media(lista_notas)}) #quando passar por aluno adiciona media em lista de dicionario
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/carla/Área de Trabalho/meu-github/dio-desafio-github-repositorio/006 python/notas_alunos.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'C:/Users/carla/Área de Trabalho/meu-github/dio-desafio-github-repositorio/006 python')
    #se colocasse novo nome junto ao link acima, ar seria movido com novo nome

if __name__ == '__main__':
    move_arquivo('notas.txt') #arq estava no diretorio app_python e foi para 006 python
    #copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media) #imprime lista do dicionario com aluno e sua media
    #escrever_arquivo('Primeira linha.\n')
    #aluno = 'Cesar, 7, 9, 3, 8\n' #texto para atualizar arq
    #atualizar_arquivo('notas.txt', aluno) #cria arquivo com notas
    #ler_arquivo('teste.txt')
    #acrescentada manualmente "Quarta linha." para nova leitura

def escrever_arquivo(texto): #met escrever cria arquivo em outro diretorio
    diretorio = 'C:/Users/carla/Área de Trabalho/meu-github/dio-desafio-github-repositorio/006 python/teste.txt'
    arquivo = open(diretorio, 'w') #para funcionar link do diretorio é preciso inverter a barra (de \ para /)
    arquivo.write(texto) #se não passar nenhum diretorio, arq é criado em mesmo diretorio de execução do arq.py
    arquivo.close()
#"C:\Users\carla\Área de Trabalho\meu-github\dio-desafio-github-repositorio\006 python"

if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')

