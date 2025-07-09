from personagens_data import personagens

# Usamos os 20 primeiros personagens para gerar as 60 fases
personagens_base = personagens[:20]  # Garante consistência com a regra

def escolher_fase(fase_num):
    if fase_num < 1 or fase_num > 60:
        raise ValueError("Número de fase inválido (deve ser entre 1 e 60)")

    indice_personagem = (fase_num - 1) // 3  # Cada personagem aparece em 3 fases
    repeticao = (fase_num - 1) % 3           # Define a dificuldade

    personagem = personagens_base[indice_personagem]

    if repeticao == 0:
        dificuldade = "Fácil"
    elif repeticao == 1:
        dificuldade = "Médio"
    else:
        dificuldade = "Difícil"

    return {
        "nome": personagem["nome"],
        "dificuldade": dificuldade,
        "terreno": personagem["terreno"]  # ✅ Corrigido: 'terreno', não 'terreno_favorito'
    }
