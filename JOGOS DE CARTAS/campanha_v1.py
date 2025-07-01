# campanha_v1.py

from mapa import escolher_fase
from personagens_data import personagens
from batalha_v8 import Jogador, batalha
from card_repository import get_carta_by_id
import random


def get_personagem_info(nome_personagem):
    for p in personagens:
        if p["nome"] in nome_personagem or nome_personagem in p["nome"]:
            return p
    raise ValueError(f"Personagem não encontrado: {nome_personagem}")


def jogar_campanha(nome_personagem, deck):
    progresso = 0
    total_fases = len(personagens) * 3

    while progresso < total_fases:
        fase_info = escolher_fase(progresso)
        if fase_info is None:
            break

        nome_inimigo = fase_info["nome"]
        dificuldade = fase_info["dificuldade"]
        terreno = fase_info["terreno"]
        buff = fase_info.get("buff", {"tipo": "atk", "valor": 0})

        print(f"=== FASE {progresso + 1}/{total_fases}: {nome_inimigo} — {dificuldade} ===")

        info_jogador = get_personagem_info(nome_personagem)
        player = Jogador(
            nome=nome_personagem,
            is_bot=False,
            habilidade_especial=info_jogador.get("habilidade_especial"),
            custo_habilidade=info_jogador.get("custo_habilidade", 0),
            terreno_favorito=info_jogador.get("terreno")
        )

        bot_info = get_personagem_info(nome_inimigo)
        bot = Jogador(
            nome=nome_inimigo,
            is_bot=True,
            habilidade_especial=bot_info.get("habilidade_especial"),
            custo_habilidade=bot_info.get("custo_habilidade", 0),
            terreno_favorito=bot_info.get("terreno")
        )

        # Aplica buff de fase no inimigo
        bot.vida += int(bot.vida * (buff["valor"] / 100))

        # Preenche decks
        for _ in range(10):
            player.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))
            bot.deck.append(get_carta_by_id(f"Carta_{random.randint(1, 80)}"))

        batalha(player, bot)

        if player.vida <= 0:
            print("\n⚠️ Derrota! Você pode tentar novamente.")
            break
        else:
            progresso += 1

    if progresso >= total_fases:
        print("\n🎉 Parabéns! Você concluiu toda a campanha!")
