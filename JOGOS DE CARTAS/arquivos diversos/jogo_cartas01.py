class Carta:
    def __init__(self, nome, custo_mana, ataque, defesa, habilidade, custo_habilidade):
        self.nome = nome
        self.custo_mana = custo_mana
        self.ataque = ataque
        self.defesa = defesa
        self.habilidade = habilidade
        self.custo_habilidade = custo_habilidade
        self.em_campo = False

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mana = 0
        self.turno = 0
        self.deck = []
        self.mao = []
        self.campo = [None, None, None, None]  # 4 slots

    def ganhar_mana(self):
        ganho_por_turno = [1, 3, 5, 6, 7, 8, 9, 10]
        if self.turno < len(ganho_por_turno):
            self.mana = ganho_por_turno[self.turno]
        else:
            self.mana = 10
        self.turno += 1

    def jogar_carta(self, indice_carta, slot):
        carta = self.mao[indice_carta]
        if self.mana >= carta.custo_mana and self.campo[slot] is None:
            self.mana -= carta.custo_mana
            self.campo[slot] = carta
            carta.em_campo = True
            print(f"{self.nome} jogou {carta.nome} no slot {slot+1}.")
        else:
            print(f"{self.nome} não conseguiu jogar a carta.")

    def usar_habilidade(self, slot):
        carta = self.campo[slot]
        if carta and self.mana >= carta.custo_habilidade:
            self.mana -= carta.custo_habilidade
            print(f"{self.nome} usou a habilidade da carta {carta.nome}: {carta.habilidade}")
        else:
            print(f"{self.nome} não pode usar a habilidade.")

# Exemplo de Teste de Batalha Básica:
jogador1 = Jogador("Player 1")
jogador2 = Jogador("Player 2")

# Criando algumas cartas de exemplo
goblin = Carta("Goblin Selvagem", 2, 2, 1, "Investida: +1 ATK", 1)
troll = Carta("Troll das Rochas", 5, 4, 5, "Regenerar: Recupera 2 de vida", 2)

# Montando decks e mãos
jogador1.mao.append(goblin)
jogador2.mao.append(troll)

# Iniciando turnos
jogador1.ganhar_mana()
jogador2.ganhar_mana()

# Jogando cartas
jogador1.jogar_carta(0, 0)
jogador2.jogar_carta(0, 1)

# Usando habilidades
jogador1.usar_habilidade(0)
