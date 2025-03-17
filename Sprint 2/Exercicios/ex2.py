for x in ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']:
    if(x[::-1] == x):
        print("A palavra: {} é um palíndromo".format(x))
    else:
        print("A palavra: {} não é um palíndromo".format(x))
