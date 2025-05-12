import names,os,time,random

random.seed(40)

qtd_nomes_unicos = 39080

qtd_nomes_aleatorios = 10000000

aux=[]

aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print("Gerando {} nomes aleatórios...".format(qtd_nomes_aleatorios))

dados=[]

dados = random.choices(aux, k=qtd_nomes_aleatorios)

with open("nomes_aleatorios.txt", "w") as f:
    for i in range(qtd_nomes_aleatorios):
        f.write(dados[i] + "\n")