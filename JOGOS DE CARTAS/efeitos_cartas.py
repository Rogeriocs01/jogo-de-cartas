# efeitos_cartas.py

def efeito_dano_direto(jogador, alvo, quantidade=2):
    alvo.vida -= quantidade
    print(f"🔥 {jogador.nome} lançou um feitiço que causou {quantidade} de dano direto em {alvo.nome}!")

def efeito_cura(jogador, quantidade=3):
    jogador.vida += quantidade
    print(f"💖 {jogador.nome} lançou um feitiço de cura e recuperou {quantidade} de vida!")

def efeito_comprar_cartas(jogador, quantidade=2):
    for _ in range(quantidade):
        jogador.comprar_carta()
    print(f"🃏 {jogador.nome} comprou {quantidade} cartas com um feitiço!")

def efeito_buff_ataque(jogador, quantidade=1):
    for carta in jogador.campo:
        if carta:
            carta.ataque += quantidade
    print(f"💪 Todas as cartas de {jogador.nome} ganharam +{quantidade} de ATK temporariamente!")

def efeito_debuff_inimigo(inimigo, quantidade=1):
    for carta in inimigo.campo:
        if carta:
            carta.ataque = max(0, carta.ataque - quantidade)
    print(f"😵 As cartas de {inimigo.nome} perderam {quantidade} de ATK por um feitiço!")
