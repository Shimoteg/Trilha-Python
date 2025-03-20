#O loop permite repetir um bloco de codigo enquanto uma condição for verdadeira

#For: utilizado para iterar uma sequencia de elementos (lista, tuplas, dicionarios )

print("For utilizando lista")
lista = [1,2,3,4,5,]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
tupla = (0, 1, 2, 3, 4, 5, 6, 5, 42, 9, 10)
for elemento in tupla:
    print(elemento)

#Utilizando dicionarios no for
pessoa = {"nome": "Gabriel", "idade": 25, "altura": 1.93, "linguagem": ["python", "java"]}
print("For utilizando dicionario")
for chave in pessoa.keys():
    print(chave, pessoa[chave])


#verificaçao dos valores
print(" For utilizando dicionario value")
for valor in pessoa.values():
    print(valor)


#Tambem e possivel realizar o get de ambos os elementos tranfdormando em uma lista
print("For utilizando dicionario get")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#Range(): interalo numerico // retorna em lista os valores declarados
print("\n Usando a funçao range() e transformando em lista: ")
range(0, 10)
print(list(range(0,10)))

#Short hand =  a função range poide ser dado o valor final que comeca em 0
print("\n Exemplo de range usando apenas o valor final (50): ")
print(list(range(50)))

#Utilizando a funcao len() junto com a range() e possivel mensurar o tamanho da lista *Esta maneira e utilizada pois permite alteracao
print("\n Utilizando a funçao len() junto com a range(): ")
lista = [0, 1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print("Indice: ", indice)
    print("Elemento: ", lista[indice])

#Realizando alteracao na lista
print("\n Realizando alteracao na lista: ")
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 100
    else:
        lista[indice] = 0
print("\n Apos a alteracao: ")
print(lista)

#Enumerate(): permite retornar o indice e o elemento da lista
lista_enumerate = ["a", "b", "c"]	
print("\n Usando enumerate(): ")
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 2")