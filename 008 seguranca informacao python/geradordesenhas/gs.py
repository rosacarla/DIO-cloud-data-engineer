import random, string

#tamanho = 16  ##recebe tamanho da senha
tamanho = int(input('Digite o tamanho de senha que você deseja: ')) ##usuario informa o tamanho da senha

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;:/?'
##recebe estrutura da senha gerada (letras miusculas e minusculas + numeros + caracteres)

rnd = random.SystemRandom() ##SystemRandom chama classe os.random para gerar nros aleatorios
                            ##a partir de fontes fornecidas pelo SO
print(''.join(rnd.choice(chars) for i in range (tamanho))) ##gera senha forte e dificil de quebrar
##rnd.choice retorna lista com caracteres randomicos; pega cada caractere randomico gerado
##pelo chars, para cada i no range tamanho gera nova letra/nro/simbolo aleatorios até 16.