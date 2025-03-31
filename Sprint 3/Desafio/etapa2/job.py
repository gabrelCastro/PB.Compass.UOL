import pandas as pd
import matplotlib.pyplot as plt
import time

time.sleep(1) # Esperar 1 segundo para que o arquivo da primeira parte seja criado

dataFrame = pd.read_csv("../volume/csv_limpo.csv"); # Lendo o arquivo csv

##### Exercício 1

dataFrameEx1 = dataFrame.groupby("Artist")["Actual gross"]

mediaEx1 = dataFrameEx1.mean().rename_axis("Actual gross").reset_index(name="Media")
numeroValores = dataFrameEx1.count().reset_index(name="Contagem")

# Ordenando os valores primeiro pela contagem depois pela media do Actual gross
resultado = pd.concat([mediaEx1,numeroValores],axis=1).sort_values(by=["Contagem","Media"],ascending=False).iloc[0]


# Resultado do primerio exercício
stringFinal = "Q1:\n" 

stringFinal += "--- A artista que mais aparece na lista e também possui a maior média de faturamento bruto é a {} com {} aparições e média de {} milhões\n".format(resultado["Artist"],resultado["Contagem"],int(resultado["Media"]/1000000))



##### Exercício 2

resposta2 = dataFrame[dataFrame['Start year'] - dataFrame['End year'] == 0].sort_values(by=["Average gross"], ascending=False).iloc[0][["Tour title","Average gross"]]

stringFinal += "Q2:\n"
stringFinal += "--- A turnê com maior média de faturamento bruto é a {} com média de {} milhões\n".format(resposta2["Tour title"],int(resposta2["Average gross"]/1000000))



##### Exercício 3

dataFrame['Average per show'] = dataFrame['Adjusted gross(in 2022 dollars)'] / dataFrame['Shows']

resposta3 = dataFrame.sort_values(by=['Average per show'], ascending=False).iloc[0:3][["Artist","Tour title",'Average per show']]

stringFinal += "Q3:\n"
stringFinal += "As 3 artistas que possuem o show mais lucrativo por apresentação são:\n"
for index, row in resposta3.iterrows():
    stringFinal += "  --- {} com a turnê {} com um valor médio de {} milhões\n".format(row["Artist"],row["Tour title"],int(row["Average per show"]/1000000))



# Escrever no arquivo
with open("../volume/respostas.txt",'w') as arquivo:
    arquivo.write(stringFinal)


##### Exercício 4
dataFrameEx1 = dataFrame.groupby("Artist")["Actual gross"]

mediaEx1 = dataFrameEx1.sum().rename_axis("Actual gross").reset_index(name="Faturamento total")
numeroValores = dataFrameEx1.count().reset_index(name="Contagem")

resultado = pd.concat([mediaEx1,numeroValores],axis=1).sort_values(by=["Contagem","Faturamento total"],ascending=False).iloc[0]

artista = resultado["Artist"]

resultadoEx4 = dataFrame[dataFrame["Artist"] == artista][["Actual gross","Start year","Tour title"]]

plt.plot(resultadoEx4["Start year"],resultadoEx4["Actual gross"])
plt.title("Faturamento por ano "+ artista)
plt.xlabel("Ano")
plt.ylabel("Faturamento")
plt.savefig("../volume/Q4.png") 

plt.clf()


##### Exercício 5

resultadoEx5 = dataFrame.groupby("Artist")["Shows"].sum().sort_values(ascending=False).iloc[0:5]

plt.bar(resultadoEx5.index,resultadoEx5)

plt.title("Shows por artista")

plt.savefig("../volume/Q5.png") 
