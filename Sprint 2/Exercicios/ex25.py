def maiores_que_media(conteudo:dict)->list:
    media = sum(list(conteudo.values()))/len(conteudo)

    chaves =  list(filter(lambda x: conteudo[x] < media,conteudo.keys()))

    nova = []

    for chave in conteudo.keys():
        if(chave not in chaves):
            nova.append((chave,conteudo[chave]))

    return sorted(nova,key=lambda x:x[1],reverse=False)