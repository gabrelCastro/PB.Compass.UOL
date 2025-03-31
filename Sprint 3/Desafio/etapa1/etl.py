import pandas as pd


df = pd.read_csv('concert_tours_by_women.csv') # Lendo o CSV


# Filtrando os dados de gross
# Tira tudo que não é número

def convertToNumber(x):
    numero = ""
    vetor = list(x)
    for indice in range(len(vetor)):
        if(vetor[indice].isdigit()):
            numero += vetor[indice]
    return float(numero)

# Aplicando a função de conversão nas tabelas numéricas
df['Average gross'] = df['Average gross'].apply(convertToNumber) # Aplicando a função de conversão
df['Actual gross'] = df['Actual gross'].apply(convertToNumber) # Aplicando a função de conversão
df['Adjustedgross (in 2022 dollars)'] = df['Adjustedgross (in 2022 dollars)'].apply(convertToNumber) # Aplicando a função de conversão

# Criando as colunas com a função que faz isso na linha
def separar_anos(linha):
    anos = linha["Year(s)"].split("-")
    if len(anos) == 1:
        linha["Start year"] = anos[0]
        linha["End year"] = anos[0]
    else:
        linha["Start year"] = anos[0]
        linha["End year"] = anos[1]
    return linha

# Aplica em todas as linhas do dataFrame
df = df.apply(separar_anos, axis=1)

df.head(5)

# Criando a coluna dos anos


import re

# Filtrando os dados de gross tirando o que não é alfanumérico
def convertToAl(x):
    string = ""
    vetor = list(x)
    for indice in range(len(vetor)):
        if(vetor[indice].isalnum()):
            string += vetor[indice]
        elif (vetor[indice] == " "):
            string += " "
    return string

df['Tour title'] = df['Tour title'].apply(convertToAl) # Aplicando a função de conversão


# Tira tudo que tá depois de Tour, incluindo Tour, depois adiciona de novo 
df['Tour title'] = [re.split(r'\bTour\b', x)[0] + "Tour" for x in df['Tour title']] 

df.head(5)


# Renomeando as colunas
df = df.rename(columns={'Adjustedgross (in 2022 dollars)': 'Adjusted gross(in 2022 dollars)'})

df[['Rank','Actual gross','Adjusted gross(in 2022 dollars)','Artist','Tour title','Shows','Average gross','Start year','End year']].to_csv('../volume/csv_limpo.csv',index=False)
