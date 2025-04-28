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
for t in range(5):
    definitivo = []
    while len(definitivo) < 95:
        url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&page={}&sort_by=revenue.desc&with_genres={}%7C{}".format(str(1+i),idAction, idAdventure)
        response = requests.get(url,headers=headers)
        resultados = response.json()['results']
        for y in resultados:
            tem = False
            for x in df1['tituloOriginal']:
                if(x == y['original_title']):
                    tem = True
                    break
            if(tem == False):
                definitivo.append(y)
            
        i+=1

    json_string = json.dumps(definitivo, ensure_ascii=False)

    s3.put_object(Bucket='data-lake-do-gabriel-castro', Key='RAW/LOCAL/JSON/Movies/{}/{}/{}/json{}.json'.format(datat.year, datat.month, datat.day,t), Body=json_string.encode('utf-8'))

def lambda_handler(event, context):
    print("Handler executado com sucesso")
    return {
        'statusCode': 200,
        'body': 'OK'
    }