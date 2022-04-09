arroz_kg = 7.00
feijao_kg = 9.00
carne_kg = 35.00

for i in range(3):
  valor = input('Informe valor do produto: R$ ')
  valor = float(valor)
  if valor <= 10.00:
    print('Posso comprar.')
else:
  print('Nao posso comprar.')  