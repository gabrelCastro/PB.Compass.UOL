import random

random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

random_list = sorted(random_list)

media = sum(random_list)/len(random_list)

valor_minimo = min(random_list)
valor_maximo = max(random_list)

if(len(random_list) % 2 == 0):
    mediana = (random_list[len(random_list)//2] + random_list[len(random_list)//2 -1])/2
else:
    mediana = random_list[len(random_list)//2]
    
print("Media: {}, Mediana: {}, Mínimo: {}, Máximo: {}".format(media,mediana,valor_minimo,valor_maximo))


