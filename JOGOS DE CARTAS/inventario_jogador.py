import json
import os

CAMINHO_ARQUIVO = "inventario.json"

inventario = {}

def carregar_inventario():
    global inventario
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
            inventario = json.load(f)
    else:
        inventario = {}
    return inventario  # ✅ Retorna para que outros módulos possam usá-lo

def salvar_inventario(inventario_atualizado):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(inventario_atualizado, f, indent=4)

def adicionar_carta(carta_id, nome_heroi):
    inventario = carregar_inventario()

    if nome_heroi not in inventario:
        inventario[nome_heroi] = {}

    if carta_id in inventario[nome_heroi]:
        inventario[nome_heroi][carta_id] += 1
    else:
        inventario[nome_heroi][carta_id] = 1

    salvar_inventario(inventario)

def mostrar_inventario(nome_heroi):
    inventario = carregar_inventario()

    print(f"\n📜 Inventário de Cartas de {nome_heroi}:")
    cartas = inventario.get(nome_heroi, {})
    if not cartas:
        print("Este herói ainda não possui cartas.")
    else:
        for carta_id, quantidade in cartas.items():
            print(f"{carta_id} x{quantidade}")
