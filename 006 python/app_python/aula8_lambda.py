contador_letras = lambda lista: [len(x) for x in lista]
#definida a variavel contador_letras (acima)
#fç anonima ficou dentro da variavel

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(5, 10))
print(subtracao(10, 5))

#criar calculadora com lambda; cria-se dicionario que simula uma classe
calculadora = { #tem-se conjunto de fçs analiticas em mesmo lugar
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
print('\n')
soma = calculadora['soma']
#soma = lambda a, b: a + b (mesma coisa da linha acima)
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('\n')
print('A multiplicacao é: {}'.format(multiplicacao(10, 2)))
