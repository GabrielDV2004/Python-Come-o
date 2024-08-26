import os

os.system("cls || clear") # Limpa o terminal

for i in range(5):
    numero = int(input(f"Digite {i+1}º número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")