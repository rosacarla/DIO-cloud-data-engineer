# Princípios de Pensamento Computacional com Python

<p align="center"><img src="https://github.com/rosacarla/DIO-cloud-data-engineer/blob/main/007%20pensamento-computacional-python/quatro-pilares.jpg" width="750"></p>

---

## Exemplo de abstração

A nota de alunos é uma abstração, obtida por um método qualquer que isola aspectos relevantes para chegar na informação pretendida. </br>
```python
# Código média geral de alunos
print('Hello World!\n')
nota_aluno1 = 7.0
nota_aluno2 = 5.0
soma_alunos = nota_aluno1 + nota_aluno2
qtd_alunos = 2
media = soma_alunos / qtd_alunos
print(media)

#fim do codigo
```
---

## Exemplo de decomposição

Dividir um problema maior em partes menores para resolvê-las e obter a resposta, como calcular o valor do salário líquido a receber no mês. </br>
```python
# Código salário líquido mensal
descontos = 300.00
salario_fixo = 1650.00
vendas_mes = 31
valor_comissao = 20.00
valor_total_vendas = vendas_mes * valor_comissao

valor_salario_liquido = (salario_fixo + valor_total_vendas) - descontos

print('O salario liquido é R$ %.2f.'%(valor_salario_liquido))

#fim do codigo
```

---

## Exemplo de pensamento algorítmico

Podemos resolver um problema de diferentes formas, como a decisão de dividir igualmente um valor para comprar 2 itens no supermercado. </br>
```python
# Código compra de 2 itens com R$ 20,00 
arroz_kg = 7.00
feijao_kg = 9.00
carne_kg = 35.00

if arroz_kg <= 10.00:
  print('Posso comprar arroz.')
else:
  print('Nao posso comprar arroz.')  

if feijao_kg <= 10.00:
  print('Posso comprar feijao.')
else:
  print('Nao posso comprar feijao.')  

if carne_kg <= 10.00:
  print('Posso comprar carne.')
else:
  print('Nao posso comprar carne.') 

#fim do codigo
```

---

## Exemplo de identificação de padrões

Reconhecer o padrão de estruturas reduz esforço na solução de problemas, como reescrever código anterior com estrutura de repetição. </br>
```python
# Código compra de 2 itens com R$ 20,00 - versao com loop for
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

# fim do codigo
```

---

## Ferramentas utilizadas

Interpretador online [Repl.it](https://replit.com/) </br>
IDE [PyCharm](https://www.jetbrains.com/pycharm/promo/)

---
