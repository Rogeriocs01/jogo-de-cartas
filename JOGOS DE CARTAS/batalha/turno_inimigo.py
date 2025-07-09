from executar_habilidade import executar_habilidade
from batalha.habilidade_heroi import usar_habilidade_heroi
from interface_terminal import exibir_campo

def turno_inimigo(bot, jogador):
    print(f"\n🤖 Turno de {bot.nome}")
    bot.mana = 3
    bot.resetar_habilidades()
    bot.comprar_carta()

    exibir_campo(bot, jogador)

    # 🔹 Ordena mão por poder (ATK + DEF)
    bot.mao.sort(key=lambda c: c.ataque + c.defesa, reverse=True)

    # 🔹 Tenta invocar cartas se tiver mana suficiente
    for carta in bot.mao[:]:
        if bot.mana < carta.custo_mana:
            continue
        for slot in range(5):
            if not bot.campo[slot]:
                sucesso = bot.invocar_carta(bot.mao.index(carta), slot)
                if sucesso:
                    break  # Sai do loop de slots se invocou

    # 🔹 Usa habilidades das cartas em campo (se possível)
    for carta in bot.campo:
        if carta and not carta.habilidade_usada and bot.mana >= carta.custo_mana:
            executar_habilidade(carta.id, carta, bot, jogador)
            carta.habilidade_usada = True
            bot.mana -= carta.custo_mana

    # 🔹 Usa habilidade especial do herói
    usar_habilidade_heroi(bot, jogador)

    # 🔹 Ataca
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

    # 🔹 Exibe o estado final do campo
    exibir_campo(bot, jogador)
