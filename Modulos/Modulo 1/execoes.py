print("Exemplo de captura de exceção")
#tenta realizar o bloco de codigo
try:
    numero = int(input("Digite um numero inteiro "))
    resultado = 10 / numero 
except ValueError as e:
    print(f"Ocorreu um value erro: {e}")
 #O raise function planca o erro da maneira desejada permitindo que catregorize de maneira personalizada 
    raise ValueError("Tipo de variaveis imcompativeis")
except ZeroDivisionError as e:
    print(f"Ocorreu um erro de divisão por zero: {e}")
#Caputra o erro de maneira generica
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#Se ultizina em caso de sucesso
else:
    print(f"Resultado {resultado}")
#Aparece independende to resultado
finally:
    print("Operacao  finalizada")

