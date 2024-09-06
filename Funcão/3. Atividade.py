
import os  

os.system("cls || clear")

""""
Crie uma função que receba um numero e mostre uma 
mensagem informando se o numero é par ou impar

 """

print("\n = = = Solicitando dados = = =" )

primeiro_numero = int(input("Digite um numero: "))

def verificar_par_impar(primeiro_numero):
    if primeiro_numero % 2 == 0:
        print(f"O número {primeiro_numero} é par.")
    else:
        print(f"O número {primeiro_numero} é ímpar.")

resposta = verificar_par_impar(primeiro_numero)        

