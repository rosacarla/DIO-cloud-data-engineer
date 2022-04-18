#VALORES POSITIVOS
counter = 0
for i in range(6):
    i = float(input('Informe um numero: '))
    if i > 0:
        counter = counter + 1

print("{} valores positivos".format(counter))


#CRESCENTE E DESCRESCENTE
# X, Y = map(int, input().split())
# while (X != Y):
#     floor = min(X, Y)
#     top = max(X, Y)
#     if (X < Y):
#         print("Crescente")
#     elif (X > Y):
#         print("Decrescente")
#     X, Y = map(int, input().split())


# #RESTO DA DIVISAO
X = int(input('Informe o primeiro numero: '))
Y = int(input('Informe o segundo numero: '))

while (X <= 7 and Y <= 8):
    print('error')
    break
if (Y > X):
    for i in range(X + 1, Y):
        if (i % 5 == 2) or (i % 5 == 3):
            print(i)
elif (X > Y):
    for i in range(Y + 1, X):
        if (i % 5 == 2) or (i % 5 == 3):
            print(i)