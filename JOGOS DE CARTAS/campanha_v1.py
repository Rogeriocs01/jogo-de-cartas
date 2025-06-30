# campanha_v1.py
from batalha_v8 import Jogador, batalha
from deck_personalizado import criar_deck_personalizado
from selecao_personagem import escolher_personagem
from mapa import escolher_fase
from personagens_data import personagens


def get_personagem_info(nome_personagem: str) -> dict:
    """
    Retorna o dicionário de dados do personagem selecionado.
    """
    for p in personagens:
        if p["nome"] == nome_personagem:
            return p
    raise ValueError(f"Personagem não encontrado: {nome_personagem}")


def jogar_campanha(nome_personagem: str, deck_jogador: list):
    fase_atual = 0
    total_fases = len(personagens) * 3

    # Pega dados do jogador
    info_jogador = get_personagem_info(nome_personagem)

    while fase_atual < total_fases:
        fase_info = escolher_fase(fase_atual)
        if fase_info is None:
            # Voltar ao menu principal
            return

        nome_inimigo = fase_info["nome"]
        buff = fase_info["buff"]
        dificuldade = fase_info["dificuldade"]
        terreno = fase_info["terreno"]

        print(f"\n=== FASE {fase_atual+1}/{total_fases}: {nome_inimigo} — {dificuldade} ===")

        # Cria instâncias de jogadores
        player = Jogador(
            nome=nome_personagem,
            is_bot=False,
            habilidade_especial=info_jogador.get("habilidade"),
            custo_habilidade=info_jogador.get("custo_mana_habilidade", 0),
            terreno_favorito=info_jogador.get("terreno_favorito")
        )
        bot_info = get_personagem_info(nome_inimigo)
        bot = Jogador(
            nome=nome_inimigo,
            is_bot=True,
            habilidade_especial=bot_info.get("habilidade"),
            custo_habilidade=bot_info.get("custo_mana_habilidade", 0),
            terreno_favorito=bot_info.get("terreno_favorito")
        )

        # Aplica buff de vida ao inimigo
        bot.vida += int(bot.vida * (buff / 100))

        # Monta decks
        player.deck = deck_jogador.copy()
        bot.deck = criar_deck_personalizado(nome_inimigo)

        # Executa batalha
        batalha(player, bot)

        # Se vencedor for player
        if bot.vida <= 0:
            print("\n✅ Vitória! Avançando para a próxima fase...")
            fase_atual += 1
        else:
            print("\n❌ Derrota. Tente novamente esta fase.")

    print("\n🏆 PARABÉNS! Você completou toda a campanha!")
