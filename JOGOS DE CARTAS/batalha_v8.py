# batalha_v8.py (modo de teste isolado com classe Jogador atualizada)
import random
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

# 🔽 Sistema de batalha básico para testes standalone
def batalha(jogador, bot):
    print("\n🎮 Iniciando batalha de teste...\n")

    # 🔹 Comprar 5 cartas iniciais
    for _ in range(5):
        jogador.comprar_carta()
        bot.comprar_carta()

    # Exibe informações básicas
    print(f"{jogador.nome} - Vida: {jogador.vida} | Mana: {jogador.mana}")
    print(f"{bot.nome} - Vida: {bot.vida} | Mana: {bot.mana}")

    print("\n🖐️ Mão do jogador:")
    for i, carta in enumerate(jogador.mao, start=1):
        print(f"{i} - {carta.nome} | Mana: {carta.custo_mana}")

if __name__ == "__main__":
    jogador = Jogador("Deus do Debug")
    bot = Jogador("Eldrin", is_bot=True)

    # 🔧 Deck do Deus do Debug com cartas overpower
    for i in range(1, 11):
        jogador.deck.append(get_carta_by_id(f"Carta_Debug_{i}"))

    # 🔧 Deck padrão para o bot
    for _ in range(10):
        bot.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))

    batalha(jogador, bot)
