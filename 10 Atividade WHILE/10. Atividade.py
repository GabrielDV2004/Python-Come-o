"""

Enunciado: Crie um programa que permita ao usuário registrar o número de calorias consumidas em cada refeição. O programa deve continuar registrando as calorias até que o total de calorias consumidas ultrapasse 2000 calorias. Após exceder 2000 calorias, exiba o total de calorias consumidas e o excesso.

Dica: Use um laço while para somar as calorias e parar quando o total for maior que 2000. Exiba o total e o excesso de calorias.
"""
import os
os.system("cls || clear")

# Inicializa o total de calorias consumidas
total_calorias = 0.0

# Laço para solicitar as calorias até que o total exceda 2000
while total_calorias <= 2000:
    calorias = float(input("Digite o número de calorias consumidas na refeição: "))
    total_calorias += calorias  # Adiciona as calorias consumidas ao total

# Calcula o excesso de calorias
excesso = total_calorias - 2000

# Exibe o total de calorias e o excesso
print(f"Total de calorias consumidas: {total_calorias:.2f}")
print(f"Excesso de calorias: {excesso:.2f}")
