import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import upper, col, desc


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho do arquivo no S3
caminho_arquivo = args['S3_INPUT_PATH']

# 1 Ler o arquivo CSV como DataFrame
df = spark.read.option("header", True).csv(caminho_arquivo)

# 2 Imprimir o schema
df.printSchema()

# 3 Converter os nomes para MAIÚSCULO
df = df.withColumn("nome", upper(col("nome")))

# 4 Imprimir contagem total de linhas
print("Total de linhas:", df.count())

# 5. Contagem de nomes agrupada por ano e sexo, ordenada por ano decrescente
agrupado = df.groupBy("ano", "sexo").count().orderBy(desc("ano"))
agrupado.show()

# 6 Nome feminino mais frequente e o ano
feminino = df.filter(col("sexo") == "F")
mais_feminino = feminino.groupBy("nome", "ano").count().orderBy(desc("count")).limit(1)
print("Nome feminino mais frequente:")
mais_feminino.show()

# 7 Nome masculino mais frequente e o ano
masculino = df.filter(col("sexo") == "M")
mais_masculino = masculino.groupBy("nome", "ano").count().orderBy(desc("count")).limit(1)
print("Nome masculino mais frequente:")
mais_masculino.show()

total_por_ano_sexo = df.groupBy("ano", "sexo").count().orderBy("ano").limit(10)

# Mostra o resultado
print("Total de registros por ano e sexo (primeiros 10):")
total_por_ano_sexo.show()

df.write.mode("overwrite") \
    .format("json") \
    .partitionBy("sexo", "ano") \
    .save(args['S3_TARGET_PATH'])


job.commit()