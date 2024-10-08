#Declaração de variavel
nome = "Gabriel Shimote"

#Declaração com quebra de linhas
nome_completo = """ Gabriel 
Shimote """

Nome = "Gabriel"
Sobrenome = "Shimote"

#Formataçao de texto	
print("Nome completo (1ª forma):", nome)
print("Nome completo (2ª forma):" + nome)
#A segunda maneira de concatenar os dados com a variavel e utilizando o operador + porem ele nao adiciona o espaco entre os dados.
print("Nome completo (3ª forma):" + " " + "Gabriel" + " " + "Shimote")
print("Nome completo (4ª forma): %s " % nome)
print('Nome completo (5ª forma): %s %s ' % (Nome, Sobrenome))
print(f"Nome completo (6ª forma): {Nome} {Sobrenome}")
print("Nome completo (7ª forma): {} {}".format(Nome, Sobrenome))

