# #1) CALCULA MEDIA DE NOTAS
print('-' * 60)
a = float(input('Digite a primeira nota (com até 1 casa decimal, use ponto no lugar da virgula): '))
b = float(input('Digite a segunda nota (com até 1 casa decimal, use ponto no lugar da virgula): '))

#TODO: Complete os espaços em branco com as respectivas variáveis para o cálculo da média.
media = (a * 3.5 + b * 7.5) / 11

#TODO: Complete com a variável que representa o resultado da média.
print(f'MEDIA = {media: .5f}')
#EXEMPLO DE SAÍDA
# Digite a primeira nota (com até 1 casa decimal, use ponto no lugar da virgula): 20.3
# Digite a segunda nota (com até 1 casa decimal, use ponto no lugar da virgula): 17.8
# MEDIA =  18.59545
#
# Process finished with exit code 0

#2) CALCULOS DE AREA E PERIMETRO
# lados = [float(x) for x in input().split()]
#
# a = lados[0];
# b = lados[1];
# c = lados[2];
#
# if a + b > c and a + c > b and b + c > a:
      #print('-' * 60)
#     #Preencher a formula do perímeto do triangulo (soma de todos os lados).
#     print(f"\nPerimetro = {sum(lados):.1f}")
# else:
#     #Preencher a formula da área do trapézio: AREA = ((A + B) x C) / 2
#     print(f"\nArea = {(((a+b)*c)/2):.1f}")

#3) CONVERSAO DE TEMPO
print('-' * 60)
segundos = int(input('Informe a duração do evento em segundos para conversao em horas: '))

minutos = int(segundos/60) #TODO Implementar a formula para calcular os minutos.
segundos = int(segundos - (minutos * 60))
horas = int(minutos/60) #TODO Implementar a formula para calcular as horas.
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))