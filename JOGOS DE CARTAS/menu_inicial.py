import random
from campanha.controlador import jogar_campanha
from inventario_jogador import mostrar_inventario
from progresso_heroi import carregar_progresso
from personagens_data import personagens
from dados.painel_progresso import exibir_painel_progresso
from loja import abrir_loja
from campanha.progresso_fases import exibir_progresso_fases
from jogador_global import exibir_status_jogador
from deck_manager import montar_deck_manual, criar_deck_automatico

heroi = None  # ✅ Mantém o herói selecionado durante o uso do menu

def menu_principal():
    global heroi

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Selecionar Herói e Iniciar Campanha")
        print("2 - Ver Inventário de Cartas (Global)")
        print("3 - Ver Painel de Progresso dos Heróis")
        print("4 - Ver Mapa da Campanha")
        print("5 - Acessar Loja de Cartas")
        print("6 - Ver Status do Jogador")
        print("7 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            for i, p in enumerate(personagens, start=1):
                print(f"{i} - {p['nome']}")
            opc = input("\nDigite o número do personagem desejado: ")
            if not opc.isdigit() or not (1 <= int(opc) <= len(personagens)):
                print("❌ Opção inválida!")
                continue

            heroi = personagens[int(opc) - 1]
            nome = heroi["nome"]
            print(f"\n✅ Você escolheu: {nome}!")

            progresso = carregar_progresso()
            nivel = progresso.get(nome, {}).get("nivel", 1)
            xp = progresso.get(nome, {}).get("xp", 0)

            print(f"\n📊 Progresso de {nome}:")
            print(f"🔹 Nível: {nivel}")
            print(f"🔸 XP: {xp}")

            # 🔽 NOVO: Escolha entre montar deck ou usar automático
            print("\n💼 Deseja montar seu deck ou usar o automático?")
            print("1 - Montar manualmente com cartas do inventário")
            print("2 - Usar deck automático do personagem")
            opcao_deck = input("Escolha (1 ou 2): ")

            if opcao_deck == "1":
                deck = montar_deck_manual(nome)
            else:
                deck = criar_deck_automatico(nome)

            print(f"🧪 Deck carregado com {len(deck)} cartas.")
            jogar_campanha(heroi, deck)

        elif escolha == "2":
            mostrar_inventario()

        elif escolha == "3":
            exibir_painel_progresso()

        elif escolha == "4":
            if heroi:
                exibir_progresso_fases(heroi["nome"])
            else:
                print("❌ Selecione um herói primeiro para visualizar o mapa.")

        elif escolha == "5":
            abrir_loja()

        elif escolha == "6":
            exibir_status_jogador()

        elif escolha == "7":
            print("\n👋 Saindo do jogo...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
