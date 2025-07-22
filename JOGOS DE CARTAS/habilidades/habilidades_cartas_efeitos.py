### habilidades/habilidades\_cartas\_efeitos.py


# habilidades_cartas_efeitos.py

from habilidades import habilidades_utils as utils


def executar(carta_id, jogador, inimigo, campo):
    funcoes = {
        'Carta_81': carta_81,
        'Carta_82': carta_82,
        'Carta_83': carta_83,
        'Carta_84': carta_84,
        'Carta_85': carta_85,
        'Carta_86': carta_86,
        'Carta_87': carta_87,
        'Carta_88': carta_88,
        'Carta_89': carta_89,
        'Carta_90': carta_90,
        'Carta_91': carta_91,
        'Carta_92': carta_92,
        'Carta_93': carta_93,
        'Carta_94': carta_94,
        'Carta_95': carta_95,
        'Carta_96': carta_96,
        'Carta_97': carta_97,
        'Carta_98': carta_98,
        'Carta_99': carta_99,
        'Carta_100': carta_100,
    }

    habilidade = funcoes.get(carta_id)
    if habilidade:
        habilidade(jogador, inimigo, campo)
    else:
        print(f'Habilidade da {carta_id} não implementada.')


def carta_81(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 3)

def carta_82(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 2)

def carta_83(jogador, inimigo, campo):
    utils.dano_em_area(inimigo.campo, 2)

def carta_84(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 2)

def carta_85(jogador, inimigo, campo):
    utils.curar(jogador, 2)

def carta_86(jogador, inimigo, campo):
    utils.curar(jogador, 3)

def carta_87(jogador, inimigo, campo):
    utils.curar(jogador, 2)

def carta_88(jogador, inimigo, campo):
    utils.curar(jogador, 4)

def carta_89(jogador, inimigo, campo):
    utils.comprar_cartas(jogador, 1)

def carta_90(jogador, inimigo, campo):
    utils.comprar_cartas(jogador, 2)

def carta_91(jogador, inimigo, campo):
    utils.comprar_cartas(jogador, 1)

def carta_92(jogador, inimigo, campo):
    utils.comprar_cartas(jogador, 3)

def carta_93(jogador, inimigo, campo):
    for carta in jogador.campo:
        utils.buff_ataque(carta, 1)

def carta_94(jogador, inimigo, campo):
    for carta in jogador.campo:
        utils.buff_ataque(carta, 2)

def carta_95(jogador, inimigo, campo):
    for carta in jogador.campo:
        utils.buff_ataque(carta, 1)

def carta_96(jogador, inimigo, campo):
    for carta in jogador.campo:
        utils.buff_ataque(carta, 3)

def carta_97(jogador, inimigo, campo):
    for carta in inimigo.campo:
        utils.debuff_ataque(carta, 1)

def carta_98(jogador, inimigo, campo):
    for carta in inimigo.campo:
        utils.debuff_ataque(carta, 2)

def carta_99(jogador, inimigo, campo):
    for carta in inimigo.campo:
        utils.debuff_ataque(carta, 1)

def carta_100(jogador, inimigo, campo):
    for carta in inimigo.campo:
        utils.debuff_ataque(carta, 1)
        utils.debuff_defesa(carta, 1)
