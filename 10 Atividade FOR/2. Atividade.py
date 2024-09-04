"""
Enunciado: Crie um programa que, utilizando um laço `for`, calcule a soma dos números de 1 a 5 e mostre o resultado.

Dica: Você pode criar uma variável para armazenar a soma e adicionar a ela o valor de cada número a cada iteração.

"""
import os
os.system("cls || clear")

# Inicializa a variável que armazenará a soma
soma = 0

# Utiliza um laço for para iterar sobre os números de 1 a 5
for numero in range(1, 6):
    soma += numero  # Adiciona o valor atual à soma

# Exibe o resultado da soma
print("A soma dos números de 1 a 5 é:", soma)


