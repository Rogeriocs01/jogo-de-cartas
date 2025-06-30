# mapa.py

from personagens_data import personagens

def escolher_fase(progresso):
    total = len(personagens) * 3
    proxima = progresso + 1

    if proxima > total:
        print("Você já completou todas as fases!")
        return None

    idx = progresso // 3
    diff = progresso % 3

    personagem = personagens[idx]
    nome = personagem["nome"]
    terreno = personagem["terreno_favorito"]
    buff = personagem["buffs"][diff]
    dificuldade = ["Fácil", "Médio", "Difícil"][diff]

    print(f"\n=== PRÓXIMA FASE: {proxima}/{total} — {nome} ({dificuldade}) | Terreno: {terreno} ===")
    confirm = input("Pressione ENTER para iniciar esta fase ou 'm' para voltar ao menu: ")

    if confirm.lower() == "m":
        return None

    return {
        "nome": nome,
        "buff": buff,
        "dificuldade": dificuldade,
        "terreno": terreno
    }
