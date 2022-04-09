print('Imprime tupla')
tupla = (1, 10, 12, 14)
#tupla[0] = 12  #ocorre erro porque não se altera uma tupla
print(len(tupla)) #retorna qtde de itens da tupla

lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'ariranha']

print('\nImprime lista de animal atualizada')
lista_animal[0] = 'macaco'
print(lista_animal)
print('\nImprime qtde de elementos da lista_animal')
print(len(lista_animal))

print('\nConversao de lista[] em tupla()')
tupla_animal = tuple(lista_animal) #pode converter tupla em lista para alterar
print(type(tupla_animal)) #tuplas atendem necessidade de manter itens inalterados
print(tupla_animal)

print('\nConversao de tupla() em lista[]')
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

print('\nAlteracao de item da lista_numerica')
lista_numerica[0] = 100
print(lista_numerica)

# print('Imprime listas')
# lista = [1, 3, 5, 7]
# lista_animais = ['cachorro', 'gato', 'elefante']
# print(lista)
# print(lista_animais)
# print('\nImprime elemento em posicao 1 da lista')
# print(lista_animais[1])
#
# print('\nImprime todos os elementos da lista')
# for x in lista_animais:
#     print(x)
#
# print('\nImprime elementos e soma da lista')
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma) #imprime lista e a soma dos nros
# print('\nImprime soma de nros da lista')
# print(sum(lista))
# print('\nImprime maior nro da lista')
# print(max(lista))
# print('\nImprime menor nro da lista')
# print(min(lista))
# print('\nImprime menor string da lista')
# print(min(lista_animais)) #considera a ordem alfabetica
# print('\nImprime maior string da lista')
# print(max(lista_animais))
#
# print('\nConfere se um elemento consta na lista')
# if 'gato' in lista_animais:
#     print('Existe um gato na lista.')
# else:
#     print('Nao existe um gato na lista.')
# if 'lobo' in lista_animais:
#     print('\nExiste um lobo na lista.')
# else:
#     print('\nNao existe um lobo na lista.')
#     lista_animais.append('lobo') #append é metodo de inclusao
#     print('\nLista de animais atualizada\n', lista_animais)
#     print('\nExclusao de item da lista de animais')
#     lista_animais.pop(0) #indica a posicao a ser excluida
#     print(lista_animais) #pop() remove ultimo ou posicao citada
#     print('\nSegunda exclusao da lista de animais')
#     lista_animais.remove('elefante') #usado com elemento conhecido
#     print(lista_animais)
#
# print("\nImprime lista multiplicada")
# nova_lista = lista_animais * 3
# print(nova_lista)
#
# print('\nImprime listas ordenadas')
# lista = [12, 10, 7, 5]
# lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
# lista_animais.reverse()
# print(lista_animais)