def funcao(*args, **kwargs):
    for x in args:
        print(x)
    
    for chave, valor in kwargs.items():
        print(valor)


funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)