# batalha/habilidade_heroi.py
from habilidades.habilidades_heroi import heroi_habilidades

def usar_habilidade_heroi(jogador, inimigo):
    if jogador.habilidade_heroi_usada:
        return
    if jogador.habilidade_especial not in heroi_habilidades:
        return
    if jogador.mana < jogador.custo_habilidade:
        return

    jogador.mana -= jogador.custo_habilidade
    habilidade = heroi_habilidades[jogador.habilidade_especial]

    if jogador.habilidade_especial in ["curar", "comprar_cartas", "reduzir_custo_mana"]:
        habilidade(jogador)
    else:
        habilidade(jogador, inimigo)

    jogador.habilidade_heroi_usada = True
