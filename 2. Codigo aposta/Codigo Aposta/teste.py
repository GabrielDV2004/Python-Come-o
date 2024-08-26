import os

os.system("sls || clear") # Limpa o terminal

import random

# Função para prever o resultado de uma partida
def prever_resultado(equipe1, equipe2, estatisticas):
    """
    Prevê o resultado de uma partida entre equipe1 e equipe2 com base nas estatísticas fornecidas.
    
    Parameters:
    equipe1 (str): Palmeiras
    equipe2 (str): Cuiabá
    estatisticas (dict): Dicionário contendo estatísticas das equipes
    
    Returns:
    str: Resultado previsto da partida
    """
    
    # Estatísticas das equipes
    v1, e1, d1 = estatisticas[equipe1]
    v2, e2, d2 = estatisticas[equipe2]
    
    # Probabilidades baseadas nas taxas de vitória
    prob_vitoria1 = v1 / (v1 + v2 + e1 + e2 + d1 + d2)
    prob_vitoria2 = v2 / (v1 + v2 + e1 + e2 + d1 + d2)
    prob_empate = (e1 + e2) / (v1 + v2 + e1 + e2 + d1 + d2)
    
    # Ajuste as probabilidades para somarem 1
    total_prob = prob_vitoria1 + prob_vitoria2 + prob_empate
    prob_vitoria1 /= total_prob
    prob_vitoria2 /= total_prob
    prob_empate /= total_prob
    
    # Sorteia o resultado baseado nas probabilidades ajustadas
    resultado = random.choices(
        ['Vitória Clube Atlético Mineiro', 'Fluminense', 'Empate'],
        [prob_vitoria1, prob_vitoria2, prob_empate]
    )[0]
    
    return resultado

# Estatísticas de exemplo
estatisticas = {
    'EquipeA': (10, 5, 3),  # (vitórias, empates, derrotas)
    'EquipeB': (8, 6, 4)
}

# Nome das equipes
equipe1 = 'EquipeA'
equipe2 = 'EquipeB'

# Previsão
resultado = prever_resultado(equipe1, equipe2, estatisticas)
print(f'O resultado previsto para o jogo entre {equipe1} e {equipe2} é: {resultado}')
