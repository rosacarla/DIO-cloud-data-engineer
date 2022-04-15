# Databricks notebook source
# Criar um Spark Session com suporte a Hive:
# PySpark

from pyspark.sql import SparkSession
spark_session = SparkSession.builder.enableHiveSupport().getOrCreate()
# Duas maneiras de acessar o contexto do spark a partir da sessão do spark
spark_context = spark_session._sc
spark_context = spark_session.sparkContext

# COMMAND ----------

spark_context

# COMMAND ----------

#criada interface, meio de comunicação entre objetos do Spark (RDD) e StreamingContext

from pyspark.streaming import StreamingContext
ssc = StreamingContext(sc, 1)
lines = ssc.socketTextStream('localhost', 9999)
counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint()
ssc.start()
ssc.awaitTermination()
