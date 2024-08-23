import os

os.system("cls || clear") # Limpa o terminal

# Solicitando dados
numero = int(input("Digite um número para a tabuada: "))

print(f"\nTabuada de multiplicação do número: {numero}")
for i in range(1,11):
    print(f"{numero} x {i} = {numero} * i")