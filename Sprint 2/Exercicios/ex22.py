from functools import reduce


def calcula_saldo(lancamentos) -> float:
        
    lancamentos = list(map(lambda x: x[0] * 1 if x[1] == 'C' else x[0] * -1,lancamentos))
    
    return reduce(lambda acumulador,elemento: elemento + acumulador,lancamentos,0)
        