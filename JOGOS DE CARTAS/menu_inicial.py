# menu_inicial.py
import random
from campanha_v1 import jogar_campanha
from personagens_data import personagens
from recompensas_cartas import carregar_inventario


def mostrar_inventario():
    nome = input("Digite o nome do herói para ver o inventário: ").strip()
    inventario = carregar_inventario()
    cartas = inventario.get(nome, [])
    if not cartas:
        print(f"📭 Nenhuma carta desbloqueada para {nome}.")
    else:
        print(f"📦 Inventário de cartas de {nome}:\n")
        for carta in sorted(cartas):
            print(f" - {carta}")


def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Iniciar Campanha")
        print("2 - Ver Inventário de Cartas")
        print("3 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            print("\n=== ESCOLHA SEU PERSONAGEM ===")
            for idx, p in enumerate(personagens):
                print(f"{idx + 1} - {p['nome']} ({p['terreno']})")

            selecionado = int(input("\nDigite o número do personagem desejado: ")) - 1
            if 0 <= selecionado < len(personagens):
                heroi = personagens[selecionado]
                print(f"\n✅ Você escolheu: {heroi['nome']}!")
                deck = [f"Carta_{random.randint(1, 80)}" for _ in range(10)]
                jogar_campanha(heroi, deck)
            else:
                print("❌ Escolha inválida.")

        elif escolha == "2":
            mostrar_inventario()

        elif escolha == "3":
            print("👋 Saindo do jogo...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
