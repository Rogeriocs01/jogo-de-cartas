# menu_inicial.py
import random
from campanha.controlador import jogar_campanha
from recompensas_cartas import carregar_inventario
from progresso_heroi import carregar_progresso
from personagens_data import personagens
from card_repository import get_carta_by_id

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Iniciar Campanha")
        print("2 - Ver Inventário de Cartas")
        print("3 - Ver Progresso do Herói")
        print("4 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            for i, p in enumerate(personagens, start=1):
                print(f"{i} - {p['nome']}")
            opc = input("\nDigite o número do personagem desejado: ")
            if not opc.isdigit() or not (1 <= int(opc) <= len(personagens)):
                print("Opção inválida!")
                continue

            heroi = personagens[int(opc) - 1]
            print(f"\n✅ Você escolheu: {heroi['nome']}!")

            progresso = carregar_progresso()
            inventario = carregar_inventario()
            nome = heroi["nome"]
            nivel = progresso.get(nome, {}).get("nivel", 1)
            xp = progresso.get(nome, {}).get("xp", 0)
            cartas = inventario.get(nome, [])

            print(f"\n📊 Progresso de {nome}:")
            print(f"🔹 Nível: {nivel}")
            print(f"🔸 XP: {xp}")
            print(f"📦 Cartas desbloqueadas: {len(cartas)}")

            deck = [get_carta_by_id(f"Carta_{random.randint(1, 80)}") for _ in range(10)]
            jogar_campanha(heroi, deck)

        elif escolha == "2":
            inventario = carregar_inventario()
            for heroi, cartas in inventario.items():
                print(f"\n🧙‍♂️ {heroi}: {len(cartas)} cartas desbloqueadas")
                for c in cartas:
                    print(f" - {c}")

        elif escolha == "3":
            progresso = carregar_progresso()
            for heroi, dados in progresso.items():
                print(f"\n🧝‍♀️ {heroi} — Nível {dados['nivel']} | XP: {dados['xp']}/100")

        elif escolha == "4":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
