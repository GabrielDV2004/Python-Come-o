"""
Enunciado:
Escreva um programa que utilize um laço for para multiplicar cada número de 1 a 6 por 3 e exibir o resultado.

Dica: Para cada número no intervalo de 1 a 6, multiplique-o por 3 e mostre o resultado da multiplicação.


"""

import os
os.system("cls || clear")

# Utiliza um laço for para iterar sobre os números de 1 a 6
for numero in range(1, 7):
    resultado = numero * 3  # Calcula o resultado da multiplicação
    print(f"{numero} x 3 = {resultado}")
