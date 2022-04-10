import itertools #possibilita iteracoes como permutação e combinação
#objetivo é gerar lista com caracteres diferentes sem repetir palavras

string = input('String a ser permutada: ')
#resultado = itertools.permutations('abc', 3) #metodo permutations fará 3 permutações nos caracteres "abc"
#resultado = itertools.permutations('abcdef', 3) #quanto mais caracteres e iterações, maior será a wordlist
#resultado = itertools.permutations('abcdefghi', 5)
resultado = itertools.permutations(string,len(string)) #permutacao da str do input com tamanho igual ao dela
for i in resultado:
    print(''.join(i)) #imprime caracteres permutados e junta 3 em cada iteração