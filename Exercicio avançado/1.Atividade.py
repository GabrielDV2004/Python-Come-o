"""
Crie um algoritmo que leia 5 numeros inteiros e, em seguida, mostre na tela:
1- a quantidade de numeros pares
2. a quantidade de numeros impares
3. a quantidade de numeros positivos
4. a quantidade de numeros negativos
"""
import os
os.system("cls || clear")

pares = 0
impares = 0
positivos = 0
negativos = 0

#Pedindo os numeros

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))

#Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Verifica se o número é positivo ou negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1



#Mostrando os resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números Positivos: {positivos}")
print(f"Quantidade de números Positivos: {negativos}")