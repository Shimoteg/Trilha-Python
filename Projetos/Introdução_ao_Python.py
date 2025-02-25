
contatos = []
def adicionar_contato(contatos):
    nome_contato = input("Digite o nome do Contato:")
    telefone = input("Digite o telefone do Contato:")
    email = input("Digite o email do Contato:")
    contato = {"Nome": nome_contato, "Favorito": False, "Telefone": telefone, "Email": email}
    contatos.append(contato)
    print(f"Contato {nome_contato} adicionado com sucesso!")

def ver_contatos(contatos):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["Favorito"] else ""
        print(f"{indice}. [{status}] {contato['Nome']} - {contato['Telefone']} - {contato['Email']}")

def editar_contato(contatos):
    ver_contatos(contatos)
    indice_contato = int(input("Digite o numero do contato que deseja editar: "))
    if indice_contato < 1 or indice_contato > len(contatos):
        print("Índice inválido!")
        return
    novo_nome = input("Digite o novo nome do Contato: ")
    novo_telefone = input("Digite o novo telefone do Contato: ")
    novo_email = input("Digite o novo email do Contato: ")
    contatos[indice_contato - 1] = {"Nome": novo_nome, "Telefone": novo_telefone, "Email": novo_email, "Favorito": contatos[indice_contato - 1]["Favorito"]}
    print(f"Contato {novo_nome} editado com sucesso!")

def definir_favorito(contatos):
    ver_contatos(contatos)
    indice_contato = int(input("Digite o numero do contato que deseja definir como favorito:"))
    if indice_contato < 1 or indice_contato > len(contatos):
        print("Índice inválido!")
        return
    contatos[indice_contato - 1]["Favorito"] = not contatos[indice_contato - 1]["Favorito"]
    print(f"Contato {contatos[indice_contato - 1]['Nome']} marcado como favorito")

def ver_favoritos(contatos):
    print("\nLista de Favoritos:")
    for contato in contatos:
        if contato["Favorito"]:
            print(f"{contato['Nome']} - {contato['Telefone']} - {contato['Email']}")

def excluir_contato(contatos):
    ver_contatos(contatos)
    indice_contato = int(input("Digite o numero do contato que deseja excluir: "))
    if indice_contato < 1 or indice_contato > len(contatos):
        print("Índice inválido!")
        return
    contato_excluido = contatos.pop(indice_contato - 1)
    print(f"Contato{contato_excluido['Nome']} excluido com sucesso!")

def menu():
    while True:
        print("\nMenu do Gerenciador de Contatos")
        print("1. Adicionar Contato")
        print("2. Ver Lista de Contatos")
        print("3. Editar Contato ")
        print("4. Definir/Remover Contato como Favorito")
        print("5. Favoritos")
        print("6. Excluir Contato")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_contato(contatos)
        elif escolha == "2":
            ver_contatos(contatos)
        elif escolha == "3":
            editar_contato(contatos)
        elif escolha == "4":
            definir_favorito(contatos)
        elif escolha == "5":
            ver_favoritos(contatos)
        elif escolha == "6":
            excluir_contato(contatos)
        elif escolha == "7":
            print("Encerrando o programa...")
            break

menu()
