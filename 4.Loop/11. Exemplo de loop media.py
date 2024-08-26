import os

os.system("cls || clear") # Limpa o terminal

soma = 0
for i in range(4):
    nota = int(input(f"Digite sua {i+1}º nota: "))
    soma = soma + nota
    media = soma /4

print(f"Sua média foi: {media} ")    

