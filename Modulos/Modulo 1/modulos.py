#Sao arquivos que contem arquivbos ou isntrucoes que podem ser reutilizados em outros programas
# Em python alguns modulos ja vem com o python nomeados de modulos padrao

print("Exemplo de importacao de um modulo padrao:")
import math
#raiz_quadrada = math.sqrt(25)

#Como boa pratica utilçizamos somente a parte de codigo que nos interessa internamente a função neste caso math (aplicacoes matematicas) substituindo na declaracao da variavel
from math import sqrt
raiz_quadrada = sqrt(25)


print(f"Raiz quadrada de 25: { raiz_quadrada}") #Imprimindo o valor da raiz quadrada (raiz_quadrada)


print("\n Exemplo de importacao de um modulo padrao:")
#utilizando outros modulos
import meu_modulo

mensagem = meu_modulo.saudacao("Gabriel")
resultado_dobro = meu_modulo.dobro(5)
print(mensagem)
print(f"Dobro de 5: {resultado_dobro}")

#Realizando a partir do metodo from
from meu_modulo import saudacao, dobro
