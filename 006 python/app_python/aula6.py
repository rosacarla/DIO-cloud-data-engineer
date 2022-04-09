print('Imprime elementos de um conjunto')
conjunto = {1, 2, 3, 4}
print(conjunto)
print('\nImprime conjunto alterado')
print('\nInclusao')
conjunto.add(5)
print(conjunto)
print('\nExclusao')
conjunto.discard(2)
print(conjunto)

print('\nImprime uniao de conjuntos')
conjunto1 = {1, 2, 3, 4, 5, 6}
print('\nConj1')
print(conjunto1)
conjunto2 = {6, 7, 8, 9, 10}
print('\nConj2')
print(conjunto2)
conjunto_uniao = conjunto1.union(conjunto2)
print('\nImprime uniao de conjuntos\n')
print('Uniao: {}'.format(conjunto_uniao))
print('\nImprime intersecçao de conjuntos')
conj_interseccao = conjunto1.intersection(conjunto2)
print('Interseccao: {}'.format(conj_interseccao))

print('\nDiferencas entre conjuntos')
conj_diferenca1 = conjunto1.difference(conjunto2)
print('Diferenca entre 1 e 2: {}'.format(conj_diferenca1))
conj_diferenca2 = conjunto2.difference(conjunto1)
print('Diferenca ente 2 e 1: {}'.format(conj_diferenca2))

print('\nDiferença simétrica entre conjuntos')
conj_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferenca simetrica: {}'.format(conj_diff_simetrica))

print('Metodo subset')
conj_a = {1, 2, 3}
conj_b = {1, 2, 3, 4, 5}
conj_subset = conj_a.issubset(conj_b)
print('Conj_a: ', conj_a)
print('Conj_b: ', conj_b)
print('A é subconjunto B: {}'.format(conj_subset))
conj_subset = conj_b.issubset(conj_a)
print('Subconjunto b de a? ', conj_subset)

conj_superset = conj_b.issuperset(conj_a)
print('B é superconjunto A: {}'.format(conj_superset)) #b é superset de a porque a é seu subset
conj_superset = conj_a.issuperset(conj_b)
print('Superconjunto a de b? ', conj_superset) #somente b tem todos os itens de a

print('Lista com dados repetidos para eliminar')
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conj_animais = set(lista)
print('\nConjunto de animais', conj_animais)
lista_animais = list(conj_animais)
print('\nLista de animais', lista_animais)
#maneira facil de atualizar lista é converte-la para conjunto
#essa conversao tem baixo custo computacional