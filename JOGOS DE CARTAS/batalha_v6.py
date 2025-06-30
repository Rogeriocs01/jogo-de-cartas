import random

LIMITE_MAO = 5

class Carta:
    def __init__(self, nome, custo_mana, ataque, defesa, habilidade, custo_habilidade, tipo_habilidade=None, efeito_habilidade=None, efeito_morte=None):
        self.nome = nome
        self.custo_mana = custo_mana
        self.ataque = ataque
        self.defesa = defesa
        self.habilidade = habilidade
        self.custo_habilidade = custo_habilidade
        self.tipo_habilidade = tipo_habilidade  # "cura", "dano_direto", etc.
        self.efeito_habilidade = efeito_habilidade
        self.efeito_morte = efeito_morte
        self.em_campo = False

    def resumo(self):
        return f"{self.nome} (ATK:{self.ataque} DEF:{self.defesa})"

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mana = 0
        self.turno = 0
        self.vida = 20
        self.deck = []
        self.mao = []
        self.campo = [None, None, None, None]

    def ganhar_mana(self):
        ganho_por_turno = [1, 3, 5, 6, 7, 8, 9, 10]
        if self.turno < len(ganho_por_turno):
            self.mana = ganho_por_turno[self.turno]
        else:
            self.mana = 10
        self.turno += 1

    def comprar_carta(self):
        if not self.deck:
            print(f"{self.nome} não tem mais cartas no deck!")
            return

        if len(self.mao) >= LIMITE_MAO:
            descartada = self.mao.pop(0)
            print(f"{self.nome} estava com a mão cheia! Descartou: {descartada.nome}")

        carta = self.deck.pop(0)
        self.mao.append(carta)
        print(f"{self.nome} comprou: {carta.nome}")

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

    def usar_habilidade(self, slot, oponente):
        carta = self.campo[slot]
        if carta and self.mana >= carta.custo_habilidade and carta.efeito_habilidade:
            alvos_validos = []

            if carta.tipo_habilidade == "cura_aliado":
                alvos_validos = [i for i, c in enumerate(self.campo) if c]
            elif carta.tipo_habilidade == "dano_inimigo":
                alvos_validos = [i for i, c in enumerate(oponente.campo) if c]

            if not alvos_validos:
                print("Nenhum alvo válido!")
                return

            print(f"Alvos disponíveis para a habilidade '{carta.habilidade}':")
            for idx in alvos_validos:
                if carta.tipo_habilidade == "cura_aliado":
                    print(f"[{idx}] {self.campo[idx].resumo()}")
                else:
                    print(f"[{idx}] {oponente.campo[idx].resumo()}")

            escolha = input("Escolha o número do slot alvo: ")
            try:
                alvo_idx = int(escolha)
                if alvo_idx in alvos_validos:
                    self.mana -= carta.custo_habilidade
                    carta.efeito_habilidade(self, oponente, alvo_idx)
                else:
                    print("Escolha inválida.")
            except:
                print("Entrada inválida.")

    def atacar_slot(self, slot, oponente):
        atacante = self.campo[slot]
        defensor = oponente.campo[slot]
        if atacante:
            print(f"{self.nome} ataca com {atacante.nome} no slot {slot+1}!")
            if defensor:
                dano = atacante.ataque
                defensor.defesa -= dano
                print(f"{defensor.nome} sofreu {dano} de dano, DEF agora: {defensor.defesa}")
                if defensor.defesa <= 0:
                    print(f"{defensor.nome} foi destruído!")
                    if defensor.efeito_morte:
                        defensor.efeito_morte(oponente, self, slot)
                    oponente.campo[slot] = None
            else:
                print(f"Ataque direto! {atacante.ataque} de dano na vida de {oponente.nome}")
                oponente.vida -= atacante.ataque

# Exemplos de efeitos com alvo
def cura_aliado(jogador, oponente, alvo_idx):
    alvo = jogador.campo[alvo_idx]
    if alvo:
        alvo.defesa += 3
        print(f"{alvo.nome} recuperou 3 de defesa!")

def dano_direto_inimigo(jogador, oponente, alvo_idx):
    alvo = oponente.campo[alvo_idx]
    if alvo:
        alvo.defesa -= 2
        print(f"{alvo.nome} sofreu 2 de dano direto!")
        if alvo.defesa <= 0:
            print(f"{alvo.nome} foi destruído!")
            if alvo.efeito_morte:
                alvo.efeito_morte(oponente, jogador, alvo_idx)
            oponente.campo[alvo_idx] = None

def efeito_morte_dano(oponente, jogador, slot):
    print(f"{oponente.nome} sofreu 2 de dano por efeito de morte!")
    oponente.vida -= 2

def criar_deck():
    return [
        Carta("Goblin Selvagem", 2, 2, 1, "Investida", 1),
        Carta("Clérigo Curador", 3, 1, 3, "Cura um aliado", 2, "cura_aliado", cura_aliado),
        Carta("Mago de Fogo", 6, 4, 4, "Dano direto", 3, "dano_inimigo", dano_direto_inimigo),
        Carta("Bomba Viva", 4, 3, 2, "Explosão ao morrer", 2, None, None, efeito_morte_dano),
    ] * 3

def mostrar_estado(jogador1, jogador2):
    print("\n==================== ESTADO DO CAMPO ====================")
    print(f"{jogador1.nome}: Vida: {jogador1.vida} | Mana: {jogador1.mana}")
    print(f"{jogador2.nome}: Vida: {jogador2.vida} | Mana: {jogador2.mana}\n")

    print("Campo:")
    for i in range(4):
        slot1 = jogador1.campo[i].resumo() if jogador1.campo[i] else "[Vazio]"
        slot2 = jogador2.campo[i].resumo() if jogador2.campo[i] else "[Vazio]"
        print(f"Slot {i+1}: {jogador1.nome}: {slot1}  ||  {jogador2.nome}: {slot2}")
    print("========================================================\n")

def batalha(jogador1, jogador2):
    while jogador1.vida > 0 and jogador2.vida > 0:
        for jogador, oponente in [(jogador1, jogador2), (jogador2, jogador1)]:
            print(f"\n\n==== Turno de {jogador.nome} ====")
            jogador.ganhar_mana()
            jogador.comprar_carta()
            mostrar_estado(jogador1, jogador2)

            print(f"Mão de {jogador.nome}:")
            for idx, carta in enumerate(jogador.mao):
                print(f"[{idx}] {carta.nome} | Custo:{carta.custo_mana} | ATK:{carta.ataque} | DEF:{carta.defesa} | Hab:{carta.habilidade}")

            # Jogar primeira carta disponível
            for idx, carta in enumerate(jogador.mao):
                for slot in range(4):
                    if jogador.mana >= carta.custo_mana and jogador.campo[slot] is None:
                        jogador.jogar_carta(idx, slot)
                        break

            # Usar habilidades
            for slot in range(4):
                if jogador.campo[slot] and jogador.campo[slot].efeito_habilidade:
                    if jogador.mana >= jogador.campo[slot].custo_habilidade:
                        jogador.usar_habilidade(slot, oponente)

            # Atacar
            for slot in range(4):
                jogador.atacar_slot(slot, oponente)

            # Fim de jogo
            if oponente.vida <= 0:
                print(f"\n=== {jogador.nome} venceu a partida! ===")
                return

# Inicialização
jogador1 = Jogador("Player 1")
jogador2 = Jogador("Player 2")

jogador1.deck = criar_deck()
jogador2.deck = criar_deck()

random.shuffle(jogador1.deck)
random.shuffle(jogador2.deck)

batalha(jogador1, jogador2)
