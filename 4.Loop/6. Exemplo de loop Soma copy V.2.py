import os

os.system("cls || clear") # Limpa o terminal

soma = 0
for i in range(5):
    numero = int(input(f"Digite {i+1}º número: "))
    soma = soma + numero

print(f"Soma: {soma} ")    

