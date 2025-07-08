# deck_personalizado.py

import random
from card_repository import get_carta_by_id
from personagens_data import personagens

def criar_deck_personalizado(personagem_nome: str):
    """
    Monta e retorna um deck (lista de Carta) baseado no personagem escolhido.
    Cada ID é convertido em um objeto Carta via get_carta_by_id.
    """
    # Mapeamento de personagem para lista de IDs das 10 cartas iniciais
    decks = {
        "Thorin, o Bravo":             ["Carta_1","Carta_2","Carta_3","Carta_4","Carta_5"] * 2,
        "Elora, a Arqueira Élfica":     ["Carta_6","Carta_7","Carta_8","Carta_9","Carta_10"] * 2,
        "Balgor, o Orc Sanguinário":    ["Carta_11","Carta_12","Carta_13","Carta_14","Carta_15"] * 2,
        "Luthien, a Maga da Luz":       ["Carta_16","Carta_17","Carta_18","Carta_19","Carta_20"] * 2,
        "Dargul, o Senhor dos Túneis":  ["Carta_21","Carta_22","Carta_23","Carta_24","Carta_25"] * 2,
        "Mirael, a Feiticeira Sombria": ["Carta_26","Carta_27","Carta_28","Carta_29","Carta_30"] * 2,
        "Rogar, o Bárbaro do Norte":    ["Carta_31","Carta_32","Carta_33","Carta_34","Carta_35"] * 2,
        "Elenor, a Protetora da Floresta":["Carta_36","Carta_37","Carta_38","Carta_39","Carta_40"] * 2,
        "Karguk, o Rei Goblin":         ["Carta_41","Carta_42","Carta_43","Carta_44","Carta_45"] * 2,
        "Sirius, o Invocador de Feras": ["Carta_46","Carta_47","Carta_48","Carta_49","Carta_50"] * 2,
        "Velaria, a Dama das Sombras":  ["Carta_51","Carta_52","Carta_53","Carta_54","Carta_55"] * 2,
        "Grumak, o Demônio da Rocha":   ["Carta_56","Carta_57","Carta_58","Carta_59","Carta_60"] * 2,
        "Thalia, a Curandeira de Elmswood":["Carta_61","Carta_62","Carta_63","Carta_64","Carta_65"] * 2,
        "Volgath, o Senhor dos Dragões": ["Carta_66","Carta_67","Carta_68","Carta_69","Carta_70"] * 2,
        "Feyra, a Caçadora de Almas":   ["Carta_71","Carta_72","Carta_73","Carta_74","Carta_75"] * 2,
        "Gorim, o Guerreiro Anão":      ["Carta_76","Carta_77","Carta_78","Carta_79","Carta_80"] * 2,

        # 🔥 Deck especial para testes: cartas overpower
        "Deus do Debug": [f"Carta_Debug_{i}" for i in range(1, 11)],
    }

    # Obter a lista de IDs ou usar um fallback genérico (primeiras 10 cartas)
    lista_ids = decks.get(
        personagem_nome,
        ["Carta_1","Carta_2","Carta_3","Carta_4","Carta_5","Carta_6","Carta_7","Carta_8","Carta_9","Carta_10"]
    )

    # Converter IDs em objetos Carta
    deck = []
    for carta_id in lista_ids:
        try:
            carta = get_carta_by_id(carta_id)
            deck.append(carta)
        except ValueError as e:
            # Em caso de ID inválido, avisa no console mas continua
            print(f"Aviso: {e}")

    random.shuffle(deck)
    return deck
