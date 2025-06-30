from selecao_personagem import escolher_personagem
from deck_personalizado import criar_deck_personalizado
from selecao_personagem import escolher_personagem
from inventario_jogador import mostrar_inventario  # Se quiser manter a opção de ver o inventário

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Iniciar Campanha")
        print("2 - Ver Inventário de Cartas")
        print("3 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            heroi = escolher_personagem()
            deck = criar_deck_personalizado(heroi)

            if not deck:
                print("⚠️ Não foi possível criar o deck do herói. Verifique a configuração.")
                continue

            from campanha_v1 import jogar_campanha
            jogar_campanha(heroi, deck)

        elif escolha == "2":
            mostrar_inventario()

        elif escolha == "3":
            print("\n👋 Saindo do jogo... Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()
