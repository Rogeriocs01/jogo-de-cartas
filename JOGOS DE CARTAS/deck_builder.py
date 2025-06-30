from inventario_jogador import inventario

def montar_deck(inventario_atual, tamanho_deck=10):
    """
    Permite ao jogador escolher até tamanho_deck cartas para seu deck,
    usando IDs do inventário.
    Retorna uma lista de IDs selecionados.
    """
    deck = []
    print("\n=== MONTAGEM DE DECK ===")
    if not inventario_atual:
        print("Você não tem cartas no inventário. Use o sistema de recompensas primeiro.")
        return deck

    # Converter inventário em lista
    itens = list(inventario_atual.items())  # [(carta_id, qtty), ...]
    # Enquanto faltar cartas no deck e o jogador quiser adicionar:
    while len(deck) < tamanho_deck:
        print(f"\nCartas selecionadas ({len(deck)}/{tamanho_deck}): {deck}")
        print("Seu inventário:")
        for idx, (cid, qtd) in enumerate(itens, start=1):
            print(f"{idx}. {cid} x{qtd}")
        escolha = input(f"\nDigite o número da carta a adicionar (ou ENTER para finalizar): ")
        if escolha == "":
            break
        try:
            idx = int(escolha) - 1
            cid, qtd = itens[idx]
            if qtd > 0:
                deck.append(cid)
                inventario_atual[cid] -= 1
                if inventario_atual[cid] == 0:
                    itens.pop(idx)
                print(f"{cid} adicionado ao deck.")
            else:
                print("Sem cópias restantes dessa carta.")
        except (ValueError, IndexError):
            print("Escolha inválida.")
    print(f"\nDeck final: {deck}")
    return deck
