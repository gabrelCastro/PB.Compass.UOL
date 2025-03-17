lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def dividirListaEm3(listaX):
    listaY = list()
    g = 0
    for x in range(3):
        listaZ = list()
        for y in range(len(listaX)//3):
            listaZ.append(listaX[g])
            g += 1
        listaY.append(listaZ)
    return listaY
    
listaDividida = dividirListaEm3(lista)

print("{} {} {}".format(listaDividida[0],listaDividida[1],listaDividida[2]))
