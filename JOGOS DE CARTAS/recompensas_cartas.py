import json
import os
from inventario_jogador import carregar_inventario, salvar_inventario

def adicionar_cartas(nome_jogador, novas_cartas):
    inventario = carregar_inventario()

    if nome_jogador not in inventario or not isinstance(inventario[nome_jogador], dict):
        inventario[nome_jogador] = {}

    for carta in novas_cartas:
        if carta in inventario[nome_jogador]:
            inventario[nome_jogador][carta] += 1
        else:
            inventario[nome_jogador][carta] = 1

    # ✅ Salvando com o inventário atualizado
    salvar_inventario(inventario)
    return novas_cartas

def recompensar_vitoria(nome_jogador):
    recompensas = gerar_recompensas_aleatorias()
    adicionadas = adicionar_cartas(nome_jogador, recompensas)
    print(f"🎁 Recompensas adicionadas ao inventário de {nome_jogador}:")
    for carta in adicionadas:
        print(f" - {carta}")

def gerar_recompensas_aleatorias():
    import random
    ids_possiveis = [f"Carta_{i}" for i in range(1, 81)]
    return random.sample(ids_possiveis, 2)
