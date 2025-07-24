import random
from card_repository import get_carta_by_id
from inventario_jogador import carregar_inventario
from personagens_data import personagens
from progresso_heroi import carregar_progresso, get_tamanho_maximo_deck

def criar_deck_automatico(personagem_nome: str):
    """
    Gera um deck automático baseado no personagem.
    Retorna uma lista de objetos Carta.
    """
    decks = {
        "Thorin, o Bravo": ["Carta_1", "Carta_2", "Carta_3", "Carta_4", "Carta_5"] * 2,
        "Elora, a Arqueira Élfica": ["Carta_6", "Carta_7", "Carta_8", "Carta_9", "Carta_10"] * 2,
        "Balgor, o Orc Sanguinário": ["Carta_11", "Carta_12", "Carta_13", "Carta_14", "Carta_15"] * 2,
        "Luthien, a Maga da Luz": ["Carta_16", "Carta_17", "Carta_18", "Carta_19", "Carta_20"] * 2,
        "Dargul, o Senhor dos Túneis": ["Carta_21", "Carta_22", "Carta_23", "Carta_24", "Carta_25"] * 2,
        "Mirael, a Feiticeira Sombria": ["Carta_26", "Carta_27", "Carta_28", "Carta_29", "Carta_30"] * 2,
        "Rogar, o Bárbaro do Norte": ["Carta_31", "Carta_32", "Carta_33", "Carta_34", "Carta_35"] * 2,
        "Elenor, a Protetora da Floresta": ["Carta_36", "Carta_37", "Carta_38", "Carta_39", "Carta_40"] * 2,
        "Karguk, o Rei Goblin": ["Carta_41", "Carta_42", "Carta_43", "Carta_44", "Carta_45"] * 2,
        "Sirius, o Invocador de Feras": ["Carta_46", "Carta_47", "Carta_48", "Carta_49", "Carta_50"] * 2,
        "Velaria, a Dama das Sombras": ["Carta_51", "Carta_52", "Carta_53", "Carta_54", "Carta_55"] * 2,
        "Grumak, o Demônio da Rocha": ["Carta_56", "Carta_57", "Carta_58", "Carta_59", "Carta_60"] * 2,
        "Thalia, a Curandeira de Elmswood": ["Carta_61", "Carta_62", "Carta_63", "Carta_64", "Carta_65"] * 2,
        "Volgath, o Senhor dos Dragões": ["Carta_66", "Carta_67", "Carta_68", "Carta_69", "Carta_70"] * 2,
        "Feyra, a Caçadora de Almas": ["Carta_71", "Carta_72", "Carta_73", "Carta_74", "Carta_75"] * 2,
        "Gorim, o Guerreiro Anão": ["Carta_76", "Carta_77", "Carta_78", "Carta_79", "Carta_80"] * 2,
        "Deus do Debug": [f"Carta_Debug_{i}" for i in range(1, 10)],
    }

    lista_ids = decks.get(
        personagem_nome,
        ["Carta_1", "Carta_2", "Carta_3", "Carta_4", "Carta_5", "Carta_6", "Carta_7", "Carta_8", "Carta_9", "Carta_10"]
    )

    deck = []
    for carta_id in lista_ids:
        try:
            carta = get_carta_by_id(carta_id)
            deck.append(carta)
        except ValueError as e:
            print(f"[Aviso]: {e}")

    random.shuffle(deck)
    return deck


def montar_deck_manual(nome_heroi, limite_por_carta=3):
    """
    Permite ao jogador montar manualmente seu deck com cartas do inventário.
    O tamanho máximo do deck depende do nível do herói.
    """
    progresso = carregar_progresso()
    nivel = progresso.get(nome_heroi, {}).get("nivel", 1)
    tamanho_deck = get_tamanho_maximo_deck(nivel)

    inventario = carregar_inventario()
    if not inventario:
        print("❌ Você não possui cartas no inventário.")
        return []

    deck_ids = []
    print(f"\n🔧 Montando deck para {nome_heroi} (Nível {nivel}) — Limite: {tamanho_deck} cartas, máx {limite_por_carta} por tipo.")

    while len(deck_ids) < tamanho_deck:
        print(f"\n🃏 Cartas no Deck ({len(deck_ids)}/{tamanho_deck}): {deck_ids}")
        print("📦 Inventário disponível:")

        cartas_disponiveis = [(cid, qtd) for cid, qtd in inventario.items()
                              if deck_ids.count(cid) < min(qtd, limite_por_carta)]

        if not cartas_disponiveis:
            print("✅ Não há mais cartas elegíveis para adicionar.")
            break

        for i, (cid, qtd) in enumerate(cartas_disponiveis, start=1):
            print(f"{i}. {cid} (x{qtd})")

        escolha = input("Digite o número da carta para adicionar (ENTER para finalizar): ")
        if escolha.strip() == "":
            break

        try:
            idx = int(escolha) - 1
            if 0 <= idx < len(cartas_disponiveis):
                carta_id, _ = cartas_disponiveis[idx]
                deck_ids.append(carta_id)
                print(f"✅ {carta_id} adicionada ao deck.")
            else:
                print("❌ Índice fora do intervalo.")
        except ValueError:
            print("❌ Entrada inválida.")

    # Converte IDs em objetos Carta
    deck_final = []
    for cid in deck_ids:
        try:
            deck_final.append(get_carta_by_id(cid))
        except ValueError as e:
            print(f"[Aviso]: {e}")

    print(f"\n🧪 Deck finalizado com {len(deck_final)} cartas.")
    return deck_final
