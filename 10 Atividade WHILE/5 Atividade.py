"""
Enunciado: Desenvolva um programa que solicite ao usuário inserir um código de promoção para obter um desconto. O código correto é "PROMO2024". O usuário tem 3 tentativas para acertar o código. Se o código estiver correto, exiba uma mensagem de "Código aceito" e o desconto. Se o usuário errar o código nas 3 tentativas, exiba uma mensagem de "Código inválido".

Dica: Use uma variável para armazenar o código correto e um contador para as tentativas.


"""
import os
os.system("cls || clear")

# Código de promoção correto
codigo_correto = "PROMO2024"

# Número máximo de tentativas
tentativas_max = 3

# Laço para permitir até 3 tentativas
for tentativa in range(tentativas_max):
    # Solicita ao usuário para inserir o código de promoção
    codigo_usuario = input("Digite o código de promoção: ")
    
    # Verifica se o código está correto
    if codigo_usuario == codigo_correto:
        print("Código aceito! Você ganhou um desconto de 20%.")
        break  # Sai do laço se o código estiver correto
    else:
        # Informa ao usuário que o código está incorreto e mostra o número de tentativas restantes
        tentativas_restantes = tentativas_max - (tentativa + 1)
        if tentativas_restantes > 0:
            print(f"Código incorreto. Você tem {tentativas_restantes} tentativas restantes.")
        else:
            print("Código inválido. Você esgotou suas tentativas.")
