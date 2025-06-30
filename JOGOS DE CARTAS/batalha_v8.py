# batalha_v8.py (versão atualizada com execução de habilidades de cartas e logs elegantes)
import random
from card_repository import get_carta_by_id
from executar_habilidade import executar_habilidade

class Jogador:
    def __init__(self, nome, is_bot=False, habilidade_especial=None, custo_habilidade=0, terreno_favorito=None):
        self.nome = nome
        self.is_bot = is_bot
        self.vida = 20
        self.mana = 0
        self.deck = []
        self.mao = []
        self.campo = [None, None, None, None]
        self.habilidade_especial = habilidade_especial
        self.custo_habilidade = custo_habilidade
        self.terreno_favorito = terreno_favorito
        self.habilidade_usada = False

    def comprar_carta(self):
        if self.deck:
            carta = self.deck.pop(0)
            self.mao.append(carta)
            print(f"🃏 {self.nome} comprou: {carta.nome}")

    def mostrar_mao(self):
        print("\n🖐️ Mão:")
        for i, carta in enumerate(self.mao):
            print(f"[{i}] {carta}")

    def jogar_carta(self):
        self.mostrar_mao()
        for i in range(4):
            if self.campo[i] is None:
                escolha = input(f"Escolha o número da carta para jogar no slot {i+1} (ou ENTER para pular): ")
                if escolha == "":
                    continue
                try:
                    escolha = int(escolha)
                    carta = self.mao[escolha]
                    if self.mana >= carta.custo_mana:
                        self.campo[i] = carta
                        self.mao.pop(escolha)
                        self.mana -= carta.custo_mana
                        print(f"✅ {carta.nome} foi posicionada no slot {i+1}. Mana restante: {self.mana}")
                    else:
                        print("❌ Mana insuficiente para essa carta.")
                except (ValueError, IndexError):
                    print("⚠️ Escolha inválida.")

    def usar_habilidade(self):
        if self.habilidade_especial and not self.habilidade_usada:
            if self.mana >= self.custo_habilidade:
                print(f"🌟 {self.nome} usa habilidade especial: {self.habilidade_especial}")
                self.mana -= self.custo_habilidade
                self.habilidade_usada = True
            else:
                print("❌ Mana insuficiente para usar a habilidade do herói.")
        else:
            print("⚠️ Habilidade já usada neste turno ou não disponível.")

    def usar_habilidade_de_carta(self, oponente):
        print("\n✨ Habilidades disponíveis no campo:")
        for i, carta in enumerate(self.campo):
            if carta:
                print(f"[{i}] {carta.nome} - {carta.habilidade} (Custo: {carta.custo_habilidade})")

        escolha = input("Escolha o slot da carta para ativar a habilidade (ou ENTER para cancelar): ")
        if escolha == "":
            return
        try:
            slot = int(escolha)
            if 0 <= slot < 4 and self.campo[slot]:
                carta = self.campo[slot]
                if self.mana >= carta.custo_habilidade:
                    self.mana -= carta.custo_habilidade
                    carta_id = f"Carta_{slot + 1}"  # Exemplo genérico, ideal seria associar ID real da carta
                    executar_habilidade(carta_id, carta, self, oponente)
                else:
                    print("❌ Mana insuficiente para ativar a habilidade.")
            else:
                print("⚠️ Slot inválido.")
        except ValueError:
            print("⚠️ Entrada inválida.")

    def atacar(self, oponente):
        print("\n⚔️ Iniciando ataques...")
        for i in range(4):
            carta = self.campo[i]
            if carta:
                inimigo = oponente.campo[i]
                if inimigo:
                    print(f"➡️ {carta.nome} ataca {inimigo.nome}")
                    inimigo.defesa -= carta.ataque
                    if inimigo.defesa <= 0:
                        print(f"💥 {inimigo.nome} foi destruído!")
                        oponente.campo[i] = None
                    else:
                        print(f"🛡️ {inimigo.nome} agora tem {inimigo.defesa} de DEF")
                else:
                    print(f"🏹 {carta.nome} ataca diretamente o jogador!")
                    oponente.vida -= carta.ataque
                    print(f"❤️ {oponente.nome} perde {carta.ataque} de vida (vida restante: {oponente.vida})")


def batalha(jogador1, jogador2):
    turno = 1
    random.shuffle(jogador1.deck)
    random.shuffle(jogador2.deck)

    for _ in range(3):
        jogador1.comprar_carta()
        jogador2.comprar_carta()

    print("\n📥 Posicione suas cartas nos slots iniciais:")
    jogador1.mana = 3
    jogador1.jogar_carta()

    while jogador1.vida > 0 and jogador2.vida > 0:
        print(f"\n==== 🔄 TURNO {turno} ====")

        for jogador in [jogador1, jogador2]:
            jogador.mana += 1
            jogador.habilidade_usada = False
            jogador.comprar_carta()

            print(f"\n🎮 Turno de {jogador.nome} | Vida: {jogador.vida} | Mana: {jogador.mana}")

            if jogador.is_bot:
                for i in range(4):
                    for carta in jogador.mao:
                        if jogador.mana >= carta.custo_mana and jogador.campo[i] is None:
                            jogador.campo[i] = carta
                            jogador.mana -= carta.custo_mana
                            jogador.mao.remove(carta)
                            print(f"🤖 {jogador.nome} jogou {carta.nome} no slot {i+1}.")
                            break
                jogador.usar_habilidade()
                jogador.atacar(jogador1 if jogador == jogador2 else jogador2)
            else:
                while True:
                    print("\n--- 🔧 Ações disponíveis ---")
                    print("1️⃣ Jogar carta")
                    print("2️⃣ Usar habilidade do herói")
                    print("3️⃣ Usar habilidade de carta")
                    print("4️⃣ Atacar")
                    print("5️⃣ Encerrar turno")

                    escolha = input("Escolha uma ação: ")

                    if escolha == "1":
                        jogador.jogar_carta()
                    elif escolha == "2":
                        jogador.usar_habilidade()
                    elif escolha == "3":
                        jogador.usar_habilidade_de_carta(jogador2 if jogador == jogador1 else jogador1)
                    elif escolha == "4":
                        jogador.atacar(jogador2 if jogador == jogador1 else jogador1)
                    elif escolha == "5":
                        break
                    else:
                        print("Opção inválida.")

        turno += 1

    vencedor = jogador1.nome if jogador1.vida > 0 else jogador2.nome
    print(f"\n🏆 FIM DE JOGO: {vencedor} venceu a partida!")