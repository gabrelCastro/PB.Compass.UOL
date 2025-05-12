import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, when, lit

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source = args['S3_INPUT_PATH']

df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [
            source
        ]
    },
    "csv",
    {"withHeader": True, "separator": "|"},
)

df = df.toDF() # Passando para DataFrame do Spark

numero_linhas_antes = df.count() # Contando o número de linhas antes da filtragem

try:
    df = df.withColumn( 
        "genero_new", # Nova coluna com os generos colocados de forma correta
        when(
            (col("genero").isNotNull()) &
            (col("genero").contains("Action")) &
            (col("genero").contains("Adventure")), # Se o genero contiver Action e Adventure
            lit("Action and Adventure") # A coluna nova vai ser Action and Adventure
        ).when(
            (col("genero").isNotNull()) & (col("genero").contains("Adventure")), # Se o genero contiver apenas Adventure
            lit("Adventure") # A coluna nova vai ser Adventure
        ).when(
            (col("genero").isNotNull()) & (col("genero").contains("Action")), # Se o genero contiver apenas Action
            lit("Action") # A coluna nova vai ser Action
        ).otherwise(lit(None)) # Se não contiver nenhum dos dois, a coluna nova vai ser None
    )

    # Tira a coluna genero e troca por genero_new
    df = df.filter(col("genero_new").isNotNull()) \
           .drop("genero") \
           .withColumnRenamed("genero_new", "genero")

    print("Gêneros filtrados!")
except Exception as e:
    print("Falha ao filtrar gêneros!")
    raise

df = df.dropDuplicates(["tituloPincipal", "anoLancamento"]) # Removendo filmes duplicados por conta dos atores
print("Filmes duplicados eliminados") 

numero_linhas_depois = df.count()
print(f"{numero_linhas_antes - numero_linhas_depois} linhas eliminadas")

# Data atual
hoje = datetime.now()
caminho_s3 = f"{args['S3_TARGET_PATH'].rstrip('/')}/{hoje:%Y}/{hoje:%m}/{hoje:%d}"

df.write.mode("append").parquet(caminho_s3)

job.commit()
sc.stop()
