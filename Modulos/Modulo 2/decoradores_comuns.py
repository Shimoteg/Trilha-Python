# @classmethod os decoradores tem o @ antes
# @staticmethod 

class MinhaClasse:
    valor = 10 #Atributop de classe

    def __init__(self, nome) -> None:
        self.nome = nome #Atributo da instancia
    
    #requer uma isntancia para ser chamado
    def metodo_instancia(self):
        return f"Metodo da instancia {self.nome}"
    
    @classmethod
    def metodo_classe(cls): #cls recebe a classe
        return f"Metodo da classe chamado para valor {cls.valor}" 
    
    @staticmethod
    def metodo_estatico(): #nao requer uma instancia 
        return "Metodo estatico"
        

obj = MinhaClasse(nome="Classe exemplo") 
print(obj.metodo_instancia())

#Acessando atributo da classe
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self,marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao_carro):
        marca, modelo, ano = configuracao_carro.split(",")
        return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2020"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}, Modelo: {carro1.modelo}, Ano: {carro1.ano}")

class Matematica: 

    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(a=2, b=3))