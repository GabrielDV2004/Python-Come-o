import os
import time

os.system("cls || clear") # Limpa o terminal

numero = int(input("Digite o número: "))

for i in range(numero,0,-1):
    print(f"Conteudo da variavel i = {i}") #print(i)
    time.sleep(1) #vai esperar 2 segundos    

print("=== FIM ===")    