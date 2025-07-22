# habilidades/habilidades_cartas_efeito.py

from habilidades import habilidades_utils as utils

def executar_efeito(carta_id, jogador, inimigo, campo):
    efeitos = {
        'Carta_81': efeito_dano_direto,
        'Carta_82': efeito_dano_direto,
        'Carta_83': efeito_dano_direto,
        'Carta_84': efeito_dano_direto,
        'Carta_85': efeito_cura,
        'Carta_86': efeito_cura,
        'Carta_87': efeito_cura,
        'Carta_88': efeito_cura,
        'Carta_89': efeito_comprar_cartas,
        'Carta_90': efeito_comprar_cartas,
        'Carta_91': efeito_comprar_cartas,
        'Carta_92': efeito_comprar_cartas,
        'Carta_93': efeito_buff_ataque,
        'Carta_94': efeito_buff_ataque,
        'Carta_95': efeito_buff_ataque,
        'Carta_96': efeito_buff_ataque,
        'Carta_97': efeito_debuff_inimigo,
        'Carta_98': efeito_debuff_inimigo,
        'Carta_99': efeito_debuff_inimigo,
        'Carta_100': efeito_debuff_inimigo,
    }

    efeito = efeitos.get(carta_id)
    if efeito:
        efeito(jogador, inimigo, campo)
    else:
        print(f"❌ Efeito da {carta_id} não implementado.")

def efeito_dano_direto(jogador, inimigo, campo):
    utils.dano_direto(inimigo, 3)

def efeito_cura(jogador, inimigo, campo):
    utils.curar(jogador, 3)

def efeito_comprar_cartas(jogador, inimigo, campo):
    for _ in range(2):
        jogador.comprar_carta()

def efeito_buff_ataque(jogador, inimigo, campo):
    for carta in jogador.campo:
        if carta:
            utils.buff_ataque(carta, 1)

def efeito_debuff_inimigo(jogador, inimigo, campo):
    for carta in inimigo.campo:
        if carta:
            utils.debuff_ataque(carta, 1)
