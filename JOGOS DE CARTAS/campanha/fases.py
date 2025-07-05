# campanha/fases.py

def escolher_fase(fase_num):
    if fase_num % 5 == 0:
        dificuldade = "Chefe"
    elif fase_num % 4 == 0:
        dificuldade = "Difícil"
    elif fase_num % 2 == 0:
        dificuldade = "Médio"
    else:
        dificuldade = "Fácil"

    personagens_fase = [
        {"nome": "Thorin", "terreno_favorito": "Lava"},
        {"nome": "Eldrin", "terreno_favorito": "Gelo"},
        {"nome": "Lunara", "terreno_favorito": "Floresta"},
        {"nome": "Grumak", "terreno_favorito": "Terra"},
        {"nome": "Zarok", "terreno_favorito": "Sombra"},
    ]

    personagem = personagens_fase[fase_num % len(personagens_fase)]
    return {
        "nome": personagem["nome"],
        "dificuldade": dificuldade,
        "terreno_favorito": personagem["terreno_favorito"]
    }
