"""
contar_palavras_rdd.py – versão puramente Spark
Autor: Gabriel Ferreira (exemplo didático)
Descrição: Conta as palavras de um .txt usando RDD e regex.
"""
from pyspark import SparkContext
import re
import requests
from dotenv import load_dotenv

token = "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"
url = f"https://api.github.com/repos/gabrelCastro/PB.Compass.UOL/contents/README.md"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3.raw"
}

resposta = requests.get(url, headers=headers)

print(resposta)

if resposta.status_code == 200:
    with open("arquivo_baixado.txt", "wb") as f:
        f.write(resposta.content)
    print("Arquivo baixado com sucesso!")

# 1) Contexto Spark -----------------------------------------------------------
#sc = SparkContext(master="local[*]",appName="contagem_palavras_rdd")

# 2) Parametrização -----------------------------------------------------------
ARQUIVO_FONTE = "arquivo_baixado.txt"
regex_palavra = re.compile(r"[^\wÀ-ÿ]+", flags=re.UNICODE)

# 3) Função auxiliar ----------------------------------------------------------
def quebrar_em_palavras(linha):
    """
    Recebe uma linha, deixa tudo minúsculo, troca pontuação por espaço
    e devolve a lista de palavras encontradas.
    """
    return regex_palavra.sub(" ", linha.lower()).split()

# 4) Pipeline RDD -------------------------------------------------------------
contagem = (sc.textFile(ARQUIVO_FONTE)     # lê o arquivo em N partições
              .flatMap(quebrar_em_palavras) # quebra cada linha em palavras
              .filter(lambda p: p)          # remove vazios (evita '' gerado pelo split)
              .map(lambda p: (p, 1))        # vira par (palavra, 1)
              .reduceByKey(lambda a, b: a+b) # soma as ocorrências
              .sortBy(lambda par: par[1], ascending=False)
           )

# 5) Ação final ---------------------------------------------------------------
for palavra, qtd in contagem.collect():     # coleta apenas o resultado agregado
    print(f"{palavra}: {qtd}")

sc.stop()