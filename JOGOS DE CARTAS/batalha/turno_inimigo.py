# batalha/turno_inimigo.py
from executar_habilidade import executar_habilidade
from batalha.habilidade_heroi import usar_habilidade_heroi
from interface_terminal import exibir_campo

def turno_inimigo(bot, jogador):
    print(f"\n🤖 Turno de {bot.nome}")
    bot.mana = 3
    bot.resetar_habilidades()
    bot.comprar_carta()
    exibir_campo(bot, jogador)

    bot.mao.sort(key=lambda c: c.ataque + c.defesa, reverse=True)
    for carta in bot.mao[:]:
        for idx in range(5):
            if not bot.campo[idx]:
                bot.campo[idx] = carta
                bot.mao.remove(carta)
                print(f"🤖 {bot.nome} invocou {carta.nome}!")
                break

    for carta in bot.campo:
        if carta and not carta.habilidade_usada and bot.mana >= carta.custo_mana:
            executar_habilidade(carta.id, carta, bot, jogador)
            carta.habilidade_usada = True
            bot.mana -= carta.custo_mana

    usar_habilidade_heroi(bot, jogador)

    for idx, atacante in enumerate(bot.campo):
        if atacante:
            alvos = [(i, c) for i, c in enumerate(jogador.campo) if c]
            if alvos:
                alvo_idx, alvo = min(alvos, key=lambda x: x[1].defesa)
                alvo.defesa -= atacante.ataque
                print(f"🤖 {atacante.nome} atacou {alvo.nome}! Nova DEF: {alvo.defesa}")
                if alvo.defesa <= 0:
                    print(f"💥 {alvo.nome} foi destruída!")
                    jogador.campo[alvo_idx] = None
            else:
                jogador.vida -= atacante.ataque
                print(f"🤖 Ataque direto! {jogador.nome} perdeu {atacante.ataque} de vida!")
