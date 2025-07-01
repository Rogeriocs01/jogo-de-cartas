# executores.py
from habilidades.comuns import (
    curar_jogador,
    dano_direto,
    buff_ataque_temporario,
    curar_aliado,
    dano_em_area,
    buff_floresta,
    buff_defesa_temporaria,
    debuff_defesa,
    debuff_em_um_inimigo,
    debuff_ataque,
    buff_condicional,
)

habilidades_implementadas = {
    "Carta_1": lambda c, j, i: buff_ataque_temporario(c, 1),
    "Carta_2": lambda c, j, i: curar_jogador(j, 2),
    "Carta_4": lambda c, j, i: dano_direto(i, 2),
    "Carta_5": lambda c, j, i: buff_defesa_temporaria(c, 1),
    "Carta_8": lambda c, j, i: curar_aliado(j, 2),
    "Carta_14": lambda c, j, i: debuff_defesa(i.campo[0], 1),
    "Carta_19": lambda c, j, i: buff_condicional(j, c, 'ataque', 1),
    "Carta_22": lambda c, j, i: buff_defesa_temporaria(c, 2),
    "Carta_24": lambda c, j, i: buff_ataque_temporario(c, 2),
    "Carta_27": lambda c, j, i: debuff_ataque(i.campo[0], 1),
    "Carta_30": lambda c, j, i: dano_em_area(i, 1),
    "Carta_34": lambda c, j, i: debuff_em_um_inimigo(i, 'defesa', 2),
    "Carta_36": lambda c, j, i: dano_direto(i, 3),
    "Carta_44": lambda c, j, i: buff_floresta(j, 1),
    "Carta_48": lambda c, j, i: buff_condicional(j, c, 'defesa', 2),
    "Carta_50": lambda c, j, i: buff_ataque_temporario(c, 3),
    "Carta_52": lambda c, j, i: curar_aliado(j, 3),
    "Carta_55": lambda c, j, i: debuff_em_um_inimigo(i, 'ataque', 2),
    "Carta_58": lambda c, j, i: curar_jogador(j, 4),
    "Carta_60": lambda c, j, i: debuff_defesa(i.campo[0], 3),
    "Carta_62": lambda c, j, i: buff_condicional(j, c, 'ataque', 2),
    "Carta_67": lambda c, j, i: debuff_ataque(i.campo[0], 3),
    "Carta_70": lambda c, j, i: buff_defesa_temporaria(c, 3),
    "Carta_72": lambda c, j, i: buff_ataque_temporario(c, 4),
    "Carta_73": lambda c, j, i: curar_aliado(j, 5),
    "Carta_74": lambda c, j, i: buff_condicional(j, c, 'defesa', 3),
    "Carta_75": lambda c, j, i: dano_em_area(i, 2),
    "Carta_76": lambda c, j, i: debuff_ataque(i.campo[0], 4),
    "Carta_77": lambda c, j, i: buff_floresta(j, 2),
    "Carta_78": lambda c, j, i: curar_aliado(j, 4),
    "Carta_79": lambda c, j, i: debuff_defesa(i.campo[0], 4),
    "Carta_80": lambda c, j, i: buff_condicional(j, c, 'ataque', 3),
    "Carta_3": lambda c, j, i: buff_ataque_temporario(c, 2),
    "Carta_10": lambda c, j, i: buff_defesa_temporaria(c, 1),
    "Carta_16": lambda c, j, i: debuff_ataque(i.campo[0], 2),
    "Carta_20": lambda c, j, i: dano_direto(i, 1),
    "Carta_28": lambda c, j, i: curar_jogador(j, 3),
    "Carta_37": lambda c, j, i: debuff_em_um_inimigo(i, 'defesa', 3),
}

# Cartas não implementadas ainda (placeholder genérico)
for i in range(1, 81):
    cid = f"Carta_{i}"
    if cid not in habilidades_implementadas:
        habilidades_implementadas[cid] = lambda *args: print("⚠️ Habilidade ainda não implementada.")
