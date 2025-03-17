vetor = []

with open("estudantes.csv",encoding="utf-8") as arquivo:
      vetor = list(map(lambda x:x.split(','),arquivo))
      

dicionario = {}

for x in range(len(vetor)):
      for y in range(len(vetor[x])):
            vetor[x][y] = vetor[x][y].replace('\n','')
            if(vetor[x][y].isdigit()):
                  vetor[x][y] = int(vetor[x][y])
      maioresNotas = sorted(vetor[x][1:],reverse=True)[:3]
      maioresNotas = sorted(vetor[x][1:],reverse=True)[:3]
      maioresNotas = sorted(vetor[x][1:],reverse=True)[:3]
      dicionario[vetor[x][0]] = {}
      dicionario[vetor[x][0]]["maiores"] = maioresNotas
      dicionario[vetor[x][0]]["media"] = round(sum(maioresNotas)/len(maioresNotas),2)


dicionario = sorted(dicionario.items(),key=lambda x:x[0])

for x in dicionario:
      print("Nome: {} Notas: {} Média: {}".format(x[0],x[1]["maiores"],x[1]["media"]))
            
                

