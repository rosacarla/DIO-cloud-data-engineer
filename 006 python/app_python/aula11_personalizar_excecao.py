class Error(Exception): #criar classe personalizada
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True: #laco de repeticao enquanto for verdade
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break  # #msg personalizada para erro de entrada; impressa como as mensagens de sistema
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas núneros.')
    except InputError as ex: #tratamento da excecao, por isso nao aparece msg formato sistema
        print(ex)