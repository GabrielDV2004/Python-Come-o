"""
Enunciado: Desenvolva um programa que use um laço `for` para imprimir todos os números pares de 2 a 10.

Dica: Um número é par se ele é divisível por 2. Use o operador `%` para verificar se o número é par.

"""
import os
os.system("cls || clear")

# Utiliza um laço for para iterar sobre os números de 2 a 10
for numero in range(2, 11):
    # Verifica se o número é par
    if numero % 2 == 0:
        print(numero)
