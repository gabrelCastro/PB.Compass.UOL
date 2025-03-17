def calcular_valor_maximo(operadores,operandos) -> float:
    lista = []
    lista = list(zip(operadores,operandos))

    def fazerAconta(lista):
        if lista[0] == '+':
            return lista[1][0]+lista[1][1]
        elif lista[0] == '-':
            return lista[1][0]-lista[1][1]
        elif lista[0] == '*':
            return lista[1][0]*lista[1][1]
        elif lista[0] == '/':
            return lista[1][0]/lista[1][1]
        elif lista[0] == '%':
            return lista[1][0]%lista[1][1]
        
    
    lista = list(map(fazerAconta,lista))
    print(lista)
    return max(lista)
