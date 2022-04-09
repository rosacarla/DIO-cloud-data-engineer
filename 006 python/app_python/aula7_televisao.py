class Televisao: #classe Televisao, conceito de orientacao a objetos

    def __init__(self):
        self.ligada = False #instanciada variavel ligada
        self.canal = 5 #instanciada variavel canal

    def power(self): #definicao de metodo
        if self.ligada: #avalia se é True e entra nesta condicoa
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1  # incrementa canais

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1 #decremento de canais

print(__name__)
if __name__ == '__main__': #codigo só roda quando mesmo arq chama
    televisao = Televisao()
    print('Televisao está ligada? {}'.format(televisao.ligada))
    televisao.power() #ligar a TV
    print('Televisao está ligada? {}'.format(televisao.ligada))
    televisao.power() #desligar a TV
    print('Televisao está ligada? {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisao está ligada? {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))