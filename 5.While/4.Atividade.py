"""
Escreva um algoritmo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, Mostre a pergunta novamente.
Calcule e mostre a média aritmética do aluno.
"""



import os
os.system("cls || clear")
#Solicitando dados
soma = 0
while True:
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite Sua nota: "))
    soma = soma + nota1 + nota2
    media = soma /2
    
    if nota1 < 0 or nota2 > 10:
        print("\nA nota deve ser maior ou igual a 0 e Menor que 10")
    else:
        break

print(f"Nota: {media}")    