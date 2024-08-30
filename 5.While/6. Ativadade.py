import os
os.system("cls || clear") # Limpa o terminal

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Digite uma nota: "))
        if nota >= 0 and nota <= 10:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS
print(f"Media: {media}")

if media >= 7:
    print("Parabéns, você está aprovado!")
elif media >= 5 and media < 7:
    print("Infelizmente você não consegiu atingir a nota esperada. Recuperação")
elif media < 5:
    print("Sinto muito. Reprovado")
