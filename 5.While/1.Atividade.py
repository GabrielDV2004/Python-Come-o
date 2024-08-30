import os
os.system("cls || clear")
#Solicitando dados
while True:
    nota = float(input("Digite sua nota: "))
    
    if nota < 0 or nota > 10:
        print("\nA nota deve ser maior ou igual a 0 e Menor que 10")
    else:
        break

print(f"Nota: {nota}")    