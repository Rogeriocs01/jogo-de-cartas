# campanha_v1.py
from batalha_v8 import Jogador, batalha
from mapa import escolher_fase
from progresso_heroi import ganhar_xp
from recompensas_cartas import recompensar_vitoria
from campanha.recompensas_por_fase import verificar_recompensa  # ✅ NOVO
from personagens_data import personagens
from dados.status_heroi import exibir_status_heroi

def get_personagem_info(nome_personagem):
    for p in personagens:
        if str(p["nome"]) in str(nome_personagem) or str(nome_personagem) in str(p["nome"]):
            return p
    raise ValueError(f"Personagem não encontrado: {nome_personagem}")

def jogar_campanha(heroi_dict, deck):
    nome_personagem = heroi_dict["nome"]
    info_jogador = get_personagem_info(nome_personagem)

    fase_atual = 1
    while fase_atual <= 60:
        fase_info = escolher_fase(fase_atual)
        bot_info = get_personagem_info(fase_info["nome"])

        print(f"\n=== PRÓXIMA FASE: {fase_atual}/60 — {bot_info['nome']} ({fase_info['dificuldade']}) | Terreno: {bot_info['terreno']} ===")

        # ✅ Exibe status do herói antes da fase
        exibir_status_heroi(nome_personagem)

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

        player.deck = [card for card in deck]  # Clonar deck
        bot.deck = [f"Carta_{i}" for i in range(1, 11)]

        batalha(player, bot)

        if player.vida > 0:
            print(f"\n🏆 Você venceu a fase {fase_atual}!")
            ganhar_xp(player.nome, 100)
            recompensar_vitoria(player.nome)
            verificar_recompensa(fase_atual, player.nome)  # ✅ NOVO
            fase_atual += 1
        else:
            print("\n💀 Você foi derrotado. Retorne ao menu para tentar novamente.")
            break
