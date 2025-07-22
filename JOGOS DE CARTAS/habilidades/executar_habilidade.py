### habilidades/executar\_habilidade.py


# executar_habilidade.py

from habilidades import habilidades_cartas_unitarias, habilidades_cartas_efeitos


def executar_habilidade(carta, jogador, inimigo, campo):
    try:
        carta_numero = int(carta.id.split('_')[1])
        if 1 <= carta_numero <= 80:
            habilidades_cartas_unitarias.executar(carta.id, jogador, inimigo, campo)
        elif 81 <= carta_numero <= 100:
            habilidades_cartas_efeitos.executar(carta.id, jogador, inimigo, campo)
        else:
            print(f'⚠️ Carta {carta.id} não possui habilidade implementada.')
    except Exception as e:
        print(f'Erro ao executar habilidade da carta {carta.id}: {e}')
