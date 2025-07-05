# batalha/turno_jogador.py
from batalha.habilidade_cartas import usar_habilidade_de_carta
from batalha.habilidade_heroi import usar_habilidade_heroi
from interface_terminal import exibir_campo

def turno_jogador(jogador, inimigo):
    print(f"\n🎴 Turno de {jogador.nome}")
    jogador.mana = 3
    jogador.resetar_habilidades()
    jogador.comprar_carta()
    exibir_campo(jogador, inimigo)

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
                exibir_campo(jogador, inimigo)
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
                exibir_campo(jogador, inimigo)
            else:
                print("❌ Slot atacante vazio.")

        elif escolha == "3":
            usar_habilidade_de_carta(jogador, inimigo)
            exibir_campo(jogador, inimigo)

        elif escolha == "4":
            usar_habilidade_heroi(jogador, inimigo)
            exibir_campo(jogador, inimigo)

        elif escolha == "0":
            break

        else:
            print("❌ Ação inválida.")
        print(f"🔹 Mana restante: {jogador.mana}")
