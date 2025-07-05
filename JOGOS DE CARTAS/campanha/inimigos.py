# campanha/inimigos.py
from personagens_data import personagens

def get_personagem_info(nome_personagem):
    for p in personagens:
        if str(p["nome"]) in str(nome_personagem) or str(nome_personagem) in str(p["nome"]):
            return p
    raise ValueError(f"Personagem não encontrado: {nome_personagem}")
