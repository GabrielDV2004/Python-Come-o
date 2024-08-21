import os
os.system("cls || clear") # Limpa o terminal

print("""
1- Domingo
2- SEGUNDA
3- TERÇA
4- QUARTA
5- QUINTA
6- SEXTA
7- SABADO  
      """)
Opção =(input("Qual diada semana?: "))


match(Opção):
    case "1":
        print("Domingo Final de Semana")
    case "2":
        print("Segunda-Feira Dia Útil")
    case "3":
        print("Terça-Feira Dia Útil")
    case "4":
        print("Quarta-Feira Dia Útil")
    case "5":
        print("Quinta-Feira Dia Útil")
    case "6":
        print("Sexta-Feira Dia Útil")
    case "7":
        print("Sabado Final de Semana")
    case _:
        print("Opção invalida")


print,("=== FIM ===")