# batalha_v8.py (modo de teste isolado com classe Jogador atualizada)
import random
from batalha.motor import batalha
from card_repository import get_carta_by_id

class Jogador:
    def __init__(self, nome, terreno_favorito=None, is_bot=False, habilidade_especial=None, custo_habilidade=0):
        self.nome = nome
        self.vida = 20
        self.mana = 3
        self.deck = []
        self.mao = []
        self.campo = [None] * 5
        self.terreno_favorito = terreno_favorito
        self.is_bot = is_bot
        self.habilidade_especial = habilidade_especial
        self.custo_habilidade = custo_habilidade
        self.habilidade_heroi_usada = False

    def comprar_carta(self):
        if self.deck:
            carta = self.deck.pop(0)
            self.mao.append(carta)
            print(f"🃏 {self.nome} comprou a carta: {carta.nome}")

    def resetar_habilidades(self):
        for carta in self.campo:
            if carta:
                carta.habilidade_usada = False

if __name__ == "__main__":
    jogador = Jogador("Player 1")
    bot = Jogador("Player 2", is_bot=True)

    for _ in range(10):
        jogador.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))
        bot.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))

    batalha(jogador, bot)
