#1) CALCULA MEDIA DE NOTAS
print('-' * 60)
a = float(input('Digite a 1a. nota (com até 1 casa decimal, use ponto no lugar da vírgula): '))
b = float(input('Digite a 2a. nota (com até 1 casa decimal, use ponto no lugar da vírgula): '))

#TODO Complete os espaços em branco com as respectivas variáveis para o cálculo da média.
media = (a * 3.5 + b * 7.5) / 11

#TODO Complete com a variável que representa o resultado da média.
print(f'MEDIA = {media: .5f}')
#EXEMPLO 1 DE SAÍDA
# Digite a primeira nota (com até 1 casa decimal, use ponto no lugar da virgula): 20.3
# Digite a segunda nota (com até 1 casa decimal, use ponto no lugar da virgula): 17.8
# MEDIA =  18.59545
#
# Process finished with exit code 0

#2) CALCULOS DE AREA E PERIMETRO
print('-' * 60)
lados = [float(x) for x in input("Informe as medidas dos 3 lados do triângulo: ").split()]

a = lados[0];
b = lados[1];
c = lados[2];

if a + b > c and a + c > b and b + c > a:
      print('-' * 60)
      #TODO Preencha a formula do perímetro do triangulo (soma de todos os lados).
      print(f"\nPerimetro = {sum(lados):.1f}")
else:
    #TODO PreenchA a formula da área do trapézio: AREA = ((A + B) x C) / 2
    print(f"\nArea = {(((a+b)*c)/2):.1f}")

#3) CONVERSAO DE TEMPO
print('-' * 60)
segundos = int(input('Informe a duração do evento em segundos para conversao em horas: '))

minutos = int(segundos/60) #TODO Implementar a formula para calcular os minutos.
segundos = int(segundos - (minutos * 60))
horas = int(minutos/60) #TODO Implementar a formula para calcular as horas.
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))
print('-' * 60)

#######################
# EXEMPLO 2 DE SAIDAS #
#######################
# ------------------------------------------------------------
# Digite a 1a. nota (com até 1 casa decimal, use ponto no lugar da vírgula): 3.9
# Digite a 2a. nota (com até 1 casa decimal, use ponto no lugar da vírgula): 8.2
# MEDIA =  6.83182
# ------------------------------------------------------------
# Informe as medidas dos 3 lados do triângulo: 5.0 7.5 3.5
# ------------------------------------------------------------
#
# Perimetro = 16.0
# ------------------------------------------------------------
# Informe a duração do evento em segundos para conversao em horas: 78654
# 21:50:54
# ------------------------------------------------------------
#
# Process finished with exit code 0