import sys
from datetime import datetime

from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, when, lit, array_contains

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source = args['S3_INPUT_PATH']

df = spark.read.json(source)

df.show(5)

df = df.drop("backdrop_path") # Removendo coluna desnecessária

# IDS dos generos de acordo com a API do TMDB
idAventura = 12 
idAcao = 28

try:
    df = df.withColumn(
        "genero_new",
        when(
            (col("genre_ids").isNotNull()) &
            array_contains(col("genre_ids"), idAcao) &
            array_contains(col("genre_ids"), idAventura), # Se o genero contiver Action e Adventure
            lit("Action and Adventure") # A coluna nova vai ser Action and Adventure
        ).when(
            (col("genre_ids").isNotNull()) & array_contains(col("genre_ids"), idAventura), # Se o genero contiver apenas Adventure
            lit("Adventure") # A coluna nova vai ser Adventure
        ).when(
            (col("genre_ids").isNotNull()) & array_contains(col("genre_ids"), idAcao), # Se o genero contiver apenas Action
            lit("Action") # A coluna nova vai ser Action
        ).otherwise(lit(None)) # Se não contiver nenhum dos dois, a coluna nova vai ser None
    )

    # Tira a coluna genre_ids e troca por genero_new
    df = df.filter(col("genero_new").isNotNull()) \
           .drop("genre_ids") \
           .withColumnRenamed("genero_new", "genero")

    print("Gêneros filtrados!")
except Exception as e:
    print("Falha ao filtrar gêneros!")
    raise

# Data atual
hoje = datetime.now()
caminho_s3 = f"{args['S3_TARGET_PATH'].rstrip('/')}/{hoje:%Y}/{hoje:%m}/{hoje:%d}"
df.write.mode("append").parquet(caminho_s3)

job.commit()