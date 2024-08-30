import os
os.system("cls || clear") # Limpa o terminal

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador += 1
    soma += nota

    resposta = input("Deseja acrescentar mais uma nota? ").upper()
    #resposta = resposta.upper() Converte em maiusculo
    
    if resposta == "N":
        break

media = soma / contador
print(f"Média {media}")