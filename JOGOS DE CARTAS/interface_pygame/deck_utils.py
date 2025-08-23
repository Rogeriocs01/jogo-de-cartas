import json
import os

CAMINHO_DADOS_HEROIS = os.path.join("dados", "herois")
CAMINHO_DECKS = "dados"
CAMINHO_INVENTARIO = os.path.join("interface_pygame", "inventario.json")


def carregar_inventario():
    with open(CAMINHO_INVENTARIO, "r", encoding="utf-8") as f:
        return json.load(f)


def carregar_nivel_heroi(nome_heroi):
    caminho = os.path.join(CAMINHO_DADOS_HEROIS, f"{nome_heroi}.json")
    if not os.path.exists(caminho):
        return 1
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
        return dados.get("nivel", 1)


def salvar_deck(nome_heroi, deck):
    caminho = os.path.join(CAMINHO_DECKS, f"deck_{nome_heroi}.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(deck, f, indent=4, ensure_ascii=False)
