import os
os.system("cls || clear") # Limpa o terminal

#Verificando

while True:
      Login = str(input("Digite seu login: "))
      Senha = int(input("Digite sua senha: "))
      
      if Login == "gabriel@gmail.com" and Senha == 1234:
        print("BEM VINDO GOSTOSÃO!")
        break
      else:
        print("TA ERRADO OTARIO.")

