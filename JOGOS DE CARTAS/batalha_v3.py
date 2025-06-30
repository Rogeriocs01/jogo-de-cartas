import random

class Carta:
    def __init__(self, nome, custo_mana, ataque, defesa, habilidade, custo_habilidade, efeito_habilidade=None, efeito_morte=None):
        self.nome = nome
        self.custo_mana = custo_mana
        self.ataque = ataque
        self.defesa = defesa
        self.habilidade = habilidade
        self.custo_habilidade = custo_habilidade
        self.efeito_habilidade = efeito_habilidade  # Função que executa o efeito
        self.efeito_morte = efeito_morte  # Função que executa ao morrer
        self.em_campo = False

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

    def usar_habilidade(self, slot, oponente):
        carta = self.campo[slot]
        if carta and self.mana >= carta.custo_habilidade and carta.efeito_habilidade:
            self.mana -= carta.custo_habilidade
            print(f"{self.nome} ativa a habilidade de {carta.nome}: {carta.habilidade}")
            carta.efeito_habilidade(self, oponente, slot)
        else:
            print("Não foi possível usar a habilidade.")

    def atacar_slot(self, slot, oponente):
        atacante = self.campo[slot]
        defensor = oponente.campo[slot]
        if atacante:
            print(f"{self.nome} ataca com {atacante.nome} no slot {slot+1}!")
            if defensor:
                print(f"Oponente tem {defensor.nome} defendendo!")
                dano = atacante.ataque
                defensor.defesa -= dano
                print(f"{defensor.nome} sofreu {dano} de dano, DEF agora é {defensor.defesa}")
                if defensor.defesa <= 0:
                    print(f"{defensor.nome} foi destruído!")
                    if defensor.efeito_morte:
                        defensor.efeito_morte(oponente, self, slot)
                    oponente.campo[slot] = None
            else:
                print(f"Sem defensor! {atacante.ataque} de dano direto na vida de {oponente.nome}!")
                oponente.vida -= atacante.ataque

# Exemplos de efeitos de habilidades e morte
def habilidade_cura(jogador, oponente, slot):
    jogador.vida += 3
    print(f"{jogador.nome} recuperou 3 pontos de vida!")

def habilidade_dano_em_area(jogador, oponente, slot):
    for i in range(4):
        if oponente.campo[i]:
            oponente.campo[i].defesa -= 2
            print(f"{oponente.campo[i].nome} sofreu 2 de dano em área!")
            if oponente.campo[i].defesa <= 0:
                print(f"{oponente.campo[i].nome} foi destruído!")
                if oponente.campo[i].efeito_morte:
                    oponente.campo[i].efeito_morte(oponente, jogador, i)
                oponente.campo[i] = None

def efeito_morte_dano(oponente, jogador, slot):
    print(f"Efeito de morte: {oponente.nome} sofre 2 de dano direto!")
    oponente.vida -= 2

def criar_deck_exemplo():
    return [
        Carta("Goblin Selvagem", 2, 2, 1, "Investida: +1 ATK", 1),
        Carta("Sacerdote Curador", 3, 1, 3, "Cura Mágica: Recupera 3 de vida", 2, habilidade_cura),
        Carta("Mago de Fogo", 6, 4, 4, "Explosão Flamejante: 2 de dano em todas as criaturas inimigas", 3, habilidade_dano_em_area),
        Carta("Bomba Viva", 4, 3, 2, "Ao morrer: causa 2 de dano direto ao oponente", 2, None, efeito_morte_dano),
    ] * 3

def batalha(jogador1, jogador2):
    while jogador1.vida > 0 and jogador2.vida > 0:
        for jogador, oponente in [(jogador1, jogador2), (jogador2, jogador1)]:
            print(f"\n=== Turno de {jogador.nome} ===")
            jogador.ganhar_mana()
            jogador.comprar_carta()
            print(f"Mana: {jogador.mana} | Vida: {jogador.vida}")

            # Exibir mão
            for idx, carta in enumerate(jogador.mao):
                print(f"[{idx}] {carta.nome} (Custo: {carta.custo_mana} | ATK: {carta.ataque} | DEF: {carta.defesa})")

            # Jogar primeira carta disponível
            for idx, carta in enumerate(jogador.mao):
                for slot in range(4):
                    if jogador.mana >= carta.custo_mana and jogador.campo[slot] is None:
                        jogador.jogar_carta(idx, slot)
                        break

            # Usar habilidades se possível
            for slot in range(4):
                if jogador.campo[slot] and jogador.campo[slot].efeito_habilidade:
                    if jogador.mana >= jogador.campo[slot].custo_habilidade:
                        jogador.usar_habilidade(slot, oponente)

            # Atacar com todas as criaturas em campo
            for slot in range(4):
                jogador.atacar_slot(slot, oponente)

            # Verificar fim de jogo
            if oponente.vida <= 0:
                print(f"\n{jogador.nome} venceu a partida!")
                return

# Inicialização
jogador1 = Jogador("Player 1")
jogador2 = Jogador("Player 2")

jogador1.deck = criar_deck_exemplo()
jogador2.deck = criar_deck_exemplo()

random.shuffle(jogador1.deck)
random.shuffle(jogador2.deck)

batalha(jogador1, jogador2)
