from progresso_heroi import get_bonus_da_habilidade

def curar_heroi(jogador, inimigo=None):
    bonus = get_bonus_da_habilidade(jogador.nome)
    total = 2 + bonus
    jogador.vida += total
    print(f"✨ {jogador.nome} recuperou {total} de vida! Vida atual: {jogador.vida}")

def dano_heroi(jogador, inimigo):
    bonus = get_bonus_da_habilidade(jogador.nome)
    total = 2 + bonus
    inimigo.vida -= total
    print(f"🔥 {inimigo.nome} sofreu {total} de dano direto! Vida restante: {inimigo.vida}")

def comprar_cartas(jogador, inimigo=None):
    bonus = get_bonus_da_habilidade(jogador.nome)
    total = 2 + bonus
    for _ in range(total):
        jogador.comprar_carta()
    print(f"📜 {jogador.nome} comprou {total} cartas.")

def reduzir_custo_mana(jogador, inimigo=None):
    bonus = get_bonus_da_habilidade(jogador.nome)
    desconto = 1 + bonus
    for carta in jogador.mao:
        carta.custo_mana = max(0, carta.custo_mana - desconto)
    print(f"🔷 {jogador.nome} reduziu o custo de mana das cartas na mão em {desconto}.")

def manipulacao_mana(jogador, inimigo=None):
    bonus = get_bonus_da_habilidade(jogador.nome)
    recuperado = 2 + bonus
    jogador.mana += recuperado
    print(f"🔷 {jogador.nome} recuperou {recuperado} de mana! Mana total: {jogador.mana}")

def reutilizar_habilidade(jogador, inimigo=None):
    for carta in jogador.campo:
        if carta:
            carta.habilidade_usada = False
    print(f"♻️ {jogador.nome} recarregou as habilidades de todas as cartas em campo.")

def espionagem(jogador, inimigo):
    print(f"🕵️ {jogador.nome} espionou a mão de {inimigo.nome}:")
    for idx, carta in enumerate(inimigo.mao):
        print(f"  - {idx + 1}: {carta.nome}")

def furto_temporario(jogador, inimigo):
    for i, carta in enumerate(inimigo.campo):
        if carta:
            for slot in range(5):
                if not jogador.campo[slot]:
                    jogador.campo[slot] = carta
                    print(f"🎭 {jogador.nome} roubou temporariamente {carta.nome} do inimigo!")
                    return
    print("⚠️ Nenhuma carta pôde ser furtada.")

# Mapeamento das habilidades por ID textual
heroi_habilidades = {
    "curar": curar_heroi,
    "dano_em_area": dano_heroi,
    "comprar_cartas": comprar_cartas,
    "reduzir_custo_mana": reduzir_custo_mana,
    "manipulacao_mana": manipulacao_mana,
    "reutilizar_habilidade": reutilizar_habilidade,
    "espionagem": espionagem,
    "furto_temporario": furto_temporario,
}

def executar_habilidade_heroi(nome_habilidade, jogador, inimigo, campo=None):
    habilidade = heroi_habilidades.get(nome_habilidade)
    if habilidade:
        habilidade(jogador, inimigo)
    else:
        print(f"❌ Habilidade {nome_habilidade} não implementada para heróis.")
