
#Para criar comentários de uma linha utilizamos o simbolo # e para criar um comentário de multiplas linhas usamos o simbolo """ 

""" Exemplo de um comentário de multiplas linhas 
 Exemplo de um comentário de multiplas linhas  """

#Declarando variavels e atribuindo valores
nome = "Gabriel" + "Shimote"   

""" Tambem pode ser escrito da seguinte forma

    nome = "Gabriel" + /
        "Shimote"
"""

# O objeto em python nao necessita de chaves porem ele realiza a indentificação atraves da indentação. 

idade = 25
if idade >= 18:
    print("Voce e maior de idade")
else:
    print("Voce e menor de idade")

#Variaveis

#Inteiro
numero_inteiro = 4
print("Inteiro = ", numero_inteiro)

#Real com ponto flutuante
numeroReal = 4.5
print("Real com ponto flutuante = ", numeroReal)

#type () para saber o tipo da variavel
print("Tipo da variavel inteiro = ", type(numero_inteiro))
print("Tipo da variavel real = ", type(numeroReal))

#Soma
soma = 1 + 1
print("1 + 1 = ", soma)

#Subtracao
subtracao = 43 - 1
print("43 - 1 = ", subtracao)

#Multiplicacao
multiplicacao = 2 * 15
print("2 * 15 = ", multiplicacao)

#Divisão
divisao = 9 / 3
print("9 / 3 = ", divisao)
print("Tipo da variavel da divisao = ", type(divisao))
#Para transformar o resultado em inteiro, pois a divisao resulta em float
print("Tipo da variavel da divisao int = ", int(divisao))