"""

Enunciado: Crie um programa que ajude um estudante a calcular a média de suas notas. O programa deve permitir que o usuário insira notas de provas até que o usuário insira um valor negativo. O programa deve calcular e exibir a média das notas inseridas.

Dica: Use um laço while para continuar solicitando notas até que uma nota negativa seja inserida. Calcule a média dividindo a soma das notas pelo número de notas.

"""
import os
os.system("cls || clear")

# Inicializa a soma das notas e o contador de notas
soma_notas = 0.0
contador_notas = 0

# Laço para solicitar notas até que uma nota negativa seja inserida
while True:
    nota = float(input("Digite a nota (ou um valor negativo para encerrar): "))
    
    if nota < 0:
        break  # Sai do laço se a nota for negativa
    
    soma_notas += nota  # Adiciona a nota à soma total
    contador_notas += 1  # Incrementa o contador de notas

# Calcula e exibe a média das notas
if contador_notas > 0:
    media = soma_notas / contador_notas
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
