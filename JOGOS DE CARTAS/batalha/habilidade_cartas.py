from habilidades.executar_habilidade import executar_habilidade

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


# ✅ Função necessária para carregar habilidades por ID
def get_habilidade_por_id(habilidade_id):
    return lambda carta, jogador, inimigo: executar_habilidade(habilidade_id, carta, jogador, inimigo)
