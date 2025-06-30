from carta import Carta

# Repositório de cartas do jogo: IDs de "Carta_1" a "Carta_80"
card_repository = {
    "Carta_1": {"nome": "Dragão de Lava", "tipo": "Lava", "raridade": "Raro", "ataque": 7, "defesa": 5, "mana": 6,  "custo_habilidade": 3},
    "Carta_2": {"nome": "Sentinela de Água", "tipo": "Água", "raridade": "Comum", "ataque": 2, "defesa": 4, "mana": 2, "custo_habilidade": 1},
    "Carta_3": {"nome": "Golem de Pedra", "tipo": "Terra", "raridade": "Comum", "ataque": 3, "defesa": 6, "mana": 3,  "custo_habilidade": 1},
    "Carta_4": {"nome": "Fada da Luz", "tipo": "Luz", "raridade": "Incomum", "ataque": 1, "defesa": 2, "mana": 2, "custo_habilidade": 2},
    "Carta_5": {"nome": "Espectro das Sombras", "tipo": "Trevas", "raridade": "Raro", "ataque": 5, "defesa": 3, "mana": 4, "custo_habilidade": 3},
    "Carta_6": {"nome": "Mago de Fogo", "tipo": "Lava", "raridade": "Comum", "ataque": 4, "defesa": 2, "mana": 3, "custo_habilidade": 1},
    "Carta_7": {"nome": "Guardião da Floresta", "tipo": "Floresta", "raridade": "Incomum", "ataque": 2, "defesa": 5, "mana": 3, "custo_habilidade": 2},
    "Carta_8": {"nome": "Sereia Encantadora", "tipo": "Água", "raridade": "Raro", "ataque": 3, "defesa": 4, "mana": 4,  "custo_habilidade": 3},
    "Carta_9": {"nome": "Espadachim Élfico", "tipo": "Floresta", "raridade": "Comum", "ataque": 3, "defesa": 3, "mana": 2, "custo_habilidade": 1},
    "Carta_10": {"nome": "Anjo Guardião", "tipo": "Luz", "raridade": "Raro", "ataque": 4, "defesa": 6, "mana": 5, "custo_habilidade": 3},
    "Carta_11": {"nome": "Lobo da Nevasca", "tipo": "Vento", "raridade": "Incomum", "ataque": 3, "defesa": 2, "mana": 3, "custo_habilidade": 2},
    "Carta_12": {"nome": "Curandeiro de Elmswood", "tipo": "Floresta", "raridade": "Comum", "ataque": 1, "defesa": 4, "mana": 2, "custo_habilidade": 1},
    "Carta_13": {"nome": "Guardião de Rocha", "tipo": "Terra", "raridade": "Incomum", "ataque": 2, "defesa": 5, "mana": 4, "custo_habilidade": 2},
    "Carta_14": {"nome": "Goblin Selvagem", "tipo": "Lava", "raridade": "Comum", "ataque": 2, "defesa": 1, "mana": 1, "custo_habilidade": 1},
    "Carta_15": {"nome": "Serpente da Água", "tipo": "Água", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_16": {"nome": "Árvore Ancestral", "tipo": "Floresta", "raridade": "Raro", "ataque": 2, "defesa": 7, "mana": 5, "custo_habilidade": 3},
    "Carta_17": {"nome": "Escudeiro da Planície", "tipo": "Planície", "raridade": "Comum", "ataque": 2, "defesa": 3, "mana": 2, "custo_habilidade": 1},
    "Carta_18": {"nome": "Bomba Viva", "tipo": "Lava", "raridade": "Incomum", "ataque": 3, "defesa": 2, "mana": 4, "custo_habilidade": 2},
    "Carta_19": {"nome": "Guerreiro de Gondren", "tipo": "Planície", "raridade": "Comum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 1},
    "Carta_20": {"nome": "Ilusionista Etéreo", "tipo": "Vento", "raridade": "Raro", "ataque": 2, "defesa": 3, "mana": 4, "custo_habilidade": 3},
    "Carta_21": {"nome": "Guardião da Luz", "tipo": "Luz", "raridade": "Raro", "ataque": 4, "defesa": 5, "mana": 5, "custo_habilidade": 3},
    "Carta_22": {"nome": "Elemental de Água", "tipo": "Água", "raridade": "Incomum", "ataque": 3, "defesa": 4, "mana": 3, "custo_habilidade": 2},
    "Carta_23": {"nome": "Cavaleiro da Tempestade", "tipo": "Vento", "raridade": "Raro", "ataque": 5, "defesa": 3, "mana": 5, "custo_habilidade": 3},
    "Carta_24": {"nome": "Espreitador Sombrio", "tipo": "Trevas", "raridade": "Incomum", "ataque": 3, "defesa": 2, "mana": 3, "custo_habilidade": 2},
    "Carta_25": {"nome": "Guardião Subterrâneo", "tipo": "Terra", "raridade": "Comum", "ataque": 2, "defesa": 4, "mana": 2, "custo_habilidade": 1},
    "Carta_26": {"nome": "Feiticeira da Lua", "tipo": "Trevas", "raridade": "Raro", "ataque": 3, "defesa": 4, "mana": 4, "custo_habilidade": 3},
    "Carta_27": {"nome": "Águia Celeste", "tipo": "Vento", "raridade": "Comum", "ataque": 2, "defesa": 2, "mana": 1, "custo_habilidade": 1},
    "Carta_28": {"nome": "Lança de Chamas", "tipo": "Lava", "raridade": "Incomum", "ataque": 5, "defesa": 1, "mana": 4, "custo_habilidade": 2},
    "Carta_29": {"nome": "Xamã Tribal", "tipo": "Floresta", "raridade": "Incomum", "ataque": 2, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_30": {"nome": "Guardião Glacial", "tipo": "Água", "raridade": "Raro", "ataque": 4, "defesa": 6, "mana": 5, "custo_habilidade": 3},
    "Carta_31": {"nome": "Guardião das Dunas", "tipo": "Planície", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_32": {"nome": "Dragão Etéreo", "tipo": "Vento", "raridade": "Raro", "ataque": 6, "defesa": 4, "mana": 6, "custo_habilidade": 4},
    "Carta_33": {"nome": "Fênix Incandescente", "tipo": "Lava", "raridade": "Raro", "ataque": 5, "defesa": 3, "mana": 5, "custo_habilidade": 3},
    "Carta_34": {"nome": "Oráculo das Marés", "tipo": "Água", "raridade": "Incomum", "ataque": 2, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_35": {"nome": "Vigia da Penumbra", "tipo": "Trevas", "raridade": "Incomum", "ataque": 2, "defesa": 2, "mana": 2, "custo_habilidade": 2},
    "Carta_36": {"nome": "Sentinela Celeste", "tipo": "Luz", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_37": {"nome": "Clérigo Curador", "tipo": "Luz", "raridade": "Comum", "ataque": 1, "defesa": 3, "mana": 3, "custo_habilidade": 1},
    "Carta_38": {"nome": "Muralha de Espinhos", "tipo": "Floresta", "raridade": "Incomum", "ataque": 0, "defesa": 6, "mana": 3, "custo_habilidade": 2},
    "Carta_39": {"nome": "Cavaleiro Sagrado", "tipo": "Planície", "raridade": "Raro", "ataque": 4, "defesa": 4, "mana": 5, "custo_habilidade": 3},
    "Carta_40": {"nome": "Banshee Gritante", "tipo": "Trevas", "raridade": "Raro", "ataque": 5, "defesa": 2, "mana": 4, "custo_habilidade": 3},
    "Carta_41": {"nome": "Golem de Cristal", "tipo": "Luz", "raridade": "Incomum", "ataque": 3, "defesa": 5, "mana": 4, "custo_habilidade": 2},
    "Carta_42": {"nome": "Feiticeiro do Relâmpago", "tipo": "Vento", "raridade": "Raro", "ataque": 4, "defesa": 3, "mana": 5, "custo_habilidade": 3},
    "Carta_43": {"nome": "Escorpião de Areia", "tipo": "Planície", "raridade": "Comum", "ataque": 2, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_44": {"nome": "Guardiã das Estrelas", "tipo": "Luz", "raridade": "Raro", "ataque": 3, "defesa": 4, "mana": 5, "custo_habilidade": 3},
    "Carta_45": {"nome": "Demônio do Caos", "tipo": "Trevas", "raridade": "Raro", "ataque": 6, "defesa": 3, "mana": 6, "custo_habilidade": 4},
    "Carta_46": {"nome": "Arqueiro Fantasma", "tipo": "Trevas", "raridade": "Incomum", "ataque": 3, "defesa": 2, "mana": 3, "custo_habilidade": 2},
    "Carta_47": {"nome": "Guarda Real", "tipo": "Planície", "raridade": "Comum", "ataque": 2, "defesa": 4, "mana": 2, "custo_habilidade": 1},
    "Carta_48": {"nome": "Serpente do Trovão", "tipo": "Vento", "raridade": "Raro", "ataque": 5, "defesa": 2, "mana": 5, "custo_habilidade": 3},
    "Carta_49": {"nome": "Caçadora de Alias", "tipo": "Trevas", "raridade": "Raro", "ataque": 4, "defesa": 3, "mana": 4, "custo_habilidade": 2},
    "Carta_50": {"nome": "Barreira de Gelo", "tipo": "Água", "raridade": "Incomum", "ataque": 0, "defesa": 6, "mana": 3, "custo_habilidade": 2},
    "Carta_51": {"nome": "Dragão Ancião", "tipo": "Lava", "raridade": "Raro", "ataque": 7, "defesa": 6, "mana": 7, "custo_habilidade": 4},
    "Carta_52": {"nome": "Sacerdotisa da Luz", "tipo": "Luz", "raridade": "Incomum", "ataque": 2, "defesa": 4, "mana": 3, "custo_habilidade": 2},
    "Carta_53": {"nome": "Assassino das Sombras", "tipo": "Trevas", "raridade": "Raro", "ataque": 5, "defesa": 2, "mana": 4, "custo_habilidade": 3},
    "Carta_54": {"nome": "Centauro Veloz", "tipo": "Planície", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_55": {"nome": "Guardião Solar", "tipo": "Luz", "raridade": "Raro", "ataque": 4, "defesa": 5, "mana": 5, "custo_habilidade": 3},
    "Carta_56": {"nome": "Arcanista do Vento", "tipo": "Vento", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 4, "custo_habilidade": 2},
    "Carta_57": {"nome": "Gigante de Rocha", "tipo": "Terra", "raridade": "Raro", "ataque": 6, "defesa": 6, "mana": 6, "custo_habilidade": 3},
    "Carta_58": {"nome": "Caçadora da Selva", "tipo": "Floresta", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_59": {"nome": "Barreira Flamejante", "tipo": "Lava", "raridade": "Incomum", "ataque": 0, "defesa": 6, "mana": 3, "custo_habilidade": 2},
    "Carta_60": {"nome": "Falcão Mensageiro", "tipo": "Vento", "raridade": "Comum", "ataque": 1, "defesa": 2, "mana": 1, "custo_habilidade": 1},
    "Carta_61": {"nome": "Guardião das Raízes", "tipo": "Floresta", "raridade": "Incomum", "ataque": 2, "defesa": 5, "mana": 3, "custo_habilidade": 2},
    "Carta_62": {"nome": "Tartaruga Mística", "tipo": "Água", "raridade": "Raro", "ataque": 2, "defesa": 7, "mana": 4, "custo_habilidade": 3},
    "Carta_63": {"nome": "Guardiã dos Ventos", "tipo": "Vento", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_64": {"nome": "Besta Flamejante", "tipo": "Lava", "raridade": "Raro", "ataque": 5, "defesa": 3, "mana": 4, "custo_habilidade": 3},
    "Carta_65": {"nome": "Vidente da Névoa", "tipo": "Água", "raridade": "Incomum", "ataque": 2, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_66": {"nome": "Centelha de Luz", "tipo": "Luz", "raridade": "Comum", "ataque": 1, "defesa": 1, "mana": 1, "custo_habilidade": 1},
    "Carta_67": {"nome": "Estátua Viva", "tipo": "Terra", "raridade": "Comum", "ataque": 3, "defesa": 5, "mana": 3, "custo_habilidade": 0},
    "Carta_68": {"nome": "Fera de Sombras", "tipo": "Trevas", "raridade": "Raro", "ataque": 5, "defesa": 4, "mana": 5, "custo_habilidade": 3},
    "Carta_69": {"nome": "Bardo dos Ventos", "tipo": "Vento", "raridade": "Comum", "ataque": 1, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_70": {"nome": "Guardião de Cristal", "tipo": "Luz", "raridade": "Incomum", "ataque": 3, "defesa": 5, "mana": 4, "custo_habilidade": 2},
    "Carta_71": {"nome": "Lobisomem Feral", "tipo": "Trevas", "raridade": "Incomum", "ataque": 4, "defesa": 2, "mana": 3, "custo_habilidade": 2},
    "Carta_72": {"nome": "Arqueiro da Aurora", "tipo": "Luz", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_73": {"nome": "Sábio da Montanha", "tipo": "Terra", "raridade": "Raro", "ataque": 2, "defesa": 6, "mana": 4, "custo_habilidade": 3},
    "Carta_74": {"nome": "Salamandra Escaldante", "tipo": "Lava", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_75": {"nome": "Guardião da Selva", "tipo": "Floresta", "raridade": "Comum", "ataque": 2, "defesa": 4, "mana": 2, "custo_habilidade": 0},
    "Carta_76": {"nome": "Sacerdote da Tempestade", "tipo": "Vento", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_77": {"nome": "Guardião da Névoa", "tipo": "Água", "raridade": "Incomum", "ataque": 2, "defesa": 5, "mana": 3, "custo_habilidade": 2},
    "Carta_78": {"nome": "Espíritu Selvagem", "tipo": "Floresta", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_79": {"nome": "Guarda Real de Gondren", "tipo": "Planície", "raridade": "Raro", "ataque": 4, "defesa": 5, "mana": 5, "custo_habilidade": 3},
    "Carta_80": {"nome": "Serpente das Profundezas", "tipo": "Água", "raridade": "Raro", "ataque": 5, "defesa": 4, "mana": 5, "custo_habilidade": 3}
}


from habilidades_cartas import get_habilidade_por_id

def get_carta_by_id(carta_id: str) -> Carta:
    """
    Retorna uma instância da carta com base no ID informado.
    A habilidade é carregada do arquivo habilidades_cartas.py.
    """
    data = card_repository.get(carta_id)
    if not data:
        raise ValueError(f"ID de carta desconhecido: {carta_id}")
    return Carta(
        nome=data['nome'],
        custo_mana=data['mana'],
        ataque=data['ataque'],
        defesa=data['defesa'],
        habilidade=get_habilidade_por_id(carta_id),
        custo_habilidade=data.get('custo_habilidade', 0),
        tipo_terreno=data['tipo'],
        raridade=data['raridade']
    )
