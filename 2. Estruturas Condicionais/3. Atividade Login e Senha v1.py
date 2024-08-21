import os
os.system("cls || clear") # Limpa o terminal


#Solicitando dados
Login = str(input("Digite seu login: "))
Senha = int(input("Digite sua senha: "))

#Verificando
if Login == "gabriel@gmail.com" and Senha == 1234:
        print("BEM VINDO GOSTOSÃO!")
else:
        print("TA ERRADO OTARIO.")

