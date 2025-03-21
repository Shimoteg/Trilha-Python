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

#Objeto do Heroi 
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel) #Usar o super para usar a implementacao 
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"

#Objeto do Inimigo 
class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"
class Jogo:
    """Classe orquestradora do jogo"""
    def __init__(self):
        self.heroi = Heroi("Heroi", vida=100, nivel=5, habilidade="Destruição de mundos\n")
        self.inimigo = Vilao("Arauto do luto", 500, 10, "Desconhecido\n") 

    def iniciar_batalha(self):
        """ Fazer a gestao da batalha em turnos"""
        print("Iniciando a batalha...")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha uma opcao:\n1. Atacar\n2. Especial\n")
 
##Exibe os detalhes (foi realizado dentro do metodo exibir_detalhes())

#heroi = Heroi(nome="Heroi", vida=100, nivel=5, habilidade="Destruição de mundos")
#print(heroi.exibir_detalhes())
#inimigo = Vilao(nome="Arauto do luto", vida=500, nivel=10, tipo="Desconhecido")
#print(inimigo.exibir_detalhes())


#Instancia do jogo e iniciando a batalha
jogo = Jogo()
jogo.iniciar_batalha()