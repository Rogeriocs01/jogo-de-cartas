from campanha.fases import escolher_fase
from jogador_global import carregar_jogador

def exibir_progresso_fases():
    jogador = carregar_jogador()
    fase_atual = jogador.get("fase", 1)

    print(f"\n🗺️ Progresso da Campanha Global:\n")
    for i in range(1, 61):
        fase_info = escolher_fase(i)
        nome = fase_info["nome"]
        dificuldade = fase_info["dificuldade"]

        if i < fase_atual:
            status = "✅"
        elif i == fase_atual:
            status = "⏳"
        else:
            status = "🔒"

        print(f"Fase {i:02d} - {nome:<15} | {dificuldade:<8} | {status}")
