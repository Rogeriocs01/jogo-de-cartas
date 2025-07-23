# batalha/turno_inimigo.py

from habilidades import habilidades_cartas_unitarias as habilidades
from utils import pausar


def turno_inimigo(inimigo, jogador):
    print(f"\n🤖 Turno do inimigo: {inimigo.nome}")

    # Invoca cartas da mão automaticamente, se houver espaço
    for _ in range(5):
        if any(carta is not None for carta in inimigo.mao):
            inimigo.invocar_carta()

    # Usa habilidades das cartas em campo automaticamente
    for idx, carta in enumerate(inimigo.campo):
        if carta and hasattr(carta, "habilidade") and not getattr(carta, "habilidade_usada", False):
            if inimigo.mana >= carta.custo_mana:
                inimigo.mana -= carta.custo_mana
                habilidades.executar(carta.id, inimigo, jogador, inimigo.campo)
                carta.habilidade_usada = True
                print(f"🌀 Inimigo usou a habilidade de {carta.nome}!")
    
    # Ataca com as cartas disponíveis
    inimigo.atacar(jogador)

    pausar()
