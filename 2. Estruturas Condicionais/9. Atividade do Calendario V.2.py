import os
os.system("cls || clear") # Limpa o terminal

# Função para determinar o tipo de dia
def verificar_dia(dia):
    if dia == 1 or dia == 7:
        return "Final de semana"
    elif 2 <= dia <= 6:
        return "Dia útil"
    else:
        return "Inválido"

# Solicita a entrada do usuário
try:
    dia = int(input("Digite um número inteiro representando um dia da semana (1 a 7): "))
    resultado = verificar_dia(dia)
    print(resultado)
except ValueError:
    print("Por favor, digite um número inteiro válido.")



print,("=== FIM ===")