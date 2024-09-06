import os  

os.system("cls || clear")

""""
Crie um progama que leia 6 numeros e informe por meio
de uma função:
- Quantos numeros sao pares
- Quantos numeros sao impares

 """

def verificar_pares_impares():
    impares = 0
    pares = 0
    for i in range(6):
        numero = int(input(f"Digite o {i+1} numero: "))
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
    print(f"\nQuantidade de números pares: {pares}")
    print(f"Quantidade de números impares: {impares}")

verificar_pares_impares()
