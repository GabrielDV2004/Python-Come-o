import os
os.system("cls || clear") # Limpa o terminal

def calcular_peso_ideal(sexo, altura):
    """
    Calcula o peso ideal com base no sexo e altura do usuário.
    
    :param sexo: 'M' para masculino ou 'F' para feminino
    :param altura: Altura do usuário em metros
    :return: Peso ideal calculado
    """
    if sexo.upper() == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo.upper() == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return "Sexo inválido. Por favor, informe 'M' para masculino ou 'F' para feminino."
    
    return peso_ideal

def main():
    try:
        # Solicita o sexo do usuário
        sexo = input("Informe seu sexo (M para masculino ou F para feminino): ").strip()
        
        # Solicita a altura do usuário
        altura = float(input("Informe sua altura em metros (por exemplo, 1.75): "))
        
        # Calcula o peso ideal
        resultado = calcular_peso_ideal(sexo, altura)
        
        if isinstance(resultado, str):
            print(resultado)  # Mensagem de erro
        else:
            print(f"Seu peso ideal é: {resultado:.2f} kg")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para a altura.")

if __name__ == "__main__":
    main()
