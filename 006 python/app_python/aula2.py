a = 10
b = 4
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
soma = str(soma)
print(type (soma))
print('soma: ' + str(soma))
print('subtracao: ' + str(subtracao))
print('multiplicacao: ' + str(multiplicacao))
print('divisao: ' + str(divisao))
print(int(divisao))
print('resto: ' + str(resto))
x = '1'
soma2 = int(x) + 1
print(soma2)

#exemeplo de interacao com usuario
c = int(input('Entre com o primeiro valor: '))
d = int(input('Entre com o segundo valor: '))
print(type(a))
soma = c + d
subtracao = c - d
multiplicacao = c * d
divisao = c / d
resto = c % d

resultado = ('Soma: {soma} \nSubtracao: {subtracao}'
      '\nMultiplicacao: {multiplicacao} '
      '\nDivisao: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto)) #concatenacao independe do tipo de variavel
print(resultado)