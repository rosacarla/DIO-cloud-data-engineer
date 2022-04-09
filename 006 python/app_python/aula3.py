e = int(input('Primeiro bimestre: '))
if e > 10:
    e = int(input('Voce digitou errado. Primeiro bimestre: '))
f = int(input('Segundo bimestre: '))
if f > 10:
    f = int(input('Voce digitou errado. Segundo bimestre: '))
g = int(input('Terceiro bimestre: '))
if g > 10:
    g = int(input('Voce digitou errado. Terceiro bimestre: '))
h = int(input('Quarto bimestre: '))
if h > 10:
    h = int(input('Voce digitou errado. Quarto bimestre: '))
media = (e + f + g + h) / 4
print('Media: {}'.format(media))

#if e <= 10 and f <= 10 and g <= 10 and h <= 10:
#    print('Media: {}'.format(media))
#else:
#    print('Foi informada alguma nota errada.')

#a = int(input('Primeiro valor: '))
#b = int(input('Segundo valor: '))
#c = int(input('Terceiro valor: '))

#if a > b and a > c:
#    print('O maior numero é {}'.format(a))
#elif b > a and b > c:
#    print('O maior numero é {}'.format(b))
#else:
#    print('O maior numero é {}'.format(c))
#print('Final do programa.')

#c = int(input('Entre com o primeiro valor: '))
#d = int(input('Entre com o segundo valor: '))
#resto_c = c % 2
#resto_d = d % 2

#if resto_c == 0 or not resto_d > 0: #operador not inverte condicao (se for mentira)1
#    print('Foi digitado um nro par.')
#else:
#    print('Nenhum nro par foi digitado.')