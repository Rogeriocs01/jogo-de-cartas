# loja.py

import random
from progresso_heroi import remover_moedas, adicionar_moedas
from inventario_jogador import adicionar_carta

cartas_disponiveis = [
    {"id": "Carta_05", "preco": 20},
    {"id": "Carta_12", "preco": 30},
    {"id": "Carta_23", "preco": 50},
    {"id": "Carta_47", "preco": 70},
    {"id": "Carta_80", "preco": 100},
]

def abrir_loja(nome_heroi):
    while True:
        print(f"\n=== LOJA DE CARTAS — {nome_heroi} ===")
        print("1 - Comprar carta específica")
        print("2 - Comprar baú de cartas aleatórias (3 cartas por 60 moedas)")
        print("3 - Comprar moedas com dinheiro real [🔒 Em breve]")
        print("0 - Voltar ao menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n🛒 Cartas disponíveis:")
            for i, carta in enumerate(cartas_disponiveis, start=1):
                print(f"{i} - {carta['id']} ({carta['preco']} moedas)")
            escolha = input("Digite o número da carta desejada: ")
            if not escolha.isdigit() or not (1 <= int(escolha) <= len(cartas_disponiveis)):
                print("❌ Escolha inválida.")
                continue
            carta = cartas_disponiveis[int(escolha) - 1]
            if remover_moedas(nome_heroi, carta["preco"]):
                adicionar_carta(carta["id"], nome_heroi)
                print(f"✅ Você comprou {carta['id']}!")
            else:
                print("❌ Moedas insuficientes.")

        elif opcao == "2":
            preco_bau = 60
            if remover_moedas(nome_heroi, preco_bau):
                print("🎁 Abrindo baú...")
                for _ in range(3):
                    drop = random.choice(cartas_disponiveis)
                    adicionar_carta(drop["id"], nome_heroi)
                    print(f"🃏 Recebeu: {drop['id']}")
            else:
                print("❌ Moedas insuficientes para o baú.")

        elif opcao == "3":
            print("💰 Integração com compras reais ainda não disponível.")
            print("🔒 Em breve será possível comprar moedas com PIX, cartão ou boleto.")
            # TODO: Integrar API de pagamento aqui futuramente
            # exemplo: integracao_pagamento.comprar_moedas(nome_heroi, quantidade)

        elif opcao == "0":
            break

        else:
            print("❌ Opção inválida.")
