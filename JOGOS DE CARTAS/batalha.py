import random

# Classe Carta
class Carta:
    def __init__(self, nome, custo_mana, ataque, defesa, habilidade, custo_habilidade):
        self.nome = nome
        self.custo_mana = custo_mana
        self.ataque = ataque
        self.defesa = defesa
        self.habilidade = habilidade
        self.custo_habilidade = custo_habilidade
        self.em_campo = False

# Classe Jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mana = 0
        self.turno = 0
        self.vida = 20
        self.deck = []
        self.mao = []
        self.campo = [None, None, None, None]  # 4 slots de campo

    def ganhar_mana(self):
        ganho_por_turno = [1, 3, 5, 6, 7, 8, 9, 10]
        if self.turno < len(ganho_por_turno):
            self.mana = ganho_por_turno[self.turno]
        else:
            self.mana = 10
        self.turno += 1

    def comprar_carta(self):
        if self.deck:
            carta = self.deck.pop(0)
            self.mao.append(carta)
            print(f"{self.nome} comprou a carta: {carta.nome}")
        else:
            print(f"{self.nome} não tem mais cartas no deck!")

    def jogar_carta(self, indice_carta, slot):
        if indice_carta >= len(self.mao):
            print("Índice de carta inválido.")
            return
        carta = self.mao[indice_carta]
        if self.mana >= carta.custo_mana and self.campo[slot] is None:
            self.mana -= carta.custo_mana
            self.campo[slot] = carta
            carta.em_campo = True
            self.mao.pop(indice_carta)
            print(f"{self.nome} jogou {carta.nome} no slot {slot+1}.")
        else:
            print(f"{self.nome} não conseguiu jogar a carta.")

    def atacar(self, slot, oponente):
        carta = self.campo[slot]
        if carta:
            dano = carta.ataque
            print(f"{self.nome} ataca com {carta.nome} causando {dano} de dano ao oponente!")
            oponente.vida -= dano
        else:
            print("Slot vazio, ataque impossível.")

    def usar_habilidade(self, slot):
        carta = self.campo[slot]
        if carta and self.mana >= carta.custo_habilidade:
            self.mana -= carta.custo_habilidade
            print(f"{self.nome} usou a habilidade de {carta.nome}: {carta.habilidade}")
        else:
            print("Não foi possível usar a habilidade.")

def criar_deck_exemplo():
    return [
        Carta("Goblin Selvagem", 2, 2, 1, "Investida: +1 ATK", 1),
        Carta("Troll das Rochas", 5, 4, 5, "Regenerar: Recupera 2 de vida", 2),
        Carta("Dragão da Montanha", 7, 6, 5, "Sopro Flamejante: Causa 3 de dano em todas as criaturas inimigas", 3),
        Carta("Elemental de Lava", 4, 5, 3, "Explosão de Lava: +2 ATK por 1 turno", 2),
    ] * 3  # Multiplicando para ter mais cartas

# Loop de batalha
def batalha(jogador1, jogador2):
    while jogador1.vida > 0 and jogador2.vida > 0:
        for jogador, oponente in [(jogador1, jogador2), (jogador2, jogador1)]:
            print(f"\n=== Turno de {jogador.nome} ===")
            jogador.ganhar_mana()
            jogador.comprar_carta()
            print(f"Mana atual: {jogador.mana}")
            print(f"Vida: {jogador.vida}")

            # Exibir mão
            for idx, carta in enumerate(jogador.mao):
                print(f"[{idx}] {carta.nome} (Custo: {carta.custo_mana} | ATK: {carta.ataque} | DEF: {carta.defesa})")

            # Jogar primeira carta possível
            for idx, carta in enumerate(jogador.mao):
                for slot in range(4):
                    if jogador.mana >= carta.custo_mana and jogador.campo[slot] is None:
                        jogador.jogar_carta(idx, slot)
                        break

            # Atacar com todas as cartas no campo
            for slot in range(4):
                if jogador.campo[slot]:
                    jogador.atacar(slot, oponente)

            # Verificar fim de jogo
            if oponente.vida <= 0:
                print(f"\n{jogador.nome} venceu a partida!")
                return

# Iniciar o jogo
jogador1 = Jogador("Player 1")
jogador2 = Jogador("Player 2")

# Criando decks
jogador1.deck = criar_deck_exemplo()
jogador2.deck = criar_deck_exemplo()

# Embaralhando os decks
random.shuffle(jogador1.deck)
random.shuffle(jogador2.deck)

# Começar batalha
batalha(jogador1, jogador2)
