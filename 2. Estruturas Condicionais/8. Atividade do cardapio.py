import os
os.system("cls || clear") # Limpa o terminal

print("""
1- Para Picanha - 25,00
2- Para Lasanha - 20,00
3- Para Strognoff - 15,00
4- Para Bife Acebolado - 10,00
5- Para Pão com ovo - 5,00     
      """)
Codigo_Prato =(input("Digite o Código do seu Prato: "))



resultado = 0

match(Codigo_Prato):
    case "1":
        print("Picanha R$ 25,00")
    case "2":
        print("Lasanha R$20,00")
    case "3":
        print("strognoff R$15,00")
    case "4":
        print("Bife Acebolado R$10,00")
    case "5":
        print("Pão com Ovo R$5,00")
    case _:
        print("Opção invalida")


print,("=== FIM ===")