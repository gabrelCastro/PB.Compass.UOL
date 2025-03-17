class Calculo:
    
    @staticmethod
    def somaDois(x,y):
        return x+y
    @staticmethod
    def subtracao(x,y):
        return x-y
        

x = 4

y = 5
        
        
print("Somando: {} + {} = {}\nSubtraindo: {}-{} = {}".format(x,y,Calculo.somaDois(x,y),x,y,Calculo.subtracao(x,y)))