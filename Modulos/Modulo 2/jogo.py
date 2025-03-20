#Personagem: classe mae (tudo que e comum entre os personagems)
#Heroi: heranca de personagem (controlado pelo usuario)
#Vilao: adversario do usuario


class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida  
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}\n"
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel) #Usar o super para usar a implementacao 
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    
class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"
    
heroi = Heroi(nome="Heroi", vida=100, nivel=5, habilidade="Destruição de mundos")
print(heroi.exibir_detalhes())


inimigo = Vilao(nome="Arauto do luto", vida=500, nivel=10, tipo="Desconhecido")
print(inimigo.exibir_detalhes())
