vetor = []

with open("number.txt") as arquivo:
    for x in arquivo:
        vetor.append(x)
        
vetorCasting = list(map(lambda x:int(x), vetor))       

vetorOrdenado = sorted(vetorCasting)

vetorPar = list(filter(lambda x:x%2 == 0,vetorOrdenado))

print(vetorPar[-5:][::-1])
print(sum(vetorPar[-5:][::-1]))