# batalha/motor.py

from batalha.turno_jogador import turno_jogador
from batalha.turno_inimigo import turno_inimigo
from utils import pausar, limpar_tela


def batalha(jogador, inimigo):
    turno = 1

    while jogador.vida > 0 and inimigo.vida > 0:
        limpar_tela()
        print(f"\n⚔️ Rodada {turno} ⚔️")
        print(f"{jogador.nome}: {jogador.vida} de vida | Mana: {jogador.mana}")
        print(f"{inimigo.nome}: {inimigo.vida} de vida | Mana: {inimigo.mana}")

        jogador.mana = turno  # Ganha 1 de mana por turno
        inimigo.mana = turno

        jogador.comprar_carta()
        inimigo.comprar_carta()

        turno_jogador(jogador, inimigo)
        if inimigo.vida <= 0:
            break

        turno_inimigo(inimigo, jogador)
        if jogador.vida <= 0:
            break

        turno += 1

    print("\n🏁 Fim da batalha!")
    if jogador.vida <= 0 and inimigo.vida <= 0:
        print("🪦 Empate! Ambos os jogadores foram derrotados.")
    elif jogador.vida <= 0:
        print("💀 Você foi derrotado...")
    else:
        print("🎉 Vitória! O inimigo foi vencido.")

    pausar()
