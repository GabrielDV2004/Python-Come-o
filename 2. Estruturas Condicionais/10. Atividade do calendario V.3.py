import os
os.system("cls || clear") # Limpa o terminal

print("""
1- Janeiro
2- Fevereiro
3- Março
4- Abril
5- Maio
6- Junho
7- Julho
8- Agosto
9- Setembro
10- Outubro
11- Novembro
12- Dezembro                          
      """)
Mes = (input("Digite um Numero para o Mês?: "))


match(Mes):
    case "1":
        print("Mês de Janeiro")
    case "2":
        print("Mês de Fevereiro")
    case "3":
        print("Mês de Março")
    case "4":
        print("Mês de Abril")
    case "5":
        print("Mês de Maio")
    case "6":
        print("Mês de Junho")
    case "7":
        print("Mês de Julho")
    case "8":
        print("Mês de Agosto")
    case "9":
        print("Mês de Setembro")
    case "10":
        print("Mês de Outubro")
    case "11":
        print("Mês de Novembro")
    case "12":
        print("Mês de Dezembro")
    case _:
        print("Opção invalida")


print,("=== FIM ===")