def selecionar_cartas_para_slots(jogador):
    print("\n📥 Posicione suas cartas nos slots iniciais:")
    print(f"Mana disponível: {jogador.mana}")
    print("Sua mão:")

    for i, carta in enumerate(jogador.mao):
        print(f"[{i}] {carta.nome} | Custo: {carta.custo_mana} | ATK: {carta.ataque} | DEF: {carta.defesa}")

    for slot in range(4):
        if jogador.mana <= 0:
            print("💧 Sem mana suficiente para continuar.")
            break

        escolha = input(f"Slot {slot + 1}: Digite o número da carta para posicionar (ou ENTER para pular): ")
        if escolha == "":
            continue

        try:
            idx = int(escolha)
            carta = jogador.mao[idx]
        except (ValueError, IndexError):
            print("❌ Escolha inválida.")
            continue

        if carta.custo_mana > jogador.mana:
            print("⚠️ Mana insuficiente para essa carta.")
            continue

        jogador.campo[slot] = carta
        jogador.mana -= carta.custo_mana
        jogador.mao.pop(idx)
        print(f"✅ {carta.nome} posicionada no slot {slot + 1}. Mana restante: {jogador.mana}")
