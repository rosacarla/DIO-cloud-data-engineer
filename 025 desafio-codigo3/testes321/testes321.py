# TODO: Complete os espaços em branco com uma solução possível para o problema.
n = int(input("Quantos pares de números serao informados? "))
for i in range(n):
    x, y = input("Informe seus pares: ").split()
    teste = 0
    cont = 0
    if len(y) > len(x):
        print("nao encaixa")

    else:
        for j in range(len(y)):
            teste -= 1
            if x[teste] == y[teste]:
                cont += 1

        if cont == len(y):
            print("encaixa")

        else:
            print("nao encaixa")