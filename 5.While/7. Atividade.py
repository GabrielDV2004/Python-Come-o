import os
os.system("cls || clear") # Limpa o terminal

QUANTIDADE_NOTAS = 3 # isto é uma constante

soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite {i+1} nota: "))

        if nota < 0 or nota > 10:
            print("Nota Inválida! \nDigite Novamente...")
        else:
            soma = soma + nota #ou soma += nota
            break
print("""
1- "N"
      """)
Opção =(input("Deseja acrescentar mais uma Nota?: ")).upper()


match(Opção):
    case "N":
        QUANTIDADE_NOTAS = 4
        nota_adicional = float(input(f"Digite a 4 nota: "))
        media = (soma + nota_adicional) / QUANTIDADE_NOTAS
           

media = soma / QUANTIDADE_NOTAS

if media >= 7 :
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")        
