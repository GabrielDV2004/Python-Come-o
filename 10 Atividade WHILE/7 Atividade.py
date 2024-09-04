"""
Enunciado: Crie um programa que solicite ao usuário criar uma senha. O programa deve então pedir para confirmar a senha e garantir que ambas as senhas coincidam. Se as senhas não coincidirem, o programa deve continuar pedindo para o usuário inserir e confirmar a  tenha até que ambas sejam iguais.

Dica: Utilize variáveis para armazenar a senha e a confirmação, e um laço while para verificar se as duas senhas coincidem.


"""
import os
os.system("cls || clear")

# Laço para solicitar e confirmar a senha até que ambas coincidam
while True:
    # Solicita a criação da senha
    senha = input("Crie uma senha: ")
    # Solicita a confirmação da senha
    confirmacao = input("Confirme a senha: ")

    # Verifica se as senhas coincidem
    if senha == confirmacao:
        print("Senha confirmada com sucesso!")
        break  # Sai do laço se as senhas coincidirem
    else:
        print("As senhas não coincidem. Tente novamente.")
