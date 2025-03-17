resultado = "1,3,4,6,10,76"

def funcao(palavra):
     numerosLetras = palavra.split(',')
     numeros = list()
     for x in numerosLetras:
         numeros.append(int(x))
     return sum(numeros)
    
print(funcao(resultado))