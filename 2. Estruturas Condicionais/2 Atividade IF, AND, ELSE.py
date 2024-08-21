import os
os.system("cls || clear") # Limpa o terminal

#Solicitando dados
numero1 = float(input("Digite seu primeiro número: "))
numero2 = float(input("Digite seu segundo número: "))

soma = numero1 + numero2
produto = numero1 * numero2
media = (numero1 + numero2) / 2

#Exibindo dados
if numero1 > numero2:
    print(f"{numero1} é maior. {numero2} é menor")
else:
    print(f"{numero2} é maior. {numero1} é menor")

#Exibindo na tela:
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Media: {media}")




