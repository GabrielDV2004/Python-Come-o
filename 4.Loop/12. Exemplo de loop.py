import os

os.system("cls || clear") # Limpa o terminal

soma = 0
for i in range(3):
    nota = int(input(f"Digite sua {i+1}º nota: "))
    soma = soma + nota
    media = soma /3

print(f"Sua média foi: {media} ")
if media >= 7:
    print("Aprovado")
elif media < 4:  #else if
    print("Reprovado")
else:
    print("Recuperação")    

print("=== FIM ===")    


