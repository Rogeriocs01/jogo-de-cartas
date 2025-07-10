# recompensas_cartas.py

import json
import random
from inventario_jogador import adicionar_carta

def recompensar_vitoria():
    recompensas = gerar_recompensas_aleatorias()
    for carta in recompensas:
        adicionar_carta(carta)

    print(f"🎁 Recompensas adicionadas ao inventário global:")
    for carta in recompensas:
        print(f" - {carta}")

def gerar_recompensas_aleatorias():
    ids_possiveis = [f"Carta_{i}" for i in range(1, 81)]
    return random.sample(ids_possiveis, 2)
