"""
Enunciado: Escreva um programa que use um laço `for` para imprimir as letras de 'A' a 'E'.

Dica: Utilize a representação numérica das letras (códigos ASCII) e incremente o valor para passar de uma letra para a próxima.



"""

import os
os.system("cls || clear")

# Laço para imprimir as letras de 'A' a 'E'
for i in range(ord('A'), ord('F')): 
    letra = chr(i)  # Converte o código
    print(letra)  # Imprime a letra
