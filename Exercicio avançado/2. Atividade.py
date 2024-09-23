"""
Altere o algoritmo que acabou de criar e faça com que o usuario insira numeros inteiros
ate que seja inserido o numero 0
1- a quantidade de numero positivos que sao pares
2. a quantidade de numeros impares
3. a quantidade de numeros negativos
4. a quantidade de numeros inseridos
"""
import os
os.system("cls || clear")

# Inicializando contadores
quantidade_pares_positivos = 0
quantidade_impares = 0
quantidade_negativos = 0
quantidade_total = 0

print("Digite números inteiros (digite 0 para parar):")

while True:
    numero = int(input())
    
    # Dizendo que o numero 0 é pra parar o codiguin
    if numero == 0:
        break
    
    # Atualizando o total de números inseridos
    quantidade_total += 1

    # Verificando se o número é par e positivo
    if numero > 0 and numero % 2 == 0:
        quantidade_pares_positivos += 1
    
    # Verificando se o número é ímpar
    if numero % 2 != 0:
        quantidade_impares += 1
    
    # Verificando se o número é negativo
    if numero < 0:
        quantidade_negativos += 1

# Mostrando os resultados
print(f"Quantidade de números positivos que são pares: {quantidade_pares_positivos}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Quantidade total de números inseridos: {quantidade_total}")
