# habilidades_heroi.py

def curar_heroi(jogador, quantidade=3):
    jogador.vida += quantidade
    print(f"✨ {jogador.nome} usou sua habilidade especial e curou {quantidade} de vida! Vida atual: {jogador.vida}")

def dano_direto_no_inimigo(inimigo, quantidade=2):
    inimigo.vida -= quantidade
    print(f"🔥 Habilidade especial causou {quantidade} de dano direto a {inimigo.nome}! Vida restante: {inimigo.vida}")

def buffar_cartas_do_campo(jogador, stat='ataque', quantidade=1):
    for carta in jogador.campo:
        if carta:
            if stat == 'ataque':
                carta.ataque += quantidade
                print(f"💪 {carta.nome} recebe +{quantidade} ATK pela habilidade especial!")
            elif stat == 'defesa':
                carta.defesa += quantidade
                print(f"🛡️ {carta.nome} recebe +{quantidade} DEF pela habilidade especial!")

def enfraquecer_inimigo(inimigo, quantidade=1):
    for carta in inimigo.campo:
        if carta:
            carta.ataque -= quantidade
            print(f"🔻 {carta.nome} perde {quantidade} ATK por causa da habilidade especial!")

def comprar_cartas(jogador, quantidade=2):
    print(f"📦 {jogador.nome} compra {quantidade} cartas com sua habilidade especial!")
    for _ in range(quantidade):
        jogador.comprar_carta()

def reduzir_custo_mana(jogador):
    for carta in jogador.mao:
        carta.custo_mana = max(0, carta.custo_mana - 1)
    print(f"💰 Todas as cartas na mão de {jogador.nome} agora custam -1 de mana neste turno!")

def dano_em_area(inimigo, quantidade=1):
    for carta in inimigo.campo:
        if carta:
            carta.defesa -= quantidade
            print(f"💥 {carta.nome} sofreu {quantidade} de dano por habilidade especial!")
            if carta.defesa <= 0:
                print(f"☠️ {carta.nome} foi destruída!")
                index = inimigo.campo.index(carta)
                inimigo.campo[index] = None

# Mapeamento central
heroi_habilidades = {
    "curar": curar_heroi,
    "dano_direto": dano_direto_no_inimigo,
    "buff_aliados": buffar_cartas_do_campo,
    "debuff_inimigos": enfraquecer_inimigo,
    "comprar_cartas": comprar_cartas,
    "reduzir_custo_mana": reduzir_custo_mana,
    "dano_em_area": dano_em_area
}
