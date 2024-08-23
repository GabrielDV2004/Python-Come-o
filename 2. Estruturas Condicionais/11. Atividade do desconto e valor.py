import os
os.system("cls || clear") # Limpa o terminal

def calcular_valor_final(valor, pagamento, parcelas=None):
    if pagamento.lower() == 'à vista':
        # Aplicando desconto de 10%
        desconto = valor * 0.10
        valor_final = valor - desconto
        return valor_final
    elif pagamento.lower() == 'a prazo':
        if parcelas is not None:
            # Calcula o valor de cada parcela
            valor_parcela = valor / parcelas
            return valor, valor_parcela
        else:
            return "Número de parcelas não informado."
    else:
        return "Forma de pagamento inválida."

def main():
    try:
        # Solicita o valor do produto
        valor = float(input("Informe o valor do produto: R$ "))
        
        # Solicita a forma de pagamento
        pagamento = input("Informe a forma de pagamento (à vista ou a prazo): ").strip()
        
        if pagamento.lower() == 'a prazo':
            # Solicita a quantidade de parcelas se o pagamento for a prazo
            parcelas = int(input("Informe a quantidade de parcelas: "))
            resultado = calcular_valor_final(valor, pagamento, parcelas)
            if isinstance(resultado, tuple):
                valor_total, valor_parcela = resultado
                print(f"Valor total do produto: R$ {valor_total:.2f}")
                print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
            else:
                print(resultado)
        else:
            resultado = calcular_valor_final(valor, pagamento)
            if isinstance(resultado, float):
                print(f"Valor com desconto: R$ {resultado:.2f}")
            else:
                print(resultado)
                
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico para o produto e um número inteiro para parcelas.")

if __name__ == "__main__":
    main()
