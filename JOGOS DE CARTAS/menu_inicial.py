# menu_inicial.py
import random
from campanha.controlador import jogar_campanha
from inventario_jogador import carregar_inventario
from progresso_heroi import carregar_progresso
from personagens_data import personagens
from card_repository import get_carta_by_id
from dados.painel_progresso import exibir_painel_progresso
from loja import abrir_loja

heroi = None  # ✅ Variável global para reuso na loja

def menu_principal():
    global heroi  # ✅ Para manter o herói selecionado entre as opções

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Iniciar Campanha")
        print("2 - Ver Inventário de Cartas")
        print("3 - Ver Painel de Progresso dos Heróis")
        print("4 - Acessar Loja de Cartas")  # 🆕
        print("5 - Sair")

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
            inventario = carregar_inventario() or {}

            nivel = progresso.get(nome, {}).get("nivel", 1)
            xp = progresso.get(nome, {}).get("xp", 0)
            cartas = inventario.get(nome, {})

            print(f"\n📊 Progresso de {nome}:")
            print(f"🔹 Nível: {nivel}")
            print(f"🔸 XP: {xp}")
            print(f"📦 Cartas desbloqueadas: {len(cartas)}")

            # Deck aleatório temporário
            deck = [get_carta_by_id(f"Carta_{random.randint(1, 80)}") for _ in range(10)]
            jogar_campanha(heroi, deck)

        elif escolha == "2":
            inventario = carregar_inventario()
            if not inventario:
                print("\n📭 Inventário vazio.")
            for heroi_nome, cartas in inventario.items():
                print(f"\n🧙‍♂️ {heroi_nome}: {len(cartas)} cartas desbloqueadas")
                for carta_id, qtd in cartas.items():
                    print(f" - {carta_id} x{qtd}")

        elif escolha == "3":
            exibir_painel_progresso()

        elif escolha == "4":
            if heroi:
                abrir_loja(heroi["nome"])
            else:
                print("❌ Selecione um herói primeiro para acessar a loja.")

        elif escolha == "5":
            print("\n👋 Saindo do jogo...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
