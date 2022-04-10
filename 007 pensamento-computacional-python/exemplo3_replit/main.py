descontos = 300.00
salario_fixo = 1650.00
vendas_mes = 31
valor_comissao = 20.00
valor_total_vendas = vendas_mes * valor_comissao

valor_salario_liquido = (salario_fixo + valor_total_vendas) - descontos

print('O salario liquido é R$ %.2f.'%(valor_salario_liquido))