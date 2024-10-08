#Muito semelhante as listas, a diferença é que as tuplas sao imutaveis e utilizam () no lugar de  []
lista_tupla = (0, 1, 2, 3, 4, 5, 6, 5, 42, 9, 10)	
print(lista_tupla)

#selecionando elementos da tupla
print(lista_tupla[0])
print(lista_tupla[5])
print(lista_tupla[-1])

#Metodo count
contagem = lista_tupla.count(5)
print("Quantidade de 5: ",contagem)

#Metodo index
indice = lista_tupla.index(42)
print("Posicao do 5: ",indice)

#Criando dicionário
pessoa = {"nome": "Gabriel", "idade": 25, "altura": 1.93, "linguagem": ["python", "java"]} 
print("Exibindo dicionário: ",pessoa)

#Selecionando elementos do dicionário
print(pessoa["linguagem"])

pessoa["faculdade"] = "Wyden University"
print("Exibindo dicionário apos inserir faculdade: ",pessoa)

#Removendo um par chave
del pessoa["faculdade"]
print("Exibindo dicionário apos remover faculdade: ",pessoa)

#Metodos: keys(), values(), items()
chaves = pessoa.keys()
print("Chaves do dicionário: ",chaves)

#Os itens são exibidos como uma tupla 
items = pessoa.items()
print("Items do dicionário: ",items)

#Transformando em lista
chaves = list(pessoa.keys())
print("Item do dicionário[3]: ",chaves[3])

#Pegando valores na tupla dos itens
valores = list(pessoa.items())
print("Item do dicionário: %s = %s" % (valores[2][0], valores[2][1]))



