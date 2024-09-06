
import os  

os.system("cls || clear")

""""
 Crie funções que recebam 2 numeros e retorne
 a soma, subtração, divisão e a multiplicação,
 destes dois numeros informados

 """
def mostrar_tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um numero: "))

mostrar_tabuada(numero)