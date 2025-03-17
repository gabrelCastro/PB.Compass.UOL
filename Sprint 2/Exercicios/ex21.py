def conta_vogais(texto:str)-> int:
    return len(list(filter(lambda x:x.lower() in ['a','e','i','o','u'],texto)))