"""
Enunciado: Escreva um programa que calcule a soma dos números ímpares de 1 a 9 utilizando um laço `for`.

Dica: Verifique
se um número é ímpar usando o operador `%` e adicione esses números a uma
variável de soma


"""

import os
os.system("cls || clear")

# Inicializa a variável de soma
soma = 0

# Laço para iterar de 1 a 9
for i in range(1, 10):
    if i % 2 != 0:  # Verifica se o número é ímpar
        soma += i  # Adiciona o número ímpar à soma

# Exibe o resultado
print("A soma dos números ímpares de 1 a 9 é:", soma)
