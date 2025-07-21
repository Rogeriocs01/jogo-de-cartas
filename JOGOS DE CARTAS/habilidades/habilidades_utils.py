
# habilidades_utils.py

def dano_direto(inimigo, quantidade):
    inimigo.vida -= quantidade
    print(f'Dano direto de {quantidade} no inimigo! Vida restante: {inimigo.vida}')

def curar(jogador, quantidade):
    jogador.vida += quantidade
    print(f'Cura de {quantidade} pontos! Vida atual: {jogador.vida}')

def buff_ataque(carta, quantidade):
    carta.ataque += quantidade
    print(f'{carta.nome} recebeu +{quantidade} de ataque!')

def buff_defesa(carta, quantidade):
    carta.defesa += quantidade
    print(f'{carta.nome} recebeu +{quantidade} de defesa!')

def debuff_ataque(carta, quantidade):
    carta.ataque = max(0, carta.ataque - quantidade)
    print(f'{carta.nome} perdeu {quantidade} de ataque.')

def debuff_defesa(carta, quantidade):
    carta.defesa = max(0, carta.defesa - quantidade)
    print(f'{carta.nome} perdeu {quantidade} de defesa.')

def comprar_cartas(jogador, quantidade):
    for _ in range(quantidade):
        if jogador.deck:
            carta = jogador.deck.pop(0)
            jogador.mao.append(carta)
            print(f'Carta {carta.nome} comprada.')

def dano_em_area(inimigos, quantidade):
    for inimigo in inimigos:
        inimigo.defesa -= quantidade
        print(f'{inimigo.nome} recebeu {quantidade} de dano em área.')

# Outras funções utilitárias podem ser adicionadas conforme necessidade.
