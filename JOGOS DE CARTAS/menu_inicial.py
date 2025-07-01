# menu_inicial.py
from campanha_v1 import jogar_campanha
from salvar_progresso import salvar_jogo
from carregar_progresso import carregar_jogo
from personagens_data import personagens
from card_repository import get_carta_by_id
import random


def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Iniciar Campanha")
        print("2 - Continuar Campanha")
        print("3 - Ver Inventário de Cartas (em breve)")
        print("4 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            print("\nEscolha seu herói:")
            for idx, p in enumerate(personagens):
                print(f"{idx + 1} - {p['nome']}")
            indice = int(input("\nDigite o número do personagem desejado: ")) - 1
            heroi = personagens[indice]["nome"]
            deck = [get_carta_by_id(f"Carta_{random.randint(1, 80)}") for _ in range(10)]
            jogar_campanha(heroi, deck)

        elif escolha == "2":
            progresso = carregar_jogo()
            if progresso:
                heroi, deck, fase = progresso
                jogar_campanha(heroi, deck, fase)

        elif escolha == "3":
            print("📦 Inventário ainda em desenvolvimento...")

        elif escolha == "4":
            print("👋 Saindo do jogo. Até a próxima!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
