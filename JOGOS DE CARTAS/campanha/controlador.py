# campanha/controlador.py
from batalha_v8 import Jogador, batalha
from card_repository import get_carta_by_id
from campanha.progresso import ganhar_xp
from campanha.fases import escolher_fase
from campanha.inimigos import get_personagem_info
from recompensas_cartas import recompensar_vitoria


def jogar_campanha(heroi_dict, deck):
    nome_personagem = heroi_dict["nome"]
    info_jogador = get_personagem_info(nome_personagem)

    fase_atual = 1
    while fase_atual <= 60:
        fase_info = escolher_fase(fase_atual)
        bot_info = get_personagem_info(fase_info["nome"])

        print(f"\n=== PRÓXIMA FASE: {fase_atual}/60 — {bot_info['nome']} ({fase_info['dificuldade']}) | Terreno: {bot_info['terreno']} ===")
        entrada = input("Pressione ENTER para iniciar esta fase ou 'm' para voltar ao menu: ")
        if entrada.lower() == 'm':
            break

        player = Jogador(
            nome=info_jogador["nome"],
            terreno_favorito=info_jogador["terreno"],
            habilidade_especial=info_jogador.get("habilidade_especial"),
            custo_habilidade=info_jogador.get("custo_habilidade", 2),
        )

        bot = Jogador(
            nome=bot_info["nome"],
            terreno_favorito=bot_info["terreno"],
            is_bot=True
        )

        player.deck = [get_carta_by_id(card) for card in deck]
        bot.deck = [get_carta_by_id(f"Carta_{i}") for i in range(1, 11)]

        batalha(player, bot)

        if player.vida > 0:
            print(f"\n🏆 Você venceu a fase {fase_atual}!")
            ganhar_xp(player.nome, 100)
            recompensar_vitoria(player.nome)
            fase_atual += 1
        else:
            print("\n💀 Você foi derrotado. Retorne ao menu para tentar novamente.")
            break
