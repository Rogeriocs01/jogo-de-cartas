# batalha/motor.py
from batalha.turno_jogador import turno_jogador
from batalha.turno_inimigo import turno_inimigo
from dados.status_heroi import exibir_status_heroi


def batalha(jogador, bot):
    # 🔹 Ambos compram 5 cartas iniciais
    for _ in range(5):
        jogador.comprar_carta()
        bot.comprar_carta()

    while jogador.vida > 0 and bot.vida > 0:
        turno_jogador(jogador, bot)
        if bot.vida <= 0:
            print(f"🎉 {jogador.nome} venceu a batalha!")
            exibir_status_heroi(jogador.nome)
            break

        turno_inimigo(bot, jogador)
        if jogador.vida <= 0:
            print(f"💀 {bot.nome} venceu a batalha!")
            break
