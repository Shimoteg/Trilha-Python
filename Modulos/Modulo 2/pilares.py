#Abstracao, encapsulamento, heranca e polimorfismo

#Herança 
print("\nExemplo de Heranca: ")
class Animal: 
    def __init__(self, nome) -> None:
        self.nome = nome
       
    def andar(self):
        print(f"O animal {self.nome} andou")
        return 
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "au au"
    
class Gato(Animal):
    def emitir_som(self):
        return "miau miau"

dog = Cachorro(nome="Rex")
cat = Gato(nome="Garfield")

print("\nExemplo de Polimorfismo: ")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de Encapsulamento: ")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado

    def depositar(self, valor):
        if valor > 0: 
            self.__saldo += valor 

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    


conta = ContaBancaria(saldo=1000)
print(f"Saldo: {conta.consultar_saldo()}")
conta.depositar(500)
print(f"Saldo: {conta.consultar_saldo()}")
conta.sacar(200)
print(f"Saldo: {conta.consultar_saldo()}")

conta_do_fumeica = ContaBancaria(saldo=50000)
print(f"Saldo na conta do fumeica: {conta_do_fumeica.consultar_saldo()}")


print("\nExemplo de abstracao: ")

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod #decorador
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None: 
        pass

    def ligar(self):
        #implementacao
        return "Carro ligado"
    
    def desligar(self):
        return "Carro desligado"
    
carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())