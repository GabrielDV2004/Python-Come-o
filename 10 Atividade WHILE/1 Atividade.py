"""

Enunciado: Desenvolva um programa que conte quantos números negativos foram inseridos pelo usuário usando um laço while. O programa deve parar quando o usuário inserir 0 ou um número positivo. Mostre a quantidade de números negativos.

Dica: Utilize uma variável para contar os números negativos e continue solicitando números até que um número positivo ou 0 seja inserido.

"""
import os
os.system("cls || clear")

# Inicializa a variável para contar números negativos
contagem_negativos = 0

while True:
    # Solicita ao usuário para inserir um número
    numero = float(input("Digite um número (ou um número positivo/0 para parar): "))
    
    # Verifica se o número é 0 ou positivo
    if numero >= 0:
        break  # Sai do laço se o número for 0 ou positivo
    
    # Incrementa a contagem se o número for negativo
    if numero < 0:
        contagem_negativos += 1

# Exibe a quantidade de números negativos
print("Quantidade de números negativos inseridos:", contagem_negativos)
