# carregar_progresso.py
import json
import os
from card_repository import get_carta_by_id

CAMINHO_SAVE = "save_data.json"

def carregar_jogo():
    if not os.path.exists(CAMINHO_SAVE):
        print("📂 Nenhum progresso salvo encontrado.")
        return None

    with open(CAMINHO_SAVE, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    nome_heroi = dados.get("heroi")
    deck_ids = dados.get("deck", [])
    fase = dados.get("fase", 0)

    deck = [get_carta_by_id(carta_id) for carta_id in deck_ids]

    print("✅ Progresso carregado com sucesso!")
    return nome_heroi, deck, fase
