import os
import time
os.system("cls || clear") # Limpa o terminal

print("=== MENU ===")
print("S - Inserir uma nota")
print("P - Ver quantas notas foram inseridas")
print("N - Caluclar média aritmética")

resposta = input("Deseja inserir uma nota: ").upper()

match resposta:
    case "S":
        nota = float(input("\nDigite uma nota: "))
        soma += nota
        quantidadeNotas += 1

    case "P":
        if quantidadeNotas == 0:
            print("Não foram inseridas notas. \n")
            input("Pressione uma tecla para continuar...")
            time.sleep(3)
        else:
            print(f"Quantidade de notas inseridas: {quantidadeNotas} \n")
            input("Pressioneuma tecla para continuar...")        

     case "N":
            if quantidadeNotas == 0:
                print("Não foram inseridas notas. \n")
            else:
                break

        case _:
            print("Opção inválida... \n")
            time.sleep(3)

media  = soma / quantidadeNotas

print(f"Média: {media}")
    

