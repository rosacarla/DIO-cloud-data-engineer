# Databricks notebook source
# Path - dataset1
path_dataset1 = "/FileStore/tables/country_vaccinations.csv"

# Path - RDD
path_rdd = "/FileStore/tables/arquivo_rdd.txt"

# COMMAND ----------

# Leitura de Dataframe

## Opção 1
df1 = spark.read.format("csv").option("header","true").option("inferSchema","false").load(path_dataset1)

## Opção 2
# df1 = spark.read.csv(path_dataset1)
# df1 = spark.read.option("header","true").option("inferSchema","true").csv(path_dataset1)

## Exibindo dataframe
df1.show(2)
#df1.dtypes

# COMMAND ----------

df1.take(1)[0]

# COMMAND ----------

df1.write.format("parquet").mode("overwrite").save("/FileStore/tables/RAW_ZONE_PARQUET/")

# COMMAND ----------

df1.take(3)

# COMMAND ----------

## Outras formas de leitura de arquivos com PySpark

path = "/../../arquivoXPTO"

# Criando um dataframe a partir de um JSON
dataframe = spark.read.json(path)

# Criando um dataframe a partir de um ORC
dataframe = spark.read.orc(path)

# Criando um dataframe a partir de um PARQUET
dataframe = spark.read.parquet(path)

# COMMAND ----------

## Imprimindo tipos de campos

df1.dtypes
#df1.printSchema

# COMMAND ----------

# Leitura de um RDD

rdd = sc.textFile(path_rdd)
#rdd.show() = Errado, não é possível exibir um SHOW() de um RDD, somente um Dataframe
rdd.collect()

# COMMAND ----------

dfff = spark.read.format("csv").load(path_rdd)
display(dfff)

# COMMAND ----------

# Criando uma tabela temporária
nome_tabela_temporiaria = "tempTableTerere"
df1.createOrReplaceTempView(nome_tabela_temporiaria)

# COMMAND ----------

# Lendo a tabela temporaria opcao 1
spark.read.table(nome_tabela_temporiaria).show()

# COMMAND ----------

dfterere = spark.sql("SELECT count(*) tt, country FROM tempTableTerere Group By country")
dfterere.dtypes

# COMMAND ----------

# Visualização do Databricks
display(spark.sql("SELECT * FROM tempTableDataFrame1"))

# COMMAND ----------

# Scala
#import org.apache.spark.sql.functions._

# Python
from pyspark.sql.functions import col, column

# Usando function col ou column
df1.select(col("country"), col("date"), column("iso_code")).show()

# COMMAND ----------

df1.selectExpr("country", "date", "iso_code").show()

# COMMAND ----------

# Scala import
# org.apache.spark.sql.types._

# Criando um Schema manualmente no PySpark
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
# Scala

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

schema

# COMMAND ----------

# Gravando um novo CSV

path_destino="/FileStore/tables/CSV/"
nome_arquivo="arquivo.csv"
path_geral= path_destino + nome_arquivo
df1.write.format("csv").mode("overwrite").option("sep", "\t").save(path_geral)

# COMMAND ----------

# Gravando um novo JSON

path_destino="/FileStore/tables/JSON/"
nome_arquivo="arquivo.json"
path_geral= path_destino + nome_arquivo
df1.write.format("json").mode("overwrite").save(path_geral)

# COMMAND ----------

# Gravando um novo PARQUET

path_destino="/FileStore/tables/PARQUET/"
nome_arquivo="arquivo.parquet"
path_geral= path_destino + nome_arquivo
df1.write.format("parquet").mode("overwrite").save(path_geral)

# COMMAND ----------

# Gravando um novo ORC

path_destino="/FileStore/tables/ORC/"
nome_arquivo="arquivo.orc"
path_geral= path_destino + nome_arquivo
df1.write.format("orc").mode("overwrite").save(path_geral)

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

# Define uma nova coluna com um valor constante
df2 = df1.withColumn("nova_coluna", lit(1))
#display(df1)
#display(df2)

# Adicionar coluna
teste = expr("total_vaccinations < 40")
#df1.select("country", "total_vaccinations").withColumn("teste", teste).show(5)


# Renomear uma coluna
df1.select(expr("total_vaccinations as total_de_vacinados")).show(5)
df1.select(col("country").alias("pais")).show(5)
df1.select("country").withColumnRenamed("country", "pais").show(5)

# Remover uma coluna
df3 = df1.drop("country")
df3.columns


# COMMAND ----------

# Filtrando dados e ordenando
# where() é um alias para filter().

# Seleciona apenas os primeiros registros da coluna "total_vaccinations"
df1.filter(df1.total_vaccinations > 55).orderBy(df1.total_vaccinations).show(2)

# Filtra por país igual Argentina
df1.select(df1.total_vaccinations, df1.country).filter(df1.country == "Argentina").show(5)

# Filtra por país diferente Argentina
df1.select(df1.total_vaccinations, df1.country).where(df1.country != "Argentina").show(5) # python type

# Mostra valores únicos
df1.select("country").distinct().show()

# Especificando vários filtros em comando separados
filtro_vacinas = df1.total_vaccinations < 100
filtro_pais = df1.country.contains("Argentina")
df1.select(df1.total_vaccinations, df1.country, df1.vaccines).where(df1.vaccines.isin("Sputnik V", "Sinovac")).filter(filtro_vacinas).show(5)
df1.select(df1.total_vaccinations, df1.country, df1.vaccines).where(df1.vaccines.isin("Sputnik V", "Sinovac")).filter(filtro_vacinas).withColumn("filtro_pais", filtro_pais).show(5)



# COMMAND ----------

"""#######################################################################################################################
Convertendo dados
#######################################################################################################################"""

df5 = df1.withColumn("PAISSSSS", col("country").cast("string").alias("PAISSSSSSS"))
df5.select(df5.PAISSSSS).show(2)

"""#######################################################################################################################
Trabalhando com funções
#######################################################################################################################"""

# Usando funções
df1.select(upper(df1.country)).show(3)
df1.select(lower(df1.country)).show(4)

# COMMAND ----------

# Criando um dataframe genérico

d = [{'name': 'Alice', 'age': 1}]
df_A = spark.createDataFrame(d)
df_A.show()

# COMMAND ----------

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


rdd2 = [
{"nome":"Marco","PaisOrigem":"Brasil"},
{"nome":"Helena","PaisOrigem":"Brasil"},
{"nome":"Gabriel","PaisOrigem":"Brasil"},
{"nome":"Vasco","PaisOrigem":"Portugal"},
{"nome":"Medhi","PaisOrigem":"Marocco"}]

dff2 = spark.createDataFrame(rdd2)
dff2.show()

'''
join_type = "inner"

+------+-----+------+------+----------+
|  nome|idade|status|  nome|PaisOrigem|
+------+-----+------+------+----------+
| Vasco|   62|  true| Vasco|  Portugal|
| Marco|   33|  true| Marco|    Brasil|
|Helena|   30|  true|Helena|    Brasil|
+------+-----+------+------+----------+
'''

'''val join_type = "left_semi"

+------+-----+------+
|  nome|idade|status|
+------+-----+------+
| Vasco|   62|  true|
| Marco|   33|  true|
|Helena|   30|  true|
+------+-----+------+
'''

'''val join_type = "right_outer"

+------+-----+------+-------+----------+
|  nome|idade|status|   nome|PaisOrigem|
+------+-----+------+-------+----------+
| Vasco|   62|  true|  Vasco|  Portugal|
| Marco|   33|  true|  Marco|    Brasil|
|  null| null|  null|Gabriel|    Brasil|
|Helena|   30|  true| Helena|    Brasil|
|  null| null|  null|  Medhi|   Marocco|
+------+-----+------+-------+----------+
'''

'''val join_type = "left_outer"

+--------+-----+------+------+----------+
|    nome|idade|status|  nome|PaisOrigem|
+--------+-----+------+------+----------+
| Antonio|   33|  true|  null|      null|
|   Vasco|   62|  true| Vasco|  Portugal|
|   Marco|   33|  true| Marco|    Brasil|
| Pereira|   33|  true|  null|      null|
|  Carlos|   28|  true|  null|      null|
|Fernando|   35|  true|  null|      null|
| Candido|   75| false|  null|      null|
|  Helena|   30|  true|Helena|    Brasil|
|    Lisa|   26|  true|  null|      null|
+--------+-----+------+------+----------+
'''

'''join_type = "full_outer"

+--------+-----+------+-------+----------+
|    nome|idade|status|   nome|PaisOrigem|
+--------+-----+------+-------+----------+
| Antonio|   33|  true|   null|      null|
|   Vasco|   62|  true|  Vasco|  Portugal|
|   Marco|   33|  true|  Marco|    Brasil|
| Pereira|   33|  true|   null|      null|
|  Carlos|   28|  true|   null|      null|
|    null| null|  null|Gabriel|    Brasil|
|Fernando|   35|  true|   null|      null|
| Candido|   75| false|   null|      null|
|  Helena|   30|  true| Helena|    Brasil|
|    Lisa|   26|  true|   null|      null|
|    null| null|  null|  Medhi|   Marocco|
+--------+-----+------+-------+----------+
'''

'''join_type = "left_anti"

+--------+-----+------+
|    nome|idade|status|
+--------+-----+------+
| Antonio|   33|  true|
| Pereira|   33|  true|
|  Carlos|   28|  true|
|Fernando|   35|  true|
| Candido|   75| false|
|    Lisa|   26|  true|
+--------+-----+------+
'''

join_type = "inner"
join_condition = dff1.nome == dff2.nome
df3 = dff1.join(dff2, join_condition, join_type)
df3.show()

#df1.groupBy("status").agg(countDistinct(col("idade"))).show()

# COMMAND ----------

# Path - RDD
path_rdd = "/FileStore/tables/arquivo_rdd.txt"
rdd = sc.textFile(path_rdd)
df_pre = spark.read.text(path_rdd)

# COMMAND ----------

from pyspark.sql import functions as f
df_pre

# COMMAND ----------

x = lambda y : y + 1

# COMMAND ----------

x(2

# COMMAND ----------

## para TXT's com header
path_rdd = "/FileStore/tables/arquivo_rdd.txt" # especificar o caminho do Bucket
df_pre = spark.read.text(path_rdd)
posicao = ((0,1),(1,5), (5,8))
header= "nome;tipo;texto"
func = lambda p,name,df : df.withColumn(name, df['value'].substr(p[0], p[1]))
def concatenaCampo(posicao, header, df_): 
  i = 0
  header_ = header.split(";")
  for p in posicao:
    df_ = func(p,header_[i],df_)
    print(header_[i])
    i=i+1
  return df_.drop('value')

# COMMAND ----------

header.split(";")

# COMMAND ----------

df_pre.show()

# COMMAND ----------

dd = concatenaCampo(posicao, header, df_pre)

# COMMAND ----------

dd.show()
