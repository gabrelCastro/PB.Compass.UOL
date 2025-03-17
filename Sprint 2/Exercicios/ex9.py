class Lampada:
    def __init__(self,ligada):
        self.ligada = ligada
        
    def liga(self):
        if(self.ligada == False):
            self.ligada = True
    
    def desliga(self):
        if(self.ligada):
            self.ligada = False
        
    def esta_ligada(self):
        return self.ligada;
        

lamp = Lampada(True)
lamp.liga()
print("A lâmpada está ligada? {}".format(lamp.esta_ligada()))
lamp.desliga()
print("A lâmpada está ligada? {}".format(lamp.esta_ligada()))
