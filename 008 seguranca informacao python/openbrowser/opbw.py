import webbrowser
from tkinter import * #* indica que é para importar tudo da lib tkinter

root = Tk( ) #variavel recebe screen name, representa a tela
#espaço (como argumento) quer dizer que é none ou nao tem nome da tela

root.title('Abrir Browser') #titulo da ferramenta grafica
root.geometry('300x200') #tamanho da janela

def google(): #abre o navegador no google
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
#botao tem comando que chama a funcao google; pack diz a posicao do botao
root.mainloop() #chama o sistema