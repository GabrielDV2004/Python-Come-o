"""
Crie um algoritmo que aceite apenas 6 valores inteiros, posisitos e pares
em seguida, mostre na tela os valores lido sua ordem inversa.
caso seja informada um numero diferente dos criterios apresentados acima,
repita a pergunta para o usuario
"""
import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 3
lista_pares_positivos = []

#Entrada
print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    while True:
        numero = int(input(f"Digite o {i+1} número: "))

        #verificando se o numero é par e positivos
        if numero % 2 == 0 and numero > 0:
            lista_pares_positivos.append(numero)
            break
        else:
            print("Número inválido. \nTente Novamente. \n\n")
            
#Saida
print("\n=== Exibindo Resultados === ")
for i, numero in enumerate(reversed(lista_pares_positivos)):
    print(f"{len(lista_pares_positivos)-i} - {numero}")            
