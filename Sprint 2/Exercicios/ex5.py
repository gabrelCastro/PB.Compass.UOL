import json

with open("person.json") as arquivo:
    dados_carregados = json.load(arquivo)
    
print(dados_carregados)