class Passaro:
    
    def voar(self):
        pass
    
    def emitirSom(self):
        pass
    

class Pato(Passaro):
    
    def voar(self):
        print("Pato\nVoando...")
    
    def emitirSom(self):
        print("Pato emitindo som...\nQuack Quack")


class Pardal(Passaro):
    
    def voar(self):
        print("Pardal\nVoando...")
    
    def emitirSom(self):
        print("Pardal emitindo som...\nPiu Piu")
        

pardal = Pardal()

pato = Pato()


pato.voar()
pato.emitirSom()
pardal.voar()
pardal.emitirSom()

    
    