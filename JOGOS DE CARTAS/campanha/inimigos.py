# campanha/inimigos.py
from personagens_data import personagens

def get_personagem_info(nome_personagem, dificuldade=None):
    for p in personagens:
        if str(p["nome"]) in str(nome_personagem) or str(nome_personagem) in str(p["nome"]):
            info = p.copy()

            # Adiciona vida e tamanho de deck conforme a dificuldade
            if dificuldade == "Fácil":
                info["vida"] = 20
                info["deck_size"] = 10
            elif dificuldade == "Médio":
                info["vida"] = 25
                info["deck_size"] = 15
            else:  # Difícil e Chefe
                info["vida"] = 30
                info["deck_size"] = 20

            return info

    raise ValueError(f"Personagem não encontrado: {nome_personagem}")
