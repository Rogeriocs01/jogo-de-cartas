#inventario_jogador.py
import json
import os

CAMINHO_ARQUIVO = "inventario.json"

def carregar_inventario():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_inventario(inventario):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4)

def adicionar_carta(carta_id):
    inventario = carregar_inventario()

    if carta_id in inventario:
        inventario[carta_id] += 1
    else:
        inventario[carta_id] = 1

    salvar_inventario(inventario)

def mostrar_inventario():
    inventario = carregar_inventario()

    print(f"\n📜 Inventário de Cartas (global):")
    if not inventario:
        print("Nenhuma carta foi adquirida ainda.")
    else:
        for carta_id, quantidade in inventario.items():
            print(f"{carta_id} x{quantidade}")
