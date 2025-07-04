# habilidades_heroi.py
from progresso_heroi import get_bonus_da_habilidade

def curar_heroi(jogador, quantidade=2):
    bonus = get_bonus_da_habilidade(jogador.nome)
    total = quantidade + bonus
    jogador.vida += total
    print(f"✨ {jogador.nome} recuperou {total} de vida! Vida atual: {jogador.vida}")

def dano_heroi(inimigo, quantidade=2):
    bonus = get_bonus_da_habilidade(inimigo.nome)
    total = quantidade + bonus
    inimigo.vida -= total
    print(f"🔥 {inimigo.nome} sofreu {total} de dano direto! Vida restante: {inimigo.vida}")

def comprar_cartas(jogador, quantidade=2):
    bonus = get_bonus_da_habilidade(jogador.nome)
    total = quantidade + bonus
    for _ in range(total):
        jogador.comprar_carta()

def reduzir_custo_mana(jogador):
    bonus = get_bonus_da_habilidade(jogador.nome)
    for carta in jogador.mao:
        carta.custo_mana = max(0, carta.custo_mana - 1 - bonus)
    print(f"🔷 Custo de mana das cartas da mão reduzido em {1 + bonus}!")

def manipulacao_mana(jogador):
    bonus = get_bonus_da_habilidade(jogador.nome)
    total = 2 + bonus
    jogador.mana += total
    print(f"🔷 {jogador.nome} recuperou {total} de mana adicionais! Mana total: {jogador.mana}")

def reutilizar_habilidade(jogador):
    for carta in jogador.campo:
        if carta:
            carta.habilidade_usada = False
    print("♻️ Todas as habilidades das cartas em campo foram recarregadas!")

def espionagem(jogador, inimigo):
    print(f"🕵️ {jogador.nome} espionou a mão de {inimigo.nome}:")
    for idx, carta in enumerate(inimigo.mao):
        print(f"  - {idx + 1}: {carta.nome}")

def furto_temporario(jogador, inimigo):
    for i, carta in enumerate(inimigo.campo):
        if carta:
            copia = carta  # Compartilha referência por 1 turno
            for slot in range(5):
                if not jogador.campo[slot]:
                    jogador.campo[slot] = copia
                    print(f"🎭 {jogador.nome} roubou temporariamente {carta.nome} do inimigo!")
                    return
    print("⚠️ Não foi possível furtar nenhuma carta.")

heroi_habilidades = {
    "curar": curar_heroi,
    "dano": dano_heroi,
    "comprar_cartas": comprar_cartas,
    "reduzir_custo_mana": reduzir_custo_mana,
    "manipulacao_mana": manipulacao_mana,
    "reutilizar_habilidade": reutilizar_habilidade,
    "espionagem": espionagem,
    "furto_temporario": furto_temporario,
}
