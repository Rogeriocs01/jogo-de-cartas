#menu_inicial.py
import random
from campanha.controlador import jogar_campanha
from inventario_jogador import mostrar_inventario
from progresso_heroi import carregar_progresso
from personagens_data import personagens
from dados.painel_progresso import exibir_painel_progresso
from loja import abrir_loja
from campanha.progresso_fases import exibir_progresso_fases
from jogador_global import exibir_status_jogador
from deck_manager import criar_deck_automatico, montar_deck_manual, salvar_deck_personalizado, carregar_deck_personalizado

heroi = None  # ✅ Mantém o herói selecionado durante o uso do menu

def menu_principal():
    global heroi

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Selecionar Herói")
        print("2 - Editar Deck Manualmente")
        print("3 - Iniciar Campanha com Deck do Herói")
        print("4 - Ver Inventário de Cartas (Global)")
        print("5 - Ver Painel de Progresso dos Heróis")
        print("6 - Ver Mapa da Campanha")
        print("7 - Acessar Loja de Cartas")
        print("8 - Ver Status do Jogador")
        print("9 - Sair")

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

        elif escolha == "2":
            if heroi:
                nome = heroi["nome"]
                print(f"\n✍️ Editando deck de: {nome}")
                novo_deck = montar_deck_manual(nome)
                salvar_deck_personalizado(nome, novo_deck)
                print("💾 Deck salvo com sucesso!")
            else:
                print("❌ Selecione um herói primeiro na opção 1.")

        elif escolha == "3":
            if not heroi:
                print("❌ Selecione um herói primeiro na opção 1.")
                continue

            nome = heroi["nome"]
            print("\n🔧 Como deseja usar seu deck?")
            print("1 - Usar deck automático baseado no personagem")
            print("2 - Usar deck salvo manualmente")
            escolha_deck = input("Escolha uma opção: ")

            if escolha_deck == "2":
                deck = carregar_deck_personalizado(nome)
            else:
                deck = criar_deck_automatico(nome)

            print(f"🧪 Deck final: {[c.nome for c in deck]}")
            jogar_campanha(heroi, deck)

        elif escolha == "4":
            mostrar_inventario()

        elif escolha == "5":
            exibir_painel_progresso()

        elif escolha == "6":
            if heroi:
                exibir_progresso_fases(heroi["nome"])
            else:
                print("❌ Selecione um herói primeiro para visualizar o mapa.")

        elif escolha == "7":
            abrir_loja()

        elif escolha == "8":
            exibir_status_jogador()

        elif escolha == "9":
            print("\n👋 Saindo do jogo...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
