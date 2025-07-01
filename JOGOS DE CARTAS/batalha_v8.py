# batalha_v8.py
import random
from carta import Carta
from executar_habilidade import executar_habilidade
from card_repository import get_carta_by_id
from habilidades.habilidades_heroi import heroi_habilidades

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


def usar_habilidade_de_carta(jogador, inimigo):
    print("\nCartas com habilidade disponíveis:")
    for idx, carta in enumerate(jogador.campo):
        if carta:
            status = "✨ Usada" if carta.habilidade_usada else "✔ Disponível"
            print(f"{idx + 1} - {carta.nome} ({status})")

    escolha = input("Escolha o número da carta para usar a habilidade (ou 0 para cancelar): ")
    if not escolha.isdigit() or int(escolha) not in range(0, 6):
        print("❌ Escolha inválida.")
        return

    idx = int(escolha) - 1
    if idx == -1:
        return

    carta_escolhida = jogador.campo[idx]
    if not carta_escolhida:
        print("❌ Não há carta nesse slot.")
        return

    if carta_escolhida.habilidade_usada:
        print("⚠️ Essa carta já usou sua habilidade neste turno.")
        return

    if jogador.mana < carta_escolhida.custo_mana:
        print("⚠️ Mana insuficiente para usar a habilidade.")
        return

    jogador.mana -= carta_escolhida.custo_mana
    executar_habilidade(carta_escolhida.id, carta_escolhida, jogador, inimigo)
    carta_escolhida.habilidade_usada = True


def usar_habilidade_heroi(jogador, inimigo):
    if jogador.habilidade_heroi_usada:
        return
    if jogador.habilidade_especial not in heroi_habilidades:
        return
    if jogador.mana < jogador.custo_habilidade:
        return

    jogador.mana -= jogador.custo_habilidade
    habilidade = heroi_habilidades[jogador.habilidade_especial]

    if jogador.habilidade_especial in ["curar", "comprar_cartas", "reduzir_custo_mana"]:
        habilidade(jogador)
    else:
        habilidade(jogador, inimigo)

    jogador.habilidade_heroi_usada = True


def turno_jogador(jogador, inimigo):
    print(f"\n🎴 Turno de {jogador.nome}")
    jogador.mana = 3
    jogador.resetar_habilidades()
    print(f"🔹 Mana disponível: {jogador.mana}")
    jogador.comprar_carta()

    while True:
        print("\nEscolha uma ação:")
        print("1 - Invocar carta")
        print("2 - Atacar")
        print("3 - Usar habilidade de carta")
        print("4 - Usar habilidade especial do herói")
        print("0 - Encerrar turno")
        escolha = input("Ação: ")

        if escolha == "1":
            print("\nMão:")
            for idx, carta in enumerate(jogador.mao):
                print(f"{idx + 1} - {carta}")
            slot = int(input("Escolha o slot do campo (1-5): ")) - 1
            carta_idx = int(input("Escolha o número da carta na mão: ")) - 1
            if 0 <= carta_idx < len(jogador.mao) and 0 <= slot < 5 and not jogador.campo[slot]:
                carta = jogador.mao.pop(carta_idx)
                jogador.campo[slot] = carta
                print(f"🧙 {carta.nome} foi invocada no campo!")
            else:
                print("❌ Escolha inválida.")

        elif escolha == "2":
            for idx, carta in enumerate(jogador.campo):
                if carta:
                    print(f"{idx + 1} - {carta.nome} (ATK: {carta.ataque})")
            slot = int(input("Escolha sua carta atacante (1-5): ")) - 1
            alvo = int(input("Escolha o slot inimigo para atacar (1-5): ")) - 1
            atacante = jogador.campo[slot]
            defensor = inimigo.campo[alvo]
            if atacante:
                if defensor:
                    defensor.defesa -= atacante.ataque
                    print(f"⚔️ {atacante.nome} atacou {defensor.nome}! Nova DEF: {defensor.defesa}")
                    if defensor.defesa <= 0:
                        print(f"💥 {defensor.nome} foi destruída!")
                        inimigo.campo[alvo] = None
                else:
                    inimigo.vida -= atacante.ataque
                    print(f"🏹 Ataque direto! {inimigo.nome} perdeu {atacante.ataque} de vida!")
            else:
                print("❌ Slot atacante vazio.")

        elif escolha == "3":
            usar_habilidade_de_carta(jogador, inimigo)

        elif escolha == "4":
            usar_habilidade_heroi(jogador, inimigo)

        elif escolha == "0":
            break

        else:
            print("❌ Ação inválida.")
        print(f"🔹 Mana restante: {jogador.mana}")


def turno_inimigo(bot, jogador):
    print(f"\n🤖 Turno de {bot.nome}")
    bot.mana = 3
    bot.resetar_habilidades()
    bot.comprar_carta()

    # Invocar melhor carta possível
    bot.mao.sort(key=lambda c: c.ataque + c.defesa, reverse=True)
    for carta in bot.mao[:]:
        for idx in range(5):
            if not bot.campo[idx]:
                bot.campo[idx] = carta
                bot.mao.remove(carta)
                print(f"🤖 {bot.nome} invocou {carta.nome}!")
                break

    # Usar habilidades de carta se possível
    for carta in bot.campo:
        if carta and not carta.habilidade_usada and bot.mana >= carta.custo_mana:
            executar_habilidade(carta.id, carta, bot, jogador)
            carta.habilidade_usada = True
            bot.mana -= carta.custo_mana

    # Usar habilidade do herói se possível
    usar_habilidade_heroi(bot, jogador)

    # Atacar estrategicamente
    for idx, atacante in enumerate(bot.campo):
        if atacante:
            # Atacar carta com menor defesa se houver
            alvos = [(i, c) for i, c in enumerate(jogador.campo) if c]
            if alvos:
                alvo_idx, alvo = min(alvos, key=lambda x: x[1].defesa)
                alvo.defesa -= atacante.ataque
                print(f"🤖 {atacante.nome} atacou {alvo.nome}! Nova DEF: {alvo.defesa}")
                if alvo.defesa <= 0:
                    print(f"💥 {alvo.nome} foi destruída!")
                    jogador.campo[alvo_idx] = None
            else:
                jogador.vida -= atacante.ataque
                print(f"🤖 Ataque direto! {jogador.nome} perdeu {atacante.ataque} de vida!")


def batalha(jogador, bot):
    while jogador.vida > 0 and bot.vida > 0:
        turno_jogador(jogador, bot)
        if bot.vida <= 0:
            print(f"🎉 {jogador.nome} venceu a batalha!")
            break
        turno_inimigo(bot, jogador)
        if jogador.vida <= 0:
            print(f"💀 {bot.nome} venceu a batalha!")
            break


if __name__ == "__main__":
    jogador = Jogador("Jogador")
    bot = Jogador("Bot")
    for i in range(10):
        jogador.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))
        bot.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))
    batalha(jogador, bot)
