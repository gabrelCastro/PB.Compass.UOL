class Aviao:
    
    def __init__(self,modelo,velocidade_maxima,capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "azul"
        self.capacidade = capacidade
        
    def __str__(self):
        return "O avião de modelo {} possui uma velocidade máxima de {}, capacidade para {} passageiros e é da cor {}.".format(self.modelo,self.velocidade_maxima,self.capacidade,self.cor)
        

avioes = [Aviao("BOIENG456",1500,400) ,Aviao("Embraer Praetor 600",863,14),Aviao("Antonov An-2",258,12)]


for aviao in avioes:
    print(aviao)

