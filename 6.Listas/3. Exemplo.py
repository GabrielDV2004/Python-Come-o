import os  

os.system("cls || clear")

def calcular_media(primeiro_numero, segundo_numero):
    soma = primeiro_numero + segundo_numero
    resultado = soma / 2
    return resultado

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))

media = calcular_media(primeiro_numero, segundo_numero)

print*f"Média: {media}"