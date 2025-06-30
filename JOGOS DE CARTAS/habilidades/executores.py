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
    "Carta_1": lambda c, j, i: buff_ataque_temporario(c, 1),          # Investida
    "Carta_2": lambda c, j, i: curar_jogador(j, 2),                   # Regenerar
    "Carta_4": lambda c, j, i: dano_direto(i, 2),                     # Explosão
    "Carta_5": lambda c, j, i: buff_defesa_temporaria(c, 1),         # Resistência
    "Carta_8": lambda c, j, i: curar_aliado(j, 2),                    # Curar aliado
    "Carta_14": lambda c, j, i: debuff_defesa(i.campo[0], 1),        # Apodrecer (primeiro inimigo)
    "Carta_19": lambda c, j, i: buff_condicional(j, c, 'ataque', 1), # Moral Alta
    "Carta_30": lambda c, j, i: dano_em_area(i, 1),                   # Erupção
    "Carta_34": lambda c, j, i: debuff_em_um_inimigo(i, 'defesa', 2),# Olhar Assombrado
    "Carta_44": lambda c, j, i: buff_floresta(j, 1),                 # Ira Selvagem
    "Carta_55": lambda c, j, i: debuff_em_um_inimigo(i, 'ataque', 2),# Olhar Sombrio
}

# Cartas não implementadas ainda (placeholder genérico)
for i in range(1, 81):
    cid = f"Carta_{i}"
    if cid not in habilidades_implementadas:
        habilidades_implementadas[cid] = lambda *args: print("⚠️ Habilidade ainda não implementada.")
