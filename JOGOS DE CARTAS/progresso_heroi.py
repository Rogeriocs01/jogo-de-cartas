# progresso_heroi.py
import json
import os

CAMINHO_SALVAMENTO = "dados/progresso_herois.json"

# Garante que a pasta existe
os.makedirs("dados", exist_ok=True)

# XP necessário por nível
XP_POR_NIVEL = {
    1: 0,
    2: 100,
    3: 250,
    4: 500,
    5: 800,
    6: 1200,
    7: 1700,
    8: 2300,
    9: 3000,
    10: 3800
}

def carregar_progresso():
    if os.path.exists(CAMINHO_SALVAMENTO):
        with open(CAMINHO_SALVAMENTO, "r") as f:
            return json.load(f)
    return {}

def salvar_progresso(dados):
    with open(CAMINHO_SALVAMENTO, "w") as f:
        json.dump(dados, f, indent=4)

def inicializar_heroi(nome):
    progresso = carregar_progresso()
    if nome not in progresso:
        progresso[nome] = {"xp": 0, "nivel": 1}
        salvar_progresso(progresso)
    return progresso[nome]

def ganhar_xp(nome, quantidade):
    progresso = carregar_progresso()
    heroi = progresso.get(nome, {"xp": 0, "nivel": 1})
    heroi["xp"] += quantidade

    # Verifica se subiu de nível
    nivel_atual = heroi["nivel"]
    while nivel_atual < 10 and heroi["xp"] >= XP_POR_NIVEL[nivel_atual + 1]:
        nivel_atual += 1
        print(f"⬆️ {nome} subiu para o nível {nivel_atual}!")

    heroi["nivel"] = nivel_atual
    progresso[nome] = heroi
    salvar_progresso(progresso)
    return heroi

def get_bonus_da_habilidade(nome):
    progresso = carregar_progresso()
    heroi = progresso.get(nome, {"nivel": 1})
    nivel = heroi.get("nivel", 1)

    # Lógica simples: bônus = +1 por 3 níveis (até no máx. +3)
    if nivel >= 9:
        return 3
    elif nivel >= 5:
        return 2
    elif nivel >= 2:
        return 1
    return 0
