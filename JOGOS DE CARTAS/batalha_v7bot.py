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
        self.tipo_habilidade = tipo_habilidade
        self.efeito_habilidade = efeito_habilidade
        self.efeito_morte = efeito_morte
        self.em_campo = False

    def resumo(self):
        return f"{self.nome} (ATK:{self.ataque} DEF:{self.defesa})"

class Jogador:
    def __init__(self, nome, is_bot=False):
        self.nome = nome
        self.is_bot = is_bot
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
            return
        carta = self.mao[indice_carta]
        if self.mana >= carta.custo_mana and self.campo[slot] is None:
            self.mana -= carta.custo_mana
            self.campo[slot] = carta
            carta.em_campo = True
            self.mao.pop(indice_carta)
            print(f"{self.nome} jogou {carta.nome} no slot {slot+1}.")

    def usar_habilidade(self, slot, oponente):
        carta = self.campo[slot]
        if carta and self.mana >= carta.custo_habilidade and carta.efeito_habilidade:
            alvos_validos = []

            if carta.tipo_habilidade == "cura_aliado":
                alvos_validos = [i for i, c in enumerate(self.campo) if c]
            elif carta.tipo_habilidade == "dano_inimigo":
                alvos_validos = [i for i, c in enumerate(oponente.campo) if c]

            if not alvos_validos:
                return

            alvo_idx = random.choice(alvos_validos) if self.is_bot else self.escolher_alvo(alvos_validos, carta, oponente)
            if alvo_idx is not None:
                self.mana -= carta.custo_habilidade
                carta.efeito_habilidade(self, oponente, alvo_idx)

    def escolher_alvo(self, alvos_validos, carta, oponente):
        print(f"Escolha o alvo para a habilidade '{carta.habilidade}':")
        for idx in alvos_validos:
            if carta.tipo_habilidade == "cura_aliado":
                print(f"[{idx}] {self.campo[idx].resumo()}")
            else:
                print(f"[{idx}] {oponente.campo[idx].resumo()}")
        try:
            escolha = int(input("Digite o número do slot alvo: "))
            if escolha in alvos_validos:
                return escolha
        except:
            pass
        print("Escolha inválida.")
        return None

    def atacar_slot(self, slot, oponente):
        atacante = self.campo[slot]
        defensor = oponente.campo[slot]
        if atacante:
            print(f"{self.nome} ataca com {atacante.nome} no slot {slot+1}!")
            if defensor:
                defensor.defesa -= atacante.ataque
                print(f"{defensor.nome} levou {atacante.ataque} de dano, DEF agora: {defensor.defesa}")
                if defensor.defesa <= 0:
                    print(f"{defensor.nome} foi destruído!")
                    if defensor.efeito_morte:
                        defensor.efeito_morte(oponente, self, slot)
                    oponente.campo[slot] = None
            else:
                print(f"Ataque direto! {atacante.ataque} de dano na vida de {oponente.nome}")
                oponente.vida -= atacante.ataque

    def turno_automatico(self, oponente):
        self.ganhar_mana()
        self.comprar_carta()

        # Jogar a primeira carta possível
        for idx, carta in enumerate(self.mao):
            for slot in range(4):
                if self.mana >= carta.custo_mana and self.campo[slot] is None:
                    self.jogar_carta(idx, slot)
                    break

        # Usar habilidades
        for slot in range(4):
            if self.campo[slot] and self.campo[slot].efeito_habilidade:
                if self.mana >= self.campo[slot].custo_habilidade:
                    self.usar_habilidade(slot, oponente)

        # Atacar
        for slot in range(4):
            self.atacar_slot(slot, oponente)

# Efeitos
def cura_aliado(jogador, oponente, alvo_idx):
    alvo = jogador.campo[alvo_idx]
    if alvo:
        alvo.defesa += 3
        print(f"{alvo.nome} recuperou 3 de defesa!")

def dano_direto_inimigo(jogador, oponente, alvo_idx):
    alvo = oponente.campo[alvo_idx]
    if alvo:
        alvo.defesa -= 2
        print(f"{alvo.nome} levou 2 de dano direto!")
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

def batalha(jogador_humano, bot):
    while jogador_humano.vida > 0 and bot.vida > 0:
        for jogador, oponente in [(jogador_humano, bot), (bot, jogador_humano)]:
            print(f"\n\n==== Turno de {jogador.nome} ====")

            if jogador.is_bot:
                jogador.turno_automatico(oponente)
            else:
                jogador.ganhar_mana()
                jogador.comprar_carta()
                mostrar_estado(jogador_humano, bot)

                print(f"Mão de {jogador.nome}:")
                for idx, carta in enumerate(jogador.mao):
                    print(f"[{idx}] {carta.nome} | Custo:{carta.custo_mana} | ATK:{carta.ataque} | DEF:{carta.defesa} | Hab:{carta.habilidade}")

                # Jogar a primeira carta disponível
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

            # Verificar fim de jogo
            if oponente.vida <= 0:
                print(f"\n=== {jogador.nome} venceu a partida! ===")
                return

# Inicialização
player = Jogador("Player 1", is_bot=False)
bot = Jogador("Bot Inimigo", is_bot=True)

player.deck = criar_deck()
bot.deck = criar_deck()

random.shuffle(player.deck)
random.shuffle(bot.deck)

batalha(player, bot)
