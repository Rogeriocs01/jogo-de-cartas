# Creating a corrected full `card_repository.py` file with complete entries and filename slugging.
# The file will be written to /mnt/data/card_repository_final.py for you to download.
from cartas.carta import Carta
from batalha.habilidade_cartas import get_habilidade_por_id
import unicodedata
import re

# Raw card data (display names, stats)
card_repository = {
    "Carta_1": {"nome": "Dragão de Lava", "arquivo": "dragao_de_lava.webp", "tipo": "Lava", "raridade": "Raro", "ataque": 7, "defesa": 5, "mana": 6,  "custo_habilidade": 3},
    "Carta_2": {"nome": "Sentinela de Água", "arquivo": "sentinela_de_agua.webp", "tipo": "Água", "raridade": "Comum", "ataque": 2, "defesa": 4, "mana": 2, "custo_habilidade": 1},
    "Carta_3": {"nome": "Golem de Pedra", "arquivo": "golem_de_pedra.webp", "tipo": "Terra", "raridade": "Comum", "ataque": 3, "defesa": 6, "mana": 3,  "custo_habilidade": 1},
    "Carta_4": {"nome": "Fada da Luz", "tipo": "Luz", "arquivo": "fada_da_luz.webp", "raridade": "Incomum", "ataque": 1, "defesa": 2, "mana": 2, "custo_habilidade": 2},
    "Carta_5": {"nome": "Espectro das Sombras","arquivo": "espectro_das_sombras.webp", "tipo": "Trevas", "raridade": "Raro", "ataque": 5, "defesa": 3, "mana": 4, "custo_habilidade": 3},
    "Carta_6": {"nome": "Mago de Fogo","arquivo": "mago_de_fogo.webp", "tipo": "Lava", "raridade": "Comum", "ataque": 4, "defesa": 2, "mana": 3, "custo_habilidade": 1},
    "Carta_7": {"nome": "Guardião da Floresta", "arquivo": "guardiao_da_floresta.webp", "tipo": "Floresta", "raridade": "Incomum", "ataque": 2, "defesa": 5, "mana": 3, "custo_habilidade": 2},
    "Carta_8": {"nome": "Sereia Encantadora", "arquivo": "sereia_encantadora.webp", "tipo": "Água", "raridade": "Raro", "ataque": 3, "defesa": 4, "mana": 4,  "custo_habilidade": 3},
    "Carta_9": {"nome": "Espadachim Élfico", "arquivo": "espadachim_elfico.webp", "tipo": "Floresta", "raridade": "Comum", "ataque": 3, "defesa": 3, "mana": 2, "custo_habilidade": 1},
    "Carta_10": {"nome": "Anjo Guardião", "arquivo": "anjo_guardiao.webp", "tipo": "Luz", "raridade": "Raro", "ataque": 4, "defesa": 6, "mana": 5, "custo_habilidade": 3},
    "Carta_11": {"nome": "Lobo da Nevasca", "arquivo": "lobo_da_nevasca.webp", "tipo": "Vento", "raridade": "Incomum", "ataque": 3, "defesa": 2, "mana": 3, "custo_habilidade": 2},
    "Carta_12": {"nome": "Curandeiro de Elmswood", "arquivo": "curandeiro_de_elmswood.webp", "tipo": "Floresta", "raridade": "Comum", "ataque": 1, "defesa": 4, "mana": 2, "custo_habilidade": 1},
    "Carta_13": {"nome": "Guardião de Rocha", "arquivo": "guardiao_de_rocha.webp", "tipo": "Terra", "raridade": "Incomum", "ataque": 2, "defesa": 5, "mana": 4, "custo_habilidade": 2},
    "Carta_14": {"nome": "Goblin Selvagem", "arquivo": "goblin_selvagem.webp", "tipo": "Lava", "raridade": "Comum", "ataque": 2, "defesa": 1, "mana": 1, "custo_habilidade": 1},
    "Carta_15": {"nome": "Serpente da Água", "arquivo": "serpente_da_agua.webp", "tipo": "Água", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_16": {"nome": "Árvore Ancestral", "arquivo": "arvore_ancestral.webp", "tipo": "Floresta", "raridade": "Raro", "ataque": 2, "defesa": 7, "mana": 5, "custo_habilidade": 3},
    "Carta_17": {"nome": "Escudeiro da Planície", "arquivo": "escudeiro_da_planice.webp", "tipo": "Planície", "raridade": "Comum", "ataque": 2, "defesa": 3, "mana": 2, "custo_habilidade": 1},
    "Carta_18": {"nome": "Bomba Viva", "arquivo": "bomba_viva.webp", "tipo": "Lava", "raridade": "Incomum", "ataque": 3, "defesa": 2, "mana": 4, "custo_habilidade": 2},
    "Carta_19": {"nome": "Guerreiro de Gondren", "arquivo": "guerreiro_de_gondren.webp", "tipo": "Planície", "raridade": "Comum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 1},
    "Carta_20": {"nome": "Ilusionista Etéreo", "arquivo": "ilusionista_etereo.webp", "tipo": "Vento", "raridade": "Raro", "ataque": 2, "defesa": 3, "mana": 4, "custo_habilidade": 3},
    "Carta_21": {"nome": "Guardião da Luz", "arquivo": "guardiao_da_luz.webp", "tipo": "Luz", "raridade": "Raro", "ataque": 4, "defesa": 5, "mana": 5, "custo_habilidade": 3},
    "Carta_22": {"nome": "Elemental de Água", "arquivo": "elemental_de_agua.webp", "tipo": "Água", "raridade": "Incomum", "ataque": 3, "defesa": 4, "mana": 3, "custo_habilidade": 2},
    "Carta_23": {"nome": "Cavaleiro da Tempestade", "arquivo": "cavaleiro_da_tempestade.webp", "tipo": "Vento", "raridade": "Raro", "ataque": 5, "defesa": 3, "mana": 5, "custo_habilidade": 3},
    "Carta_24": {"nome": "Espreitador Sombrio", "arquivo": "espreitador_sombrio.webp", "tipo": "Trevas", "raridade": "Incomum", "ataque": 3, "defesa": 2, "mana": 3, "custo_habilidade": 2},
    "Carta_25": {"nome": "Guardião Subterrâneo", "arquivo": "guardiao_subterraneo.webp", "tipo": "Terra", "raridade": "Comum", "ataque": 2, "defesa": 4, "mana": 2, "custo_habilidade": 1},
    "Carta_26": {"nome": "Feiticeira da Lua", "arquivo": "feiticeira_da_lua.webp", "tipo": "Trevas", "raridade": "Raro", "ataque": 3, "defesa": 4, "mana": 4, "custo_habilidade": 3},
    "Carta_27": {"nome": "Águia Celeste", "arquivo": "aguia_celeste.webp", "tipo": "Vento", "raridade": "Comum", "ataque": 2, "defesa": 2, "mana": 1, "custo_habilidade": 1},
    "Carta_28": {"nome": "Lança de Chamas", "arquivo": "lanca_de_chamas.webp", "tipo": "Lava", "raridade": "Incomum", "ataque": 5, "defesa": 1, "mana": 4, "custo_habilidade": 2},
    "Carta_29": {"nome": "Xamã Tribal", "arquivo": "xama_tribal.webp", "tipo": "Floresta", "raridade": "Incomum", "ataque": 2, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_30": {"nome": "Guardião Glacial", "arquivo": "guardiao_glacial.webp", "tipo": "Água", "raridade": "Raro", "ataque": 4, "defesa": 6, "mana": 5, "custo_habilidade": 3},
    "Carta_31": {"nome": "Guardião das Dunas", "arquivo": "guardiao_das_dunas.webp", "tipo": "Planície", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_32": {"nome": "Dragão Etéreo", "arquivo": "dragao_etereo.webp", "tipo": "Vento", "raridade": "Raro", "ataque": 6, "defesa": 4, "mana": 6, "custo_habilidade": 4},
    "Carta_33": {"nome": "Fênix Incandescente", "arquivo": "fenix_incandecente.webp", "tipo": "Lava", "raridade": "Raro", "ataque": 5, "defesa": 3, "mana": 5, "custo_habilidade": 3},
    "Carta_34": {"nome": "Oráculo das Marés", "arquivo": "oraculo_das_mares.webp", "tipo": "Água", "raridade": "Incomum", "ataque": 2, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_35": {"nome": "Vigia da Penumbra", "arquivo": "vigia_da_penumbra.webp", "tipo": "Trevas", "raridade": "Incomum", "ataque": 2, "defesa": 2, "mana": 2, "custo_habilidade": 2},
    "Carta_36": {"nome": "Sentinela Celeste", "arquivo": "sentinela_celeste.webp", "tipo": "Luz", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_37": {"nome": "Clérigo Curador", "arquivo": "clerigo_curador.webp", "tipo": "Luz", "raridade": "Comum", "ataque": 1, "defesa": 3, "mana": 3, "custo_habilidade": 1},
    "Carta_38": {"nome": "Muralha de Espinhos", "arquivo": "muralha_de_espinhos.webp", "tipo": "Floresta", "raridade": "Incomum", "ataque": 0, "defesa": 6, "mana": 3, "custo_habilidade": 2},
    "Carta_39": {"nome": "Cavaleiro Sagrado", "arquivo": "cavalheiro_sagrado.webp", "tipo": "Planície", "raridade": "Raro", "ataque": 4, "defesa": 4, "mana": 5, "custo_habilidade": 3},
    "Carta_40": {"nome": "Banshee Gritante", "arquivo": "banshee_gritante.webp", "tipo": "Trevas", "raridade": "Raro", "ataque": 5, "defesa": 2, "mana": 4, "custo_habilidade": 3},
    "Carta_41": {"nome": "Golem de Cristal", "arquivo": "golem_de_cristal.webp", "tipo": "Luz", "raridade": "Incomum", "ataque": 3, "defesa": 5, "mana": 4, "custo_habilidade": 2},
    "Carta_42": {"nome": "Feiticeiro do Relâmpago", "arquivo": "feiticeiro_relampago.webp", "tipo": "Vento", "raridade": "Raro", "ataque": 4, "defesa": 3, "mana": 5, "custo_habilidade": 3},
    "Carta_43": {"nome": "Escorpião de Areia", "arquivo": "escorpiao_de_areia.webp", "tipo": "Planície", "raridade": "Comum", "ataque": 2, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_44": {"nome": "Guardiã das Estrelas", "arquivo": "ardia_as_estrelas.webp", "tipo": "Luz", "raridade": "Raro", "ataque": 3, "defesa": 4, "mana": 5, "custo_habilidade": 3},
    "Carta_45": {"nome": "Demônio do Caos", "arquivo": "demonio_do_caos.webp", "tipo": "Trevas", "raridade": "Raro", "ataque": 6, "defesa": 3, "mana": 6, "custo_habilidade": 4},
    "Carta_46": {"nome": "Arqueiro Fantasma", "arquivo": "arqueiro_fantasma.webp", "tipo": "Trevas", "raridade": "Incomum", "ataque": 3, "defesa": 2, "mana": 3, "custo_habilidade": 2},
    "Carta_47": {"nome": "Guarda Real", "arquivo": "guarda_real.webp", "tipo": "Planície", "raridade": "Comum", "ataque": 2, "defesa": 4, "mana": 2, "custo_habilidade": 1},
    "Carta_48": {"nome": "Serpente do Trovão", "arquivo": "serpente_do_trovao.webp", "tipo": "Vento", "raridade": "Raro", "ataque": 5, "defesa": 2, "mana": 5, "custo_habilidade": 3},
    "Carta_49": {"nome": "Caçadora de Alias", "arquivo": "cacadora_de_alias.webp", "tipo": "Trevas", "raridade": "Raro", "ataque": 4, "defesa": 3, "mana": 4, "custo_habilidade": 2},
    "Carta_50": {"nome": "Barreira de Gelo", "arquivo": "barreira_de_gelo.webp", "tipo": "Água", "raridade": "Incomum", "ataque": 0, "defesa": 6, "mana": 3, "custo_habilidade": 2},
    "Carta_51": {"nome": "Dragão Ancião", "arquivo": "dragao_anciao.webp", "tipo": "Lava", "raridade": "Raro", "ataque": 7, "defesa": 6, "mana": 7, "custo_habilidade": 4},
    "Carta_52": {"nome": "Sacerdotisa da Luz", "arquivo": "sacerdotisa_da_luz.webp", "tipo": "Luz", "raridade": "Incomum", "ataque": 2, "defesa": 4, "mana": 3, "custo_habilidade": 2},
    "Carta_53": {"nome": "Assassino das Sombras", "arquivo": "assassino_das_sombras.webp", "tipo": "Trevas", "raridade": "Raro", "ataque": 5, "defesa": 2, "mana": 4, "custo_habilidade": 3},
    "Carta_54": {"nome": "Centauro Veloz", "arquivo": "centauro_veloz.webp", "tipo": "Planície", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_55": {"nome": "Guardião Solar", "arquivo": "guardiao_solar.webp", "tipo": "Luz", "raridade": "Raro", "ataque": 4, "defesa": 5, "mana": 5, "custo_habilidade": 3},
    "Carta_56": {"nome": "Arcanista do Vento", "arquivo": "arcanista_do_vento.webp", "tipo": "Vento", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 4, "custo_habilidade": 2},
    "Carta_57": {"nome": "Gigante de Rocha", "arquivo": "gigante_de_rocha.webp", "tipo": "Terra", "raridade": "Raro", "ataque": 6, "defesa": 6, "mana": 6, "custo_habilidade": 3},
    "Carta_58": {"nome": "Caçadora da Selva", "arquivo": "cacadora_da_selva.webp", "tipo": "Floresta", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_59": {"nome": "Barreira Flamejante", "arquivo": "barreira_flamejante.webp", "tipo": "Lava", "raridade": "Incomum", "ataque": 0, "defesa": 6, "mana": 3, "custo_habilidade": 2},
    "Carta_60": {"nome": "Falcão Mensageiro", "arquivo": "falcao_mensageiro.webp", "tipo": "Vento", "raridade": "Comum", "ataque": 1, "defesa": 2, "mana": 1, "custo_habilidade": 1},
    "Carta_61": {"nome": "Guardião das Raízes", "arquivo": "guardao_das_raizes.webp", "tipo": "Floresta", "raridade": "Incomum", "ataque": 2, "defesa": 5, "mana": 3, "custo_habilidade": 2},
    "Carta_62": {"nome": "Tartaruga Mística", "arquivo": "tartaruga_mistica.webp", "tipo": "Água", "raridade": "Raro", "ataque": 2, "defesa": 7, "mana": 4, "custo_habilidade": 3},
    "Carta_63": {"nome": "Guardiã dos Ventos", "arquivo": "guardia_dos_ventos.webp", "tipo": "Vento", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_64": {"nome": "Besta Flamejante", "arquivo": "besta_flamejante.webp", "tipo": "Lava", "raridade": "Raro", "ataque": 5, "defesa": 3, "mana": 4, "custo_habilidade": 3},
    "Carta_65": {"nome": "Vidente da Névoa", "arquivo": "vidente_da_nevoa.webp", "tipo": "Água", "raridade": "Incomum", "ataque": 2, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_66": {"nome": "Centelha de Luz", "arquivo": "centelha_de_luz.webp", "tipo": "Luz", "raridade": "Comum", "ataque": 1, "defesa": 1, "mana": 1, "custo_habilidade": 1},
    "Carta_67": {"nome": "Estátua Viva", "arquivo": "estatuta_viva.webp", "tipo": "Terra", "raridade": "Comum", "ataque": 3, "defesa": 5, "mana": 3, "custo_habilidade": 0},
    "Carta_68": {"nome": "Fera de Sombras", "arquivo": "fera_de_sombras.webp", "tipo": "Trevas", "raridade": "Raro", "ataque": 5, "defesa": 4, "mana": 5, "custo_habilidade": 3},
    "Carta_69": {"nome": "Bardo dos Ventos", "arquivo": "bardo_dos_ventos.webp", "tipo": "Vento", "raridade": "Comum", "ataque": 1, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_70": {"nome": "Guardião de Cristal", "arquivo": "guardiao_de_cristal.webp", "tipo": "Luz", "raridade": "Incomum", "ataque": 3, "defesa": 5, "mana": 4, "custo_habilidade": 2},
    "Carta_71": {"nome": "Lobisomem Feral", "arquivo": "lobisomem_feral.webp", "tipo": "Trevas", "raridade": "Incomum", "ataque": 4, "defesa": 2, "mana": 3, "custo_habilidade": 2},
    "Carta_72": {"nome": "Arqueiro da Aurora", "arquivo": "arqueiro_da_aurora.webp", "tipo": "Luz", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_73": {"nome": "Sábio da Montanha", "arquivo": "sabio_da_montanha.webp", "tipo": "Terra", "raridade": "Raro", "ataque": 2, "defesa": 6, "mana": 4, "custo_habilidade": 3},
    "Carta_74": {"nome": "Salamandra Escaldante", "arquivo": "salamandra_escaldante.webp", "tipo": "Lava", "raridade": "Comum", "ataque": 3, "defesa": 2, "mana": 2, "custo_habilidade": 1},
    "Carta_75": {"nome": "Guardião da Selva", "arquivo": "guardiao_da_selva.webp", "tipo": "Floresta", "raridade": "Comum", "ataque": 2, "defesa": 4, "mana": 2, "custo_habilidade": 0},
    "Carta_76": {"nome": "Sacerdote da Tempestade", "arquivo": "sacerdote_da_tempestade.webp", "tipo": "Vento", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_77": {"nome": "Guardião da Névoa", "arquivo": "guardiao_da_nevoa.webp", "tipo": "Água", "raridade": "Incomum", "ataque": 2, "defesa": 5, "mana": 3, "custo_habilidade": 2},
    "Carta_78": {"nome": "Espírito Selvagem", "arquivo": "espirito_selvagem.webp", "tipo": "Floresta", "raridade": "Incomum", "ataque": 3, "defesa": 3, "mana": 3, "custo_habilidade": 2},
    "Carta_79": {"nome": "Guarda Real de Gondren", "arquivo": "guarda_real.webp", "tipo": "Planície", "raridade": "Raro", "ataque": 4, "defesa": 5, "mana": 5, "custo_habilidade": 3},
    "Carta_80": {"nome": "Serpente das Profundezas", "arquivo": "serpente_das_profundezas.webp", "tipo": "Água", "raridade": "Raro", "ataque": 5, "defesa": 4, "mana": 5, "custo_habilidade": 3},
    "Carta_81": {"nome": "Bola de Fogo", "arquivo": "bola_de_fogo.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "rara", "efeito": "efeito_dano_direto"},
    "Carta_82": {"nome": "Raio Sombrio", "arquivo": "raio_sombrio.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "rara", "efeito": "efeito_dano_direto"},
    "Carta_83": {"nome": "Explosão Arcana", "arquivo": "explosao_arcana.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_dano_direto"},
    "Carta_84": {"nome": "Sopro Flamejante", "arquivo": "sopro_flamejante.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum","efeito": "efeito_dano_direto"},
    "Carta_85": {"nome": "Poção de Vida", "arquivo": "pocao_de_vida.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_cura"},
    "Carta_86": {"nome": "Luz Restauradora", "arquivo": "luz_restauradora.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "rara", "efeito": "efeito_cura"},
    "Carta_87": {"nome": "Alívio Espiritual", "arquivo": "alivio_espiritual.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_cura"},
    "Carta_88": {"nome": "Benção da Luz", "arquivo": "bencao_de_luz.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "épica", "efeito": "efeito_cura"},
    "Carta_89": {"nome": "Inspiração", "arquivo": "inspiracao.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_comprar_cartas"},
    "Carta_90": {"nome": "Clarividência", "arquivo": "clarividencia.webp", "mana": 3,"ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "rara", "efeito": "efeito_comprar_cartas"},
    "Carta_91": {"nome": "Sabedoria Antiga", "arquivo": "sabedoria_antiga.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_comprar_cartas"},
    "Carta_92": {"nome": "Olhar do Oráculo", "arquivo": "olhar_do_oraculo.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "épica", "efeito": "efeito_comprar_cartas"},
    "Carta_93": {"nome": "Fúria Bélica", "arquivo": "furia_belica.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_buff_ataque"},
    "Carta_94": {"nome": "Abençoar Guerreiros", "arquivo": "abencoar_guerreiros.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "rara", "efeito": "efeito_buff_ataque"},
    "Carta_95": {"nome": "Força das Sombras", "arquivo": "forca_das_sombras.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_buff_ataque"},
    "Carta_96": {"nome": "Grito de Guerra", "arquivo": "grito_de_guerra.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "épica", "efeito": "efeito_buff_ataque"},
    "Carta_97": {"nome": "Névoa Confusa", "arquivo": "nevoa_confusa.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_debuff_inimigo"},
    "Carta_98": {"nome": "Toque do Medo", "arquivo": "toque_do_medo.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "rara", "efeito": "efeito_debuff_inimigo"},
    "Carta_99": {"nome": "Terror Silencioso", "arquivo": "terror_silencioso.webp", "mana": 2, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "comum", "efeito": "efeito_debuff_inimigo"},
    "Carta_100":{"nome": "Enfraquecer Exército", "arquivo": "enfraquecer_exercito.webp", "mana": 3, "ataque": 0, "defesa": 0, "tipo": "efeito", "raridade": "épica", "efeito": "efeito_debuff_inimigo"},
    "Carta_Debug_1": {"nome": "Debugador Supremo 1", "arquivo": "debugador_supremo_1.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_2": {"nome": "Debugador Supremo 2", "arquivo": "debugador_supremo_2.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_3": {"nome": "Debugador Supremo 3", "arquivo": "debugador_supremo_3.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_4": {"nome": "Debugador Supremo 4", "arquivo": "debugador_supremo_4.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_5": {"nome": "Debugador Supremo 5", "arquivo": "debugador_supremo_5.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_6": {"nome": "Debugador Supremo 6", "arquivo": "debugador_supremo_6.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_7": {"nome": "Debugador Supremo 7", "arquivo": "debugador_supremo_7.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_8": {"nome": "Debugador Supremo 8", "arquivo": "debugador_supremo_8.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_9": {"nome": "Debugador Supremo 9", "arquivo": "debugador_supremo_9.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0},
    "Carta_Debug_10": {"nome": "Debugador Supremo 10", "arquivo": "debugador_supremo_10.webp", "tipo": "Código", "raridade": "Lendária", "ataque": 99, "defesa": 99, "mana": 1, "custo_habilidade": 0}
}

def _slugify(nome: str) -> str:
    """Create filename-friendly slug from display name. e.g. 'Dragão de Lava' -> 'dragao_de_lava'"""
    if not nome:
        return ""
    # Normalize accents
    s = unicodedata.normalize('NFKD', nome)
    s = s.encode('ascii', 'ignore').decode('ascii')
    # Lowercase, remove non-alnum (keep spaces and hyphens), replace spaces with underscore
    s = re.sub(r'[^a-zA-Z0-9\s-]', '', s).strip().lower()
    s = re.sub(r'\s+', '_', s)
    return s

# Inject 'arquivo' (filename without extension) into each card's data for convenience
for cid, data in card_repository.items():
    data.setdefault('arquivo', _slugify(data.get('nome', cid)))

def get_carta_by_id(carta_id):
    """
    Return a Carta instance for the given card id (e.g. 'Carta_1').
    If the card doesn't exist, return None.
    """
    data = card_repository.get(carta_id)
    if not data:
        return None

    carta = Carta(
        id=carta_id,
        nome=data.get("nome"),
        custo_mana=data.get("mana", 0),
        ataque=data.get("ataque", 0),
        defesa=data.get("defesa", 0),
        habilidade=get_habilidade_por_id(carta_id),
        custo_habilidade=data.get("custo_habilidade", 0),
        tipo_terreno=data.get("tipo"),
        raridade=data.get("raridade")
    )
    # attach arquivo slug so callers can know the image filename: <arquivo>.webp
    setattr(carta, "arquivo", data.get("arquivo"))
    return carta

def get_carta_by_nome(nome):
    """
    Accepts display name (e.g. 'Dragão de Lava') or slug ('dragao_de_lava')
    and returns a Carta instance or None.
    """
    if not nome:
        return None
    # Try exact display name match first
    for cid, data in card_repository.items():
        if data.get("nome") == nome:
            return get_carta_by_id(cid)
    # Try slug match
    slug = _slugify(nome)
    for cid, data in card_repository.items():
        if data.get("arquivo") == slug:
            return get_carta_by_id(cid)
    return None


