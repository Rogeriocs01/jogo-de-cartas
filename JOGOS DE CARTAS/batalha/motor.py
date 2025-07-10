# batalha/motor.py

from batalha.turno_jogador import turno_jogador
from batalha.turno_inimigo import turno_inimigo
from dados.status_heroi import exibir_status_heroi

def batalha(jogador, bot):
    print(f"\n⚔️ Iniciando batalha: {jogador.nome} (HP: {jogador.vida}) vs {bot.nome} (HP: {bot.vida})")

    # 🔹 Ambos compram até 5 cartas iniciais (se tiverem no deck)
    for _ in range(5):
        if jogador.deck:
            jogador.comprar_carta()
        if bot.deck:
            bot.comprar_carta()

    # 🔁 Loop principal da batalha
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

    # 🔚 Limpa a mão dos dois jogadores após o fim da batalha
    jogador.limpar_mao()
    bot.limpar_mao()
