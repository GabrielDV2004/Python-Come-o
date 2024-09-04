"""
Enunciado: Escreva um programa que use um laço while para encontrar o primeiro número maior que 50 que seja divisível por 7. Exiba esse número.

Dica: Inicie com uma variável em 51 e use o operador % para verificar divisibilidade por 7. Continue até encontrar um número que satisfaça a condição.

"""
import os
os.system("cls || clear")

# Inicializa a variável com o primeiro número maior que 50
numero = 51

# Laço para encontrar o primeiro número maior que 50 divisível por 7
while True:
    if numero % 7 == 0:  # Verifica se o número é divisível por 7
        break  # Sai do laço se o número for divisível por 7
    numero += 1  # Incrementa o número para verificar o próximo

# Exibe o número encontrado
print("O primeiro número maior que 50 que é divisível por 7 é:", numero)
