import random

class Jogador:
    def __init__(self, nome, terreno_favorito, habilidade_especial=None, custo_habilidade=2, is_bot=False):
        self.nome = nome
        self.terreno_favorito = terreno_favorito
        self.habilidade_especial = habilidade_especial
        self.custo_habilidade = custo_habilidade
        self.is_bot = is_bot

        self.vida = 20
        self.mana = 3
        self.deck = []
        self.mao = []
        self.campo = [None] * 5
        self.habilidade_usada = False

    def comprar_carta(self):
        if self.deck:
            carta = self.deck.pop(0)
            self.mao.append(carta)
            if self.is_bot:
                print(f"🃏 {self.nome} comprou a carta: {carta.nome}")
        else:
            if self.is_bot:
                print(f"🃏 {self.nome} não tem mais cartas para comprar.")

    def invocar_carta(self, indice_mao, slot):
        if indice_mao < 0 or indice_mao >= len(self.mao):
            print("❌ Índice de carta inválido.")
            return False

        carta = self.mao[indice_mao]
        if self.mana < carta.custo_mana:
            print("❌ Mana insuficiente para invocar essa carta.")
            return False

        if self.campo[slot] is not None:
            print("❌ Já existe uma carta neste slot.")
            return False

        self.mana -= carta.custo_mana
        self.campo[slot] = carta
        self.mao.pop(indice_mao)
        print(f"✅ {self.nome} invocou {carta.nome} no slot {slot + 1}!")
        return True

    def restaurar_mana(self):
        self.mana = 3
        self.habilidade_usada = False

    def resetar_habilidades(self):
        """Reseta o controle de uso de habilidades no início de cada turno."""
        self.habilidade_usada = False

    def cartas_em_campo(self):
        return [c for c in self.campo if c is not None]

    def possui_cartas_em_campo(self):
        return any(c is not None for c in self.campo)

    def __str__(self):
        return f"{self.nome} — ❤️ {self.vida} | 🔷 Mana: {self.mana}"
