class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.name} amamentou hoje!"


class Ave(Animal):
    def voar(self):
        return f"{self.name} voou hoje!"	
    
#Exeplo de heranca multipla

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrasonicos"
        #Super chama a implementacao da classe mae return
        

morcego = Morcego(name="Batman")
#Acessando os metodoas da classe "Animal" 
print("Nome do morcego:", morcego.name)
print("Som do morcego: ", morcego.emitir_som())

#Acessando os metodoas da classe "Mamifero"
print("Morcego amamentou: ", morcego.amamentar())
print("Morcego voou: ", morcego.voar())