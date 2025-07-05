# batalha/motor.py
from batalha.turno_jogador import turno_jogador
from batalha.turno_inimigo import turno_inimigo

def batalha(jogador, bot):
    while jogador.vida > 0 and bot.vida > 0:
        turno_jogador(jogador, bot)
        if bot.vida <= 0:
            print(f"🎉 {jogador.nome} venceu a batalha!")
            break
        turno_inimigo(bot, jogador)
        if jogador.vida <= 0:
            print(f"💀 {bot.nome} venceu a batalha!")
            break
