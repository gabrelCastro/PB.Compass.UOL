import requests
import pandas as pd
from dotenv import load_dotenv
import boto3
import os
import json
import io
from datetime import date


datat = date.today()


s3 = boto3.client('s3')

response = s3.get_object(Bucket='data-lake-do-gabriel-castro', Key='RAW/LOCAL/CSV/Movies/2025/4/26/movies.csv')
conteudo = response['Body'].read()
buffer = io.BytesIO(conteudo)


api_key = os.getenv('API_KEY')
url = f"https://api.themoviedb.org/3/genre/movie/list?language=en"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer {}".format(api_key)
}

response = requests.get(url,headers=headers)
data = response.json()

for x in data['genres']:
    if(x['name'] == 'Action'):
        idAction = x['id']
    if(x['name'] == 'Adventure'):
        idAdventure = x['id']


df1 = pd.read_csv(buffer, sep="|")

tem = False
i = 0
for t in range(5): # 5 arquivos com 100 filmes aproximadamente
    definitivo = [] # Criando uma lista para armazenar os filmes
    while len(definitivo) < 95: # Enquanto a lista não tiver 95 filmes aproximadamente
        url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&page={}&sort_by=revenue.desc&with_genres={}%7C{}".format(str(1+i),idAction, idAdventure)
        response = requests.get(url,headers=headers)
        resultados = response.json()['results']
        for y in resultados: # Para cada filme retornado
            tem = False
            for x in df1['tituloOriginal']:
                if(x == y['original_title']): # Verifica se o filme já existe na lista
                    tem = True
                    break # Se o filme já existe, não adiciona e para o loop procurando ele
            if(tem == False): # Se o filme não existe na lista, adiciona
                definitivo.append(y)
            
        i+=1 # Incrementa o número da página

    json_string = json.dumps(definitivo, ensure_ascii=False) # Converte a lista de filmes para JSON

    s3.put_object(Bucket='data-lake-do-gabriel-castro', Key='RAW/LOCAL/JSON/Movies/{}/{}/{}/json{}.json'.format(datat.year, datat.month, datat.day,t), Body=json_string.encode('utf-8'))

def lambda_handler(event, context):
    print("Handler executado com sucesso")
    return {
        'statusCode': 200,
        'body': 'OK'
    }