#Para utilizacao desta aula foi instalado o pacote de requests via terminal onde 
# o comando era o pip install requests

print("\nImportação e o uso de um modulo de teceiros")
import requests

url = "https://www.example.com"
#Uttiliza o comando para pegar a url atraves do requests
response = requests.get(url)
#Status da requisiscao
print(f"Solicitacao HTTP para {url}: {response.status_code}") #Imprimindo o status da requisiscao (response.status_code)