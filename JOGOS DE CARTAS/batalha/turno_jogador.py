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

    # ✅ Exibir mão no início
    print("\n🖐️ Mão do jogador:")
    if jogador.mao:
        for idx, carta in enumerate(jogador.mao):
            print(f" {idx + 1} - {carta.nome}  | Mana: {carta.custo_mana}")
    else:
        print(" (vazio)")

    while True:
        print("\nEscolha uma ação:")
        print("1 - Invocar carta")
        print("2 - Atacar")
        print("3 - Usar habilidade de carta")
        print("4 - Usar habilidade especial do herói")
        print("0 - Encerrar turno")
        escolha = input("Ação: ")

        if escolha == "1":
            if not jogador.mao:
                print("❌ Você não possui cartas na mão.")
                continue
            try:
                slot = int(input("Escolha o slot do campo (1-5): ")) - 1
                carta_idx = int(input("Escolha o número da carta na mão: ")) - 1
                sucesso = jogador.invocar_carta(carta_idx, slot)
                if sucesso:
                    exibir_campo(jogador, inimigo)
            except (ValueError, IndexError):
                print("❌ Entrada inválida.")

        elif escolha == "2":
            for idx, carta in enumerate(jogador.campo):
                if carta:
                    print(f"{idx + 1} - {carta.nome} (ATK: {carta.ataque})")
            try:
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
            except (ValueError, IndexError):
                print("❌ Entrada inválida.")

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
