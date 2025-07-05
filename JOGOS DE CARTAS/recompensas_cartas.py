# recompensas_cartas.py
import json
import os
import random

CAMINHO_RECOMPENSAS = "dados/inventario_cartas.json"
os.makedirs("dados", exist_ok=True)

# Todas as cartas possíveis (nomes ou IDs simplificados)
TODAS_AS_CARTAS = [f"Carta_{i}" for i in range(1, 101)]

def carregar_inventario():
    if os.path.exists(CAMINHO_RECOMPENSAS):
        with open(CAMINHO_RECOMPENSAS, "r") as f:
            return json.load(f)
    return {}

def salvar_inventario(dados):
    with open(CAMINHO_RECOMPENSAS, "w") as f:
        json.dump(dados, f, indent=4)

def inicializar_inventario(nome_jogador):
    inventario = carregar_inventario()
    if nome_jogador not in inventario:
        inventario[nome_jogador] = []
        salvar_inventario(inventario)
    return inventario[nome_jogador]

def adicionar_cartas(nome_jogador, cartas):
    inventario = carregar_inventario()
    jogador_cartas = set(inventario.get(nome_jogador, []))
    novas_cartas = [c for c in cartas if c not in jogador_cartas]
    inventario[nome_jogador].extend(novas_cartas)
    salvar_inventario(inventario)
    return novas_cartas

def recompensar_vitoria(nome_jogador, quantidade=2):
    inventario = set(carregar_inventario().get(nome_jogador, []))
    elegiveis = list(set(TODAS_AS_CARTAS) - inventario)

    if not elegiveis:
        print("🎉 Você já desbloqueou todas as cartas!")
        return []

    recompensas = random.sample(elegiveis, min(quantidade, len(elegiveis)))
    adicionadas = adicionar_cartas(nome_jogador, recompensas)
    print(f"🎁 Recompensas recebidas: {', '.join(adicionadas)}")
    return adicionadas
