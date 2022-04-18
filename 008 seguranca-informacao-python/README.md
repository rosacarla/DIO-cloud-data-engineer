# Segurança da informação com Python

## Conteúdos do curso:

* Introdução aos conceitos de Segurança da Informação e Ping </br>
	Por que Python?  </br>
	O que é segurança da informação?  </br>
	O que é Ping?  </br>
* Introdução a Socket e cliente TCP/UDP e Server
	Biblioteca Socket  </br>
	Desenvolvimento de um cliente TCP  </br>
	Desenvolvimento de um cliente UD  </br>
	Desenvolvimento de um Server  </br>
* Desenvolvimento de Ferramentas - Parte 1
	O que é a bibllioteca Random, uma hash e Multithreading? </br>
	Desenvolvendo um gerador de senhas  </br>
	Desenvolvendo um comparador de Hashes  </br>
	Trabalhando com Threads e IP's  </br>
* Desenvolvimento de Ferramentas - Parte 2
	Desenvolvendo um gerador de Hashes  </br>
	Desenvolvendo um Web Scraping  </br>
	Desenvolvendo um Web Crawler  </br>
* Desenvolvimento de Ferramentas - Parte 3
	Desenvolvendo um verificador de telefone  </br>
	Desenvolvendo um ocultador de arquivos  </br>
	Desenvolvendo um verificador de Ip Externo  </br>
	Ferramenta Gráfica para abrir o navegador  </br>

---

## Prática: ferramenta gráfica OpenBrowserTool

Objetivo: desenvolver uma janela com botão para abrir o navegador Google. </br>
``` python
    import webbrowser
    from tkinter import *  #* indica que é para importar tudo da lib tkinter
    
    root = Tk( )  #variavel recebe screen name, representa a tela
    #espaço (como argumento) quer dizer que é none ou nao tem nome da tela

    root.title('Abrir Browser')  #titulo da ferramenta grafica
    root.geometry('300x200')  #tamanho da janela

    def google():  #define funcao google
        webbrowser.open('www.google.com')  #abre o google no navegador

    mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
    #botao tem comando que chama a funcao google; pack diz a posicao do botao
    root.mainloop()  #chama o sistema
```

<p align="center"> 
<img src="https://github.com/rosacarla/DIO-cloud-data-engineer/blob/main/008%20seguranca-informacao-python/images/045OpenBrowserTool.gif">
</p>

---

## Ferramentas utilizadas

Consultar IP: http://ipinfo.io/json </br>
Conversor Ezgif (vídeo para GIF): https://ezgif.com/video-to-gif </br>
Md5 Online Decrypt & Encrypt (hash md5): https://md5decrypt.net/en/ </br>
Screen Recorder & Video Editor Screencast-O-Matic: https://screencast-o-matic.com/ </br>
