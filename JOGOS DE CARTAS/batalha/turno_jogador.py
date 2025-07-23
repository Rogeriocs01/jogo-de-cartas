# batalha/turno_jogador.py

from habilidades import habilidades_cartas_unitarias as habilidades
from utils import exibir_mao, exibir_campo, pausar, limpar_tela


def turno_jogador(jogador, inimigo):
    while True:
        limpar_tela()
        print(f"🎮 Turno de {jogador.nome}")
        exibir_campo(jogador, inimigo)
        exibir_mao(jogador)

        print("\nAções disponíveis:")
        print("1 - Invocar carta da mão")
        print("2 - Atacar com cartas do campo")
        print("3 - Usar habilidade de carta do campo")
        print("4 - Encerrar turno")

        escolha = input("Escolha uma ação: ")

        if escolha == "1":
            jogador.invocar_carta()
        elif escolha == "2":
            jogador.atacar(inimigo)
        elif escolha == "3":
            usar_habilidade_carta(jogador, inimigo)
        elif escolha == "4":
            break
        else:
            print("❌ Escolha inválida.")
            pausar()


def usar_habilidade_carta(jogador, inimigo):
    print("\n🌀 Cartas com habilidades disponíveis:")
    cartas_com_habilidade = []
    for idx, carta in enumerate(jogador.campo):
        if carta and hasattr(carta, "habilidade") and not getattr(carta, "habilidade_usada", False):
            print(f"{idx + 1} - {carta.nome} (Mana: {carta.custo_mana})")
            cartas_com_habilidade.append((idx, carta))

    if not cartas_com_habilidade:
        print("⚠️ Nenhuma carta com habilidade disponível.")
        pausar()
        return

    try:
        escolha = int(input("Escolha o número da carta para usar a habilidade: ")) - 1
        if 0 <= escolha < len(jogador.campo):
            carta = jogador.campo[escolha]
            if carta is None:
                print("❌ Slot vazio.")
            elif carta.habilidade_usada:
                print("⚠️ Habilidade já usada neste turno.")
            elif jogador.mana < carta.custo_mana:
                print("❌ Mana insuficiente para usar a habilidade.")
            else:
                jogador.mana -= carta.custo_mana
                habilidades.executar(carta.id, jogador, inimigo, jogador.campo)
                carta.habilidade_usada = True
                print(f"✨ Habilidade de {carta.nome} usada com sucesso!")
        else:
            print("❌ Escolha inválida.")
    except ValueError:
        print("❌ Entrada inválida.")
    
    pausar()
