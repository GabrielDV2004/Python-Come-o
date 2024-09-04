"""
Enunciado: Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`).

Dica: Use um laço para cada linha e outro para cada coluna dentro da linha.


"""

import os
os.system("cls || clear")

# Número de linhas e colunas
num_linhas = 4
num_colunas = 6

# Laço para cada linha
for i in range(num_linhas):
    # Laço para cada coluna dentro da linha
    for i in range(num_colunas):
        print('*', end='')  # Imprime um asterisco sem quebrar a linha
    print()  # Quebra a linha após terminar uma linha de asteriscos
