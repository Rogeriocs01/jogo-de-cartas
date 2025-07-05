# campanha/progresso.py
import json
import os

CAMINHO_PROGRESO = "dados/progresso_heroi.json"
os.makedirs("dados", exist_ok=True)


def carregar_progresso():
    if os.path.exists(CAMINHO_PROGRESO):
        with open(CAMINHO_PROGRESO, "r") as f:
            return json.load(f)
    return {}


def salvar_progresso(dados):
    with open(CAMINHO_PROGRESO, "w") as f:
        json.dump(dados, f, indent=4)


def ganhar_xp(nome_heroi, xp_ganho):
    progresso = carregar_progresso()
    status = progresso.get(nome_heroi, {"nivel": 1, "xp": 0})

    status["xp"] += xp_ganho
    while status["xp"] >= 100:
        status["xp"] -= 100
        status["nivel"] += 1
        print(f"✨ {nome_heroi} subiu para o nível {status['nivel']}!")

    progresso[nome_heroi] = status
    salvar_progresso(progresso)
