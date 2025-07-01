# salvar_progresso.py
import json

CAMINHO_SAVE = "save_data.json"

def salvar_jogo(nome_heroi, deck, fase):
    dados = {
        "heroi": nome_heroi,
        "deck": [carta.id for carta in deck],
        "fase": fase
    }
    with open(CAMINHO_SAVE, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("💾 Progresso salvo com sucesso!")
