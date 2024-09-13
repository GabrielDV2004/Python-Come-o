""""
 Crie funções que recebam 2 numeros e retorne
 a soma, subtração, divisão e a multiplicação,
 destes dois numeros informados

 """

import os  

os.system("cls || clear")

print("\n = = = Solicitando dados = = =" )

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))

import os  

os.system("cls || clear")

def calcular_soma(primeiro_numero, segundo_numero):    
    soma = primeiro_numero + segundo_numero
    #Tem como colocar print(f"(soma: {soma}")
    return soma

def calcular_subtracao(primeiro_numero, segundo_numero):
    subtracao = primeiro_numero - segundo_numero
    return subtracao
 
def calcular_multiplicacao(primeiro_numero, segundo_numero):
    multiplicacao = primeiro_numero * segundo_numero
    return multiplicacao

def calcular_divisao(primeiro_numero, segundo_numero):
    divisao = primeiro_numero / segundo_numero
    divisao = soma/2    
    return divisao



print("\n = = = Exibindo Dados = = =" )

soma = calcular_soma(primeiro_numero,segundo_numero)
print(f"soma: {soma}")

subtracao = calcular_subtracao(primeiro_numero,segundo_numero)
print(f"Subtração: {subtracao}")

multiplicacao = calcular_multiplicacao(primeiro_numero,segundo_numero)
print(f"Multiplicação: {multiplicacao}")

divisao = calcular_divisao(primeiro_numero,segundo_numero)
print(f"Divisão: {divisao}")

