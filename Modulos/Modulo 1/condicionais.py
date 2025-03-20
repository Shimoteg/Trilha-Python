#if elif and else

#if example
idade = int(input("Digite sua idade: "))

""" 
Tambem e possivel tranformar o resultado em um valor inteiro
idade = int(idade)
"""

#Maior que
print("Exemplo de comando if")
if idade >= 18:
    print("Voce e maior de idade")
#Igualdade
if idade == 19:
    print("Voce tem 19 anos")
#Menor que
if idade < 18:
    print("Voce e menor de idade")
#Difereça
if idade != 10:
    print("Voce não tem 10 anos")

"""else exemple
Declaração da variavel"""

sabor = "laranja" 

if sabor == "laranja":
    print("Sabor laranja")
else:
    print("Sabor diferente de laranja")

# O metodo elif permite que seja executado a condição para falso adcionando uma nova condição 

lapis = 8
if lapis >= 20:
    print("Lapis HB")
elif lapis >= 12:
    print("Lapis 2B")
else:
    print("Lapis muito fraco")

#shorthand if - else
mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Não pode tirar a carteira de habilitação"
