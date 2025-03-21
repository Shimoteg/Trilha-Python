#Poo - programacao orientada a objetos
#objetos = classees que representam coisas do mundo real
#classes = molde para criar objetos

class People:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
#  def __init__(self) -> None:             Fora de uma classe e uma funcao e quando
#       pass                                 esta dentro e um metodo

#Metodos sao as acoes permitidas para os objetos

    def saudacao(self):
        return f"Ola, meu nome e {self.name} e eu tenho {self.age} anos."


#Objeto = instancia da classe
people1 = People("Ane", 26) #criando um objeto
mensagem = people1.saudacao() #chamando um metodo
print(mensagem)

#Criar outra "pessoa"
people2 = People(name="Gabriel", age=26)
mensagem = people2.saudacao()
print(mensagem)