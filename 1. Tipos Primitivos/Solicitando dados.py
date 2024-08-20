import os

os.system("cls || clear") # Limpa o terminal

#Solicitando dados.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade "))
altura = float(input("Digite sua altura: "))

#Exibindo dados.
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} metros.")