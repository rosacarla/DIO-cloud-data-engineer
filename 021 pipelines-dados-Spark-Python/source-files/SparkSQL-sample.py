# Databricks notebook source
# Path - dataset1
path_dataset1 = "/FileStore/tables/country_vaccinations.csv"

# Path - RDD
path_rdd = "/FileStore/tables/arquivo_rdd-1.txt"

# COMMAND ----------

# Leitura de Dataframe

## Opção 1
df1 = spark.read.format("csv").option("header","true").load(path_dataset1)
 
## Exibindo dataframe com cabeçalho como 1a coluna, mostra log de informação
df1.show(2)

# COMMAND ----------

## Opção 2
df1 = spark.read.format("csv").option("header","false").load(path_dataset1)
 
## Exibindo dataframe sem cabeçalho e valores padrao na 1a coluna
df1.show(4)

# COMMAND ----------

## Opção 3 de leitura direta
df1 = spark.read.csv(path_dataset1)
 
## Exibindo dataframe com tipos de dados
df1.dtypes

# COMMAND ----------

# Opção 4 de leitura 
df1 = spark.read.option("header","true").option("inferSchema","true").csv(path_dataset1)

## Exibindo dataframe com col e tipos de dados
df1.dtypes

# COMMAND ----------

## Opção 5
df1 = spark.read.option("header","true").option("inferSchema","false").csv(path_dataset1)
 
## Exibindo dataframe todo como string para ingestao em raw zone
df1.dtypes

# COMMAND ----------

## Opção 6
df1 = spark.read.csv(path_dataset1)
df1 = spark.read.option("header","true").option("inferSchema","true").csv(path_dataset1)
 
## Exibindo colunas do dataframe 
df1.columns

# COMMAND ----------

#Opacao 7 de leitura com mudanca do delimitador csv
df1 = spark.read.option("header","true").option("delimiter", "|").option("inferSchema","true").csv(path_dataset1)

## Exibindo dataframe delimitado por |
df1.show(4)

# COMMAND ----------

#Cria objeto (lista do python) com linhas de log de informação para usar em logicas 
df1.take(1) #pode passar nro de linha como parametro

# COMMAND ----------

# Ingestao na raw zone de arq parquet
df1.write.format("parquet").save("/FileStore/tables/RAW_ZONE_PARQUET/")

#arq ficou dividido em 6 partes
# ==> deu erro na 2a execução porque já existia e não é refeito!!

# COMMAND ----------

# Fazer particionamento do arquivo parquet

df1.repartition(2).write.format("parquet").save("/FileStore/tables/RAW_ZONE_PARQUET/")

# COMMAND ----------

# CORRECAO: fazer particionamento do arquivo parquet

df1.repartition(2).write.format("parquet").mode("overwrite").save("/FileStore/tables/RAW_ZONE_PARQUET/")

# COMMAND ----------

### Outras formas de leitura de arquivos com PySpark
 
#path = "/../../arquivoXPTO"
 
## Criando um dataframe a partir de um JSON
#dataframe = spark.read.json(path)
 
## Criando um dataframe a partir de um ORC
#dataframe = spark.read.orc(path)
 
## Criando um dataframe a partir de um PARQUET
#dataframe = spark.read.parquet(path)

# COMMAND ----------

## Leitura de um RDD

rdd = sc.textFile(path_rdd)
#rdd.show() = Errado, não é possível exibir um SHOW() de um RDD, somente um Dataframe
rdd.collect()

# COMMAND ----------

## Tentativa de uso do comando show() com RDD
dfff = spark.read.format("csv").load(path_rdd)
dfff.show(4) 

# Exibe tab com única coluna

# COMMAND ----------

# Exibicao do RDD com recurso do databricks - display()
dff = spark.read.format("csv").load(path_rdd)
display(dff)

# COMMAND ----------

# Exibicao de dataframe com recurso do databricks - display()
dfff = spark.read.format("csv").load(path_dataset1)
display(dfff)

# COMMAND ----------

# Criacao de uma tabela temporária
nome_tabela_temporaria = "tempTableDataFrame1"
df1.createOrReplaceTempView(nome_tabela_temporaria)

# COMMAND ----------

# Leitura da tabela temporaria opcao 1
spark.read.table(nome_tabela_temporaria).show()

# COMMAND ----------

# Renomeada a tabela temporária
nome_tabela_temporaria = "tempTableTerere"
df1.createOrReplaceTempView(nome_tabela_temporaria)

# COMMAND ----------

# Leitura da tabela temporaria opcao 2
spark.read.table(nome_tabela_temporaria).show()

# COMMAND ----------

# Uso de SQL para mostrar tab
spark.sql("SELECT * FROM tempTableTerere").show()

# COMMAND ----------

#Mostrar somente colunas especificas da tab com comando SQL
spark.sql("SELECT country, iso_code FROM tempTableTerere").show()

# COMMAND ----------

#Mostrar agrupamento do total de registros contados por col país
spark.sql("SELECT count(*) tt, country FROM tempTableTerere Group By country").show()

# COMMAND ----------

#Exibe somente 3 registros ou linhas da selecao anterior
dfterere = spark.sql("SELECT count(*) tt, country FROM tempTableTerere Group By country")
dfterere.show(3) #criado dataframe novo

# COMMAND ----------

#Exibe tipos de dados do novo dataframe
dfterere = spark.sql("SELECT count(*) tt, country FROM tempTableTerere Group By country")
dfterere.dtypes

# COMMAND ----------

# Visualização do Databricks
display(spark.sql("SELECT * FROM tempTableDataFrame1"))

#Nao funciona na VM Everis

# COMMAND ----------

# Scala
#import org.apache.spark.sql.functions._
 
# Python - importa PySpark e funcoes col e column (sao identicas)
from pyspark.sql.functions import col, column
 
# Uso das functions col ou column
df1.select(col("country"), col("date"), column("iso_code")).show()

# COMMAND ----------

#Selecao de dados por strings que nomeiam col
df1.selectExpr("country", "date", "iso_code").show()

#Mesma saída da selecao anterior, sem usar functions col e column

# COMMAND ----------

# Scala import
# org.apache.spark.sql.types._
 
# Criacao de Schema manualmente no PySpark
from pyspark.sql.types import *
 
dataframe_ficticio = StructType([
                      StructField("col_String_1", StringType()),
                      StructField("col_Integer_2", IntegerType()),
                      StructField("col_Decimal_3", DecimalType())
                              ])
dataframe_ficticio

# COMMAND ----------

# Função para gerar Schema (campos/colunas/nomes de colunas)
 
'''
Scala
 
org.apache.spark.sql.types._
 
def getSchema(fields : Array[StructField]) : StructType = {
  new StructType(fields)
}
'''
 
# PySpark
def getSchema(fields):
  return StructType(fields)
  
schema = getSchema([StructField("coluna1", StringType()), StructField("coluna2", StringType()), StructField("coluna3", StringType())]) 

# COMMAND ----------

#Mostra  lista do schema
schema

# COMMAND ----------

df1.source_website

# COMMAND ----------

# Gravando um novo CSV
 
#path_destino="/FileStore/tables/CSV/"
#nome_arquivo="arquivo.csv"
#path_geral= path_destino + nome_arquivo
#df1.write.format("csv").mode("overwrite").option("sep", "\t").save(path_geral)

# COMMAND ----------

# Gravando um novo JSON
 
#path_destino="/FileStore/tables/JSON/"
#nome_arquivo="arquivo.json"
#path_geral= path_destino + nome_arquivo
#df1.write.format("json").mode("overwrite").save(path_geral)

# COMMAND ----------

# Gravando um novo PARQUET
 
#path_destino="/FileStore/tables/PARQUET/"
#nome_arquivo="arquivo.parquet"
#path_geral= path_destino + nome_arquivo
#df1.write.format("parquet").mode("overwrite").save(path_geral)

# COMMAND ----------

# Gravando um novo ORC
 
#path_destino="/FileStore/tables/ORC/"
#nome_arquivo="arquivo.orc"
#path_geral= path_destino + nome_arquivo
#df1.write.format("orc").mode("overwrite").save(path_geral)

# COMMAND ----------

# Outros tipos de SELECT
 
#Diferentes formas de selecionar uma coluna
 
from pyspark.sql.functions import *
 
df1.select("country").show(5)
df1.select('country').show(5)
df1.select(col("country")).show(5)
df1.select(column("country")).show(5)
df1.select(expr("country")).show(5)

# COMMAND ----------

#Mostrar col do df1 para comparar abaixo com df2
df1.columns

# COMMAND ----------

# Define nova coluna com um valor constante
df2 = df1.withColumn("nova_coluna", lit(1))
display(df2)

# COMMAND ----------

# Adicionar coluna
teste = expr("total_vaccinations < 40")
df1.select("country", "total_vaccinations").withColumn("teste", teste).show(10)

#Traz valor booleano na col teste (true ou false) para responder a condição

# COMMAND ----------

# Renomear uma coluna
df1.select(expr("total_vaccinations as total_de_vacinados")).show(5)
df1.select(col("country").alias("pais")).show(5)
df1.select("country").withColumnRenamed("country", "pais").show(5)

# COMMAND ----------

# Remover uma coluna
df3 = df1.drop("country")
df3.columns

# COMMAND ----------

# Filtrando dados e ordenando
# where() é um alias para filter(), usado em condicoes.
 
# Seleciona apenas os primeiros registros da coluna "total_vaccinations"
df1.filter(df1.total_vaccinations > 55).orderBy(df1.total_vaccinations).show(2)

# COMMAND ----------

# Filtra por país igual Argentina com data
df1.select(df1.total_vaccinations, df1.date, df1.country).filter(df1.country == "Argentina").show(24)

# COMMAND ----------

# Filtra por país igual Brasil com data
df1.select(df1.total_vaccinations, df1.date, df1.country).filter(df1.country == "Brazil").show(5)

# COMMAND ----------

# Filtra por país diferente Argentina
df1.select(df1.total_vaccinations, df1.country).where(df1.country != "Argentina").show(5) # python type

# COMMAND ----------

# Mostra valores únicos
df1.select("country").distinct().show()

# COMMAND ----------

# Especificando vários filtros em comando separados
filtro_vacinas = df1.total_vaccinations < 100
filtro_pais = df1.country.contains("Argentina")
df1.select(df1.total_vaccinations, df1.country, df1.vaccines).where(df1.vaccines.isin("Sputnik V", "Sinovac")).filter(filtro_vacinas).show(5)
df1.select(df1.total_vaccinations, df1.country, df1.vaccines).where(df1.vaccines.isin("Sputnik V", "Sinovac")).filter(filtro_vacinas).withColumn("filtro_pais", filtro_pais).show(5)

#Nao entendi por que não mostra nada

# COMMAND ----------

"""#######################################################################################################################
Convertendo dados
#######################################################################################################################"""
 
df5 = df1.withColumn("PAISSSSS", col("country").cast("string").alias("PAISSSSSSS"))
df5.select(df5.PAISSSSS).show(2)

# COMMAND ----------

"""#######################################################################################################################
Trabalhando com funções
#######################################################################################################################"""
 
# Usando funções
df1.select(upper(df1.country)).show(3)
df1.select(lower(df1.country)).show(4)

# COMMAND ----------

# Criando um dataframe genérico
 ## Usa dicionario do Python com chave-valor
d = [{'name': 'Alice', 'age': 1}]
df_A = spark.createDataFrame(d)
df_A.show()

# COMMAND ----------

#Criação de dataframe rdd1
rdd1 = [{"nome": "Marco","idade": 33,"status": 'true'},
{"nome": "Antonio","idade":33,"status": 'true'},
{"nome":"Pereira","idade":33,"status": 'true'},
{"nome":"Helena","idade":30,"status": 'true'},
{"nome":"Fernando","idade":35,"status": 'true'},
{"nome":"Carlos","idade":28,"status": 'true'},
{"nome":"Lisa","idade":26,"status": 'true'},
{"nome":"Candido","idade":75,"status": 'false'},
{"nome":"Vasco","idade":62,"status": 'true'}
]
dff1 = spark.createDataFrame(rdd1)
dff1.show()

# COMMAND ----------

#Criação de dataframe rdd2
rdd2 = [
{"nome":"Marco","PaisOrigem":"Brasil"},
{"nome":"Helena","PaisOrigem":"Brasil"},
{"nome":"Gabriel","PaisOrigem":"Brasil"},
{"nome":"Vasco","PaisOrigem":"Portugal"},
{"nome":"Medhi","PaisOrigem":"Marocco"}]
 
dff2 = spark.createDataFrame(rdd2)
dff2.show()

# COMMAND ----------

#Uso do join nos 2 dataframes para exibir onde nomes sao iguais
join_type = "inner" #mostra tudo que existe
join_condition = dff1.nome == dff2.nome
df3 = dff1.join(dff2, join_condition, join_type)
df3.show() 

# COMMAND ----------

#Junta df da esquerda
join_type = "left_semi"
join_condition = dff1.nome == dff2.nome
df3 = dff1.join(dff2, join_condition, join_type)
df3.show()

# COMMAND ----------

#Junta df da direita e exibe o que não esta na dir
join_type = "right_outer"
join_condition = dff1.nome == dff2.nome
df3 = dff1.join(dff2, join_condition, join_type)
df3.show()

# COMMAND ----------

#Junta df da esquerda e exibe o que nao esta na esq
join_type = "left_outer"
join_condition = dff1.nome == dff2.nome
df3 = dff1.join(dff2, join_condition, join_type)
df3.show()

# COMMAND ----------

#Junta todos os lados
join_type = "full_outer"
join_condition = dff1.nome == dff2.nome
df3 = dff1.join(dff2, join_condition, join_type)
df3.show()

# COMMAND ----------

#Junta tudo que nao tem nos 2 df
join_type = "left_anti"
join_condition = dff1.nome == dff2.nome
df3 = dff1.join(dff2, join_condition, join_type)
df3.show()
