import os  

os.system("cls || clear")

#Função com retorno.

def calcular_media(numero1, numero2):
    # Calcula a média dos dois números
    media = (numero1 + numero2) / 2
    
    # Mostra a mensagem com a média
    print(f"A média dos números {numero1} e {numero2} \né: {media}")

# Exemplo de uso da função
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

calcular_media(numero1, numero2)
