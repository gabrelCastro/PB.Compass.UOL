import random

lista_numeros_aleatorios = []

lista_numeros_aleatorios = [random.randint(1, 100) for _ in range(250)]

lista_numeros_aleatorios.reverse()

print("Lista de números aleatorios:")
for numero in lista_numeros_aleatorios:
    print(numero, end=", ")
