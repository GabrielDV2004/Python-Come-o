"""

Enunciado: Escreva um programa que multiplique um número inicial por um fator dado pelo usuário até que o produto exceda 100. Exiba o produto final e o número de multiplicações realizadas.

Dica: Use uma variável para o produto e outra para contar as multiplicações. Continue multiplicando o número pelo fator até que o produto seja maior que 100.

"""
import os
os.system("cls || clear")

# Solicita o número inicial e o fator ao usuário
numero_inicial = float(input("Digite o número inicial: "))
fator = float(input("Digite o fator de multiplicação: "))

# Inicializa o produto com o número inicial e o contador de multiplicações
produto = numero_inicial
contador_multiplicacoes = 0

# Laço para multiplicar até que o produto exceda 100
while produto <= 100:
    produto *= fator  # Multiplica o produto pelo fator
    contador_multiplicacoes += 1  # Incrementa o contador de multiplicações

# Exibe o produto final e o número de multiplicações realizadas
print(f"Produto final: {produto}")
print(f"Número de multiplicações realizadas: {contador_multiplicacoes}")
