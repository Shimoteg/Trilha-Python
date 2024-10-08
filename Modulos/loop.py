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