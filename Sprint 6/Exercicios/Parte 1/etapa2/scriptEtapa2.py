lista = ["Cachorro", "Gato", "Elefante", "Leão", "Cavalo", "Raposa","Tigre","Urso", "Girafa", "Zebra","Minhoca","Arara","Jacaré","Tucano","Panda","Coala","Canguru","Ornitorrinco","Bicho-preguiça","Tamanduá"]


lista.sort(reverse=True)

for animal in lista:
    print(animal, end=", ")
print("\n")

with open("animais.txt", "w") as arquivo:
    for animal in lista:
        arquivo.write(animal + "\n")

