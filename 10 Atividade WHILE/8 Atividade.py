"""
Enunciado: Crie um programa para ajudar o usuário a acompanhar suas metas de estudo. O usuário define uma meta de horas de estudo e o programa deve permitir que o usuário insira o número de horas estudadas até que o total atinja ou exceda a meta. O programa deve  exibir o total de horas estudadas e o valor excedente.

Dica: Utilize um laço while para somar as horas de estudo até atingir a meta.

"""
import os
os.system("cls || clear")
# Solicita a meta de horas de estudo ao usuário
meta = float(input("Digite a meta de horas de estudo: "))

# Inicializa o total de horas estudadas
total_estudado = 0.0

# Laço para solicitar as horas estudadas até que o total atinja ou exceda a meta
while total_estudado < meta:
    horas = float(input("Digite o número de horas estudadas: "))
    total_estudado += horas  # Adiciona as horas estudadas ao total

# Calcula o valor excedente
excedente = total_estudado - meta

# Exibe o total de horas estudadas e o valor excedente
print(f"Total de horas estudadas: {total_estudado:.2f}")
print(f"Valor excedente: {excedente:.2f}" if excedente > 0 else "Você atingiu exatamente a meta.")
