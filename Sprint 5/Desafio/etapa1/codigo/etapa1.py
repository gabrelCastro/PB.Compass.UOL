import boto3
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import date

data = date.today()

load_dotenv(override=True)

df = pd.read_csv("./csv/movies.csv", sep="|")
df2 = pd.read_csv("./csv/series.csv", sep="|")

df.head(5)
df2.head(5)
 
s3 = boto3.client('s3',
   aws_access_key_id= os.getenv('KEY_ID'),
   aws_secret_access_key= os.getenv('ACESS_KEY'),
   aws_session_token= os.getenv('TOKEN'),
   region_name='us-east-1'
)

bucket_name = 'data-lake-do-gabriel-castro'
arquivo_local = 'csv/movies.csv'
chave_destino = 'RAW/LOCAL/CSV/Movies/{}/{}/{}/movies.csv'.format(data.year, data.month, data.day)

try:
    print("Enviando arquivo de filmes para o S3...")
    s3.upload_file(arquivo_local, bucket_name, chave_destino)
    print("Arquivo de filmes enviado com sucesso para o S3.")
except Exception as e:
    print("Erro ao enviar o arquivo de filmes para o S3:", e)


bucket_name = 'data-lake-do-gabriel-castro'
arquivo_local = 'csv/series.csv'
chave_destino = 'RAW/LOCAL/CSV/Series/{}/{}/{}/series.csv'.format(data.year, data.month, data.day)


# Enviar o arquivo para o S3
try:
    print("Enviando arquivo de series para o S3...")
    s3.upload_file(arquivo_local, bucket_name, chave_destino)
    print("Arquivo de series enviado com sucesso para o S3.")
except Exception as e:
    print("Erro ao enviar o arquivo de series para o S3:", e)