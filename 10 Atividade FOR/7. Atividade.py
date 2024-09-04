"""
Enunciado: Crie um programa que use um laço `for` para gerar e exibir os quadrados dos números de 1 a 5 (ou seja, 1², 2², 3², etc.).

Dica: O quadrado de um número é o número multiplicado por ele mesmo.



"""

import os
os.system("cls || clear")

# Loop para gerar e exibir os quadrados dos números de 1 a 5
for i in range(1, 6):  # range(1, 6) gera os números de 1 a 5
    quadrado = i ** 2  # Calcula o quadrado do número i
    print(f"O quadrado de {i} é {quadrado}")  # Exibe o resultado
