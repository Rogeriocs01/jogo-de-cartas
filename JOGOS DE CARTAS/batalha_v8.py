# batalha_v8.py (modo de teste isolado)
import random
from batalha.motor import batalha
from card_repository import get_carta_by_id

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 20
        self.mana = 3
        self.deck = []
        self.mao = []
        self.campo = [None] * 5
        self.terreno_favorito = terreno_favorito
        self.terreno_favorito = None
        self.is_bot = False
        self.habilidade_especial = None
        self.custo_habilidade = 0
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
    jogador = Jogador("Jogador")
    bot = Jogador("Bot")
    bot.is_bot = True

    for _ in range(10):
        jogador.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))
        bot.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))

    batalha(jogador, bot)
