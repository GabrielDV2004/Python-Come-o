import os
os.system("cls || clear") # Limpa o terminal

#Solicitando dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))    
nota3 = float(input("Digite sua terceira nota: "))

#calculando
media = (nota1 + nota2 + nota3) /3

#Exibindo dados ao Usuario

print(f"\nSeu Nome é: {nome}")
print(f"Sua Idade é: {idade}")
print(f"Sua Média final é: {media}")

if media <= 7:
    print("REPROVADO.")
else:
    print("APROVADO")
