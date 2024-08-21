import os
os.system("cls || clear") # Limpa o terminal

#Solicitando dados
numero1 = float(input("Digite seu primeiro número: "))
numero2 = float(input("Digite seu segundo número: "))

# Determinar o maior e o menor número
if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

# Escrever os números informados
print(f"Números informados: {numero1} e {numero2}")

# Escrever o maior e o menor número
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")