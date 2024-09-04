"""
Enunciado: Crie um programa que ajude um usuário a controlar seus gastos mensais. O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. O programa deve exibir o total gasto e o valor  excedente.

Dica: Defina um orçamento e use um laço while para somar os gastos diários. Pare quando o total gasto exceder o orçamento.
"""
import os
os.system("cls || clear")

# Solicita o orçamento inicial ao usuário
orcamento = float(input("Digite o orçamento inicial para o mês: "))

# Inicializa o total gasto e o valor excedente
total_gasto = 0.0

# Laço para somar os gastos diários até que o total exceda o orçamento
while total_gasto <= orcamento:
    gasto_diario = float(input("Digite o gasto diário: "))
    total_gasto += gasto_diario  # Atualiza o total gasto

# Calcula o valor excedente
excedente = total_gasto - orcamento

# Exibe o total gasto e o valor excedente
print(f"Total gasto no mês: {total_gasto:.2f}")
print(f"Valor excedente: {excedente:.2f}")
