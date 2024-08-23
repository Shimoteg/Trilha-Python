dog = "Fumeica"

dogTwo = "Faisca" 

vdd = True

if vdd == True:
    print(dog)
else:
    print(dogTwo)

# Listas 

aLista = ["Primeiro", 2, "bic", 42, True]

print(aLista[0])
print(aLista[2:4])
print(aLista[:4])
print(aLista[3:])

#Metodo para adicionar um item a lista
aLista.append("Ultimo")
print(aLista)

#Metodo indice
indice = aLista.index("Ultimo")
print(indice)

#Metodo insert: adiciona um item em uma determinada posicao
aLista.insert(1,"2º")
print("Lista apos o insert: ", aLista)

#Metodo pop: remove um item da lista
removendo_elemento = aLista.pop(2)
print("Elemento removido: ", removendo_elemento)
print("Lista apos o pop: ", aLista)

#Metodo remove: remove um item da lista
aLista.remove(True)
print("Lista apos o remove: ", aLista)

#Metodo sort: ordena uma lista
Lista_ordenada = [15, 50, 89, 860, 2, 8]
Lista_ordenada.sort()
print("Lista em ordem: ", Lista_ordenada)