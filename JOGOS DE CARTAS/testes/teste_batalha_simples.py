# testes/teste_batalha_simples.py

import sys
import os

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from batalha.motor import batalha
from jogador_global import carregar_jogador
from herois.gerenciador_heroi import carregar_heroi
  # Corrija o caminho se o arquivo estiver em outro lugar

# Simula um jogador e um inimigo com decks simples
def mock_inimigo():
    class Inimigo:
        def __init__(self):
            self.nome = "Goblin Tester"
            self.vida = 20
            self.mana = 0
            self.mao = []
            self.campo = [None] * 5
            self.deck = ['Carta_1', 'Carta_2', 'Carta_3', 'Carta_4', 'Carta_5'] * 2

        def comprar_carta(self):
            if self.deck:
                carta_id = self.deck.pop(0)
                from cartas.card_repository import get_carta_by_id
                carta = get_carta_by_id(carta_id)
                self.mao.append(carta)

    return Inimigo()

if __name__ == "__main__":
    jogador_dados = carregar_jogador()
    heroi = carregar_heroi("Thorin")  # ou outro herói existente
    jogador = heroi
    jogador.vida = 20
    jogador.mana = 0
    jogador.mao = []
    jogador.campo = [None] * 5
    jogador.deck = ['Carta_1', 'Carta_2', 'Carta_3', 'Carta_4', 'Carta_5'] * 2

    inimigo = mock_inimigo()

    batalha(jogador, inimigo)
