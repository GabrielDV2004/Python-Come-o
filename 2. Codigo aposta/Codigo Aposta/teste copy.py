import requests
import time
import random

# Configurações do robô
API_KEY = '57ad0bf4a84fc66e839f1a02a476f2 90'  # Corrija a chave da API
BASE_URL = 'https://api.the-odds-api.com'  # Confirme que a URL está correta
MONTANTE_INICIAL = 1000  # Montante inicial para apostas
APOSTA_FIXA = 10  # Valor fixo para cada aposta

def obter_eventos():
    """
    Obtém a lista de eventos esportivos disponíveis para apostas.
    """
    url = f'{BASE_URL}/eventos'  # Verifique se esta URL está correta
    headers = {'Authorization': f'Bearer {API_KEY}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta exceções para erros HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Erro ao obter eventos: {e}')
        return []

def selecionar_evento(eventos):
    """
    Seleciona um evento aleatoriamente para apostar.
    """
    if not eventos:
        print('Nenhum evento disponível para apostar.')
        return None
    return random.choice(eventos)

def apostar(evento, valor):
    """
    Realiza uma aposta em um evento específico.
    """
    url = f'{BASE_URL}/apostar'  # Verifique se esta URL está correta
    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    data = {
        'evento_id': evento['id'],
        'valor': valor,
        'tipo_aposta': 'vitória',  # Tipo de aposta (ex: vitória, empate, derrota)
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(f'Aposta realizada com sucesso no evento {evento["nome"]}')
        return True
    except requests.exceptions.RequestException as e:
        print(f'Erro ao realizar aposta: {e}')
        return False

def gerenciar_banca(montante, ganho):
    """
    Atualiza a banca com base no ganho ou perda.
    """
    return montante + ganho

def main():
    montante = MONTANTE_INICIAL
    while montante > 0:
        eventos = obter_eventos()
        evento = selecionar_evento(eventos)
        if evento:
            sucesso = apostar(evento, APOSTA_FIXA)
            if sucesso:
                # Simulando ganho ou perda
                ganho = random.choice([-APOSTA_FIXA, APOSTA_FIXA * 2])  # Perde ou ganha o dobro
                montante = gerenciar_banca(montante, ganho)
                print(f'Novo montante: {montante}')
            time.sleep(10)  # Espera de 10 segundos antes da próxima aposta
        else:
            break

if __name__ == '__main__':
    main()
