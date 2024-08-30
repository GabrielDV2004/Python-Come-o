import os
os.system("cls || clear") # Limpa o terminal

login_salvo = input("Crie Seu Login: ")
senha_salvo = input("Crie sua senha: ")
contador = 0

while True:
    contador += 1
    login = input("Escreva seu Login: ")
    senha = input("Escreva sua senha: ")

    if login == login_salvo and senha == senha_salvo:
        print("Bem vindo Delicia!!!")
        break
    elif contador > 3:
        break
    else:
        
        print("Senha ou login incorretos, tente novamente.")