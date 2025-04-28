import requests
import pandas as pd
from IPython.display import display
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&amp;language=pt-BR"

response = requests.get(url)
data = response.json()
filmes = [0]

for movie in data['results']:
    df = {
          'Titulo': movie['title'],
          'Data de Lançamento': movie['release_date'],
          'Nota': movie['vote_average'],
          'Resumo': movie['overview'],
          'Capa': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"}
    filmes.append(df)

df = pd.DataFrame(filmes)
display(df)