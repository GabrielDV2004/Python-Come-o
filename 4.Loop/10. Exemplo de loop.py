import os
os.system("cls || clear") # Limpa o terminal

pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"Digite {i+1}º número: ")) 
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Quantidade de Pares: {pares}")    
print(f"Quantidade de ímpares: {impares}")    