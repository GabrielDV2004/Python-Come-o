import os
os.system("cls || clear") # Limpa o terminal

print("""
+ para somar
- para subtração
* para multiplicação
/ para divisão
      """)

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
opcao =input("Digite uma opção: ")

resultado = 0

match(opcao):
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Opção invalida")

print(f"Resultado: {resultado}")

print,("=== FIM ===")