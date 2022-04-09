# print('Numeros em intervalo até 100')
# for x in range(1, 100): #seleciona de 1 a 99
#     print(x)
#
# print('\nNumeros com resto e identifica nro primo')
# a = int(input('Entre com o nro: '))
# div = 0
# for x in range(1, a+1): #percorre todos nro até o do input
#     resto = a % x #armazena o resto
#     print(x, resto) #imprime nros até chegar no input e restos
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Numero {} é primo'.format(a))
# else:
#     print('Numero {} não é primo'.format(a))
#
# print('\nNumeros primos no intervalo fixado')
# a = int(input("Entre com um valor: "))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1): #laco identifica nros primos ate 100
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num) #imprime primos do intervalo até nro do input
#
# print('\nNumeros dentro do laço')
# a = 0
# while a <= 10:
#     print(a)
#     a += 1

print('Avalia notas')
nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota invalida. Entre com a nota correta: '))
print(nota)

e = int(input('Primeiro bimestre: '))
while e > 10:
    e = int(input('Voce digitou errado. Primeiro bimestre: '))
f = int(input('Segundo bimestre: '))
while f > 10:
    f = int(input('Voce digitou errado. Segundo bimestre: '))
g = int(input('Terceiro bimestre: '))
while g > 10:
    g = int(input('Voce digitou errado. Terceiro bimestre: '))
h = int(input('Quarto bimestre: '))
while h > 10:
    h = int(input('Voce digitou errado. Quarto bimestre: '))
media = (e + f + g + h) / 4
print('Media: {}'.format(media))