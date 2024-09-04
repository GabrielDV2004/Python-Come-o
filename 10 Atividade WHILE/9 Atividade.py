"""
Enunciado: Crie um programa que peça ao usuário para inserir números inteiros até que a soma dos números ímpares inseridos seja maior que 200. O programa deve exibir o total de números ímpares inseridos e a soma desses números. 

Dica: Utilize um laço while para somar os números ímpares e contar quantos foram inseridos. Pare quando a soma exceder 200.
"""
import os
os.system("cls || clear")

# Inicializa a soma dos números ímpares e o contador de números ímpares
soma_impares = 0
contador_impares = 0

# Laço para solicitar números até que a soma dos ímpares exceda 200
while soma_impares <= 200:
    numero = int(input("Digite um número inteiro: "))
    
    # Verifica se o número é ímpar
    if numero % 2 != 0:
        soma_impares += numero  # Adiciona o número ímpar à soma
        contador_impares += 1  # Incrementa o contador de números ímpares

# Exibe o total de números ímpares e a soma desses números
print(f"Total de números ímpares inseridos: {contador_impares}")
print(f"Soma dos números ímpares: {soma_impares}")
