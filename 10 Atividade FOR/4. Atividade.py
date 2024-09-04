Enunciado: Escreva
um programa que use um laço `for` para exibir a tabuada do 2, de 2 até 20.

Dica: Para cada valor de 1 a 10, multiplique por 2 e exiba o resultado. 
import os

os.system("cls || clear") # Limpa o terminal

print("\nTabuada de soma do número: 2")
for i in range(1,21):
    print(f"{2} + {i} = {2 + i}")

print("\nTabuada de Multiplicação do número: 2")
for i in range(1,21):
    print(f"{2} * {i} = {2 * i}")

print("\nTabuada de Divisão do número: 2")    
for i in range(1,21):
    print(f"{7} / {i} = {7 / i}")

print("\nTabuada de Subtração do número: 2")    
for i in range(1,21):
    print(f"{2} - {i} = {2 - i}")
