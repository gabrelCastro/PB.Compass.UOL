import sys, unicodedata, re, datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F, Window, types as T   #  <<< faltava

args = getResolvedOptions(
    sys.argv,
    ['JOB_NAME', 'S3_INPUT1_PATH', 'S3_INPUT2_PATH', 'S3_TARGET_PATH']
)

sc = SparkContext.getOrCreate()          
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

TMDB_PARQUET  = args['S3_INPUT1_PATH']
LOCAL_PARQUET = args['S3_INPUT2_PATH']  


# ───────── 1. LEITURA ────────────────────────────────────────────────────────
df_tmdb  = spark.read.parquet(TMDB_PARQUET)
df_local = spark.read.parquet(LOCAL_PARQUET)

# ───────── 2. LIMPEZA / CASTS MÍNIMOS ────────────────────────────────────────
CASTS_TMDB = {"popularity": "double", "vote_average": "double", "vote_count": "int"}
for c, typ in CASTS_TMDB.items():
    if c in df_tmdb.columns:
        df_tmdb = df_tmdb.withColumn(c, F.col(c).cast(typ))

if "release_date" in df_tmdb.columns and str(df_tmdb.schema["release_date"].dataType) == "StringType":
    df_tmdb = df_tmdb.withColumn("release_date", F.to_date("release_date", "yyyy-MM-dd"))

CASTS_LOCAL = {
    "anolancamento": "int",
    "tempominutos" : "int",
    "notamedia"    : "double",
    "numerovotos"  : "int",
    "anonascimento": "int",
    "anofalecimento": "int",
}
for c, typ in CASTS_LOCAL.items():
    if c in df_local.columns:
        df_local = df_local.withColumn(c, F.col(c).cast(typ))

# ───────── 3. UDF SLUGIFY ────────────────────────────────────────────────────
import unicodedata, re
@F.udf(returnType=T.StringType())
def slugify(txt):
    if txt is None:
        return None
    txt = unicodedata.normalize("NFD", txt)
    txt = "".join(ch for ch in txt if unicodedata.category(ch) != "Mn")
    txt = re.sub(r"[^A-Za-z0-9]", "", txt.lower())
    return txt.strip()

df_tmdb  = df_tmdb .withColumn("slug", slugify("original_title"))
df_local = df_local.withColumn("slug", slugify("titulooriginal"))

# ───────── 4. DIMENSÃO FILME (LOCAL) ─────────────────────────────────────────
filmes_local = (df_local
    .select("slug",
            F.col("titulooriginal").alias("titulo_original_local"),
            F.col("titulopincipal").alias("titulo_principal_local"),
            "anolancamento", "tempominutos",
            F.col("notamedia").alias("nota_media_local"),
            F.col("numerovotos").alias("num_votos_local"),
            "genero")
    .dropDuplicates(["slug"]))

# ───────── 5. DIMENSÃO ATOR ─────────────────────────────────────────────────
norm_name = F.lower(F.regexp_replace(F.trim(F.col("nomeartista")), r"\s+", " "))

atores_raw = (df_local
    .withColumn("nomeartista_norm", norm_name)
    .select("nomeartista_norm", "generoartista",
            "anonascimento", "anofalecimento",
            "profissao", "titulosmaisconhecidos")
    .dropDuplicates(["nomeartista_norm"]))

w_ator = Window.orderBy("nomeartista_norm")
dim_ator = atores_raw.withColumn("ator_sk", F.row_number().over(w_ator))

# ───────── 6. FATO TEMPORÁRIA ───────────────────────────────────────────────
fato_tmp = (df_local
    .withColumn("nomeartista_norm", norm_name)
    .select("slug", "nomeartista_norm", "personagem")
    .distinct())

# ───────── 7. DIMENSÃO FILME (JOIN TMDB × LOCAL) ────────────────────────────
tmdb_clean = df_tmdb.dropDuplicates(["slug"]).alias("t")
local_clean = filmes_local.alias("l")

tmdb_runtime = F.col("t.runtime") if "runtime" in df_tmdb.columns else F.lit(None)
tmdb_genres  = F.col("t.genero")  if "genero" in df_tmdb.columns else F.lit(None)

w_filme = Window.orderBy("slug")       # <-- sem partitionBy!

dim_filme = (local_clean
    .join(tmdb_clean, "slug", "full_outer")
    .withColumn("filme_sk", F.dense_rank().over(w_filme))  # ou row_number()
    .select(
        "filme_sk", "slug",
        F.coalesce("t.original_title",  "l.titulo_original_local").alias("titulo_original"),
        F.coalesce("t.title",           "l.titulo_principal_local").alias("titulo_principal"),
        F.coalesce(F.year("t.release_date"), "l.anolancamento").alias("ano_lancamento"),
        F.coalesce(
            "t.release_date",
            F.to_date(F.concat_ws('-', "l.anolancamento", F.lit('01'), F.lit('01')))
        ).alias("data_lancamento"),
        F.coalesce(tmdb_runtime, F.col("l.tempominutos")).alias("duracao_minutos"),
        F.coalesce("t.vote_average", "l.nota_media_local").alias("nota_media"),
        F.coalesce("t.vote_count",   "l.num_votos_local").alias("num_votos"),
        F.coalesce(tmdb_genres, F.col("l.genero")).alias("genero"),
        "t.overview", "t.poster_path", "t.original_language",
        "t.adult", "t.video", "t.popularity"
    ))


# ───────── 8. FACT FILME × ATOR ─────────────────────────────────────────────
fato_filme_ator = (fato_tmp
    .join(dim_filme.select("filme_sk", "slug"), "slug")
    .join(dim_ator.select("ator_sk", "nomeartista_norm"), "nomeartista_norm")
    .select("filme_sk", "ator_sk", "personagem"))


caminho_s3 = f"{args['S3_TARGET_PATH'].rstrip('/')}/2025/4/29"
dim_filme.write.mode("append").parquet(caminho_s3 + '/dimensaoFilme/')
dim_ator.write.mode("append").parquet(caminho_s3 + '/dimensaoAtor/')
fato_filme_ator.write.mode("append").parquet(caminho_s3 + '/tabelaFato/')


job.commit()