import os
os.system("cls || clear") # Limpa o terminal

peso_ideal = 0
# Solicitando dados

altura = float(input("Digite sua altura: "))

sexo = input("Digite seu sexo (M ou F): ")

#Verificando
match sexo:
    case "M" | "m":
        peso_ideal = (72.7 * altura) -58
    case "F"  | "f":
        peso_ideal = (62.1 * altura) -44.7
    case _:
        print("Opção invalida")

print(f"Sexo: {sexo}")
print(f"Peso ideal: {peso_ideal:.2f}")           