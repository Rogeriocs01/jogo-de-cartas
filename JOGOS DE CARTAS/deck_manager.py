import json
import os
import random
from card_repository import get_carta_by_id
from inventario_jogador import carregar_inventario
from personagens_data import personagens
from progresso_heroi import carregar_progresso

CAMINHO_DECKS = "decks_salvos"
os.makedirs(CAMINHO_DECKS, exist_ok=True)

LIMITE_POR_CARTA = 3

# Tamanho máximo de deck por nível do herói
TAMANHO_DECK_POR_NIVEL = {
    1: 10,
    2: 12,
    3: 14,
    4: 16,
    5: 18,
    6: 20,
    7: 22,
    8: 23,
    9: 24,
    10: 25,
}

def get_tamanho_deck(nome_heroi):
    progresso = carregar_progresso()
    nivel = progresso.get(nome_heroi, {}).get("nivel", 1)
    return TAMANHO_DECK_POR_NIVEL.get(nivel, 10)

def salvar_deck(nome_heroi, lista_ids):
    caminho = os.path.join(CAMINHO_DECKS, f"deck_{nome_heroi}.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(lista_ids, f, indent=4)

def carregar_deck(nome_heroi):
    caminho = os.path.join(CAMINHO_DECKS, f"deck_{nome_heroi}.json")
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            lista_ids = json.load(f)
            return [get_carta_by_id(cid) for cid in lista_ids]
    return None

def criar_deck_automatico(nome_heroi):
    """
    Gera um deck fixo pré-definido para cada herói.
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

    lista_ids = decks.get(nome_heroi, ["Carta_1", "Carta_2", "Carta_3", "Carta_4", "Carta_5"] * 2)
    tamanho = get_tamanho_deck(nome_heroi)

    random.shuffle(lista_ids)
    lista_ids = lista_ids[:tamanho]

    salvar_deck(nome_heroi, lista_ids)
    return [get_carta_by_id(cid) for cid in lista_ids]

def montar_deck_manual(nome_heroi):
    """
    Permite montar um deck com base no inventário global.
    Salva o deck montado e retorna objetos Carta.
    """
    tamanho_max = get_tamanho_deck(nome_heroi)
    inventario = carregar_inventario()

    if not inventario:
        print("❌ Seu inventário está vazio.")
        return []

    deck_ids = []

    while len(deck_ids) < tamanho_max:
        print(f"\n🃏 Deck atual ({len(deck_ids)}/{tamanho_max}): {deck_ids}")
        print("📦 Inventário:")
        cartas_disponiveis = [(cid, qtd) for cid, qtd in inventario.items()
                              if deck_ids.count(cid) < min(qtd, LIMITE_POR_CARTA)]

        if not cartas_disponiveis:
            print("⚠️ Não há mais cartas disponíveis para adicionar.")
            break

        for i, (cid, qtd) in enumerate(cartas_disponiveis, start=1):
            print(f"{i}. {cid} (x{qtd})")

        escolha = input("Digite o número da carta (ENTER para finalizar): ")
        if escolha.strip() == "":
            break

        try:
            idx = int(escolha) - 1
            if 0 <= idx < len(cartas_disponiveis):
                carta_id, _ = cartas_disponiveis[idx]
                deck_ids.append(carta_id)
                print(f"✅ {carta_id} adicionada.")
            else:
                print("❌ Escolha fora do intervalo.")
        except ValueError:
            print("❌ Entrada inválida.")

    salvar_deck(nome_heroi, deck_ids)
    return [get_carta_by_id(cid) for cid in deck_ids]
