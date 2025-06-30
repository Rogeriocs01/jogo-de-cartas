import random

recompensas_por_personagem = {
    "Thorin, o Bravo": [
        {"nome": "Martelo de Thorin", "raridade": "Comum", "chance": 60},
        {"nome": "Grito de Guerra", "raridade": "Rara", "chance": 25},
        {"nome": "Escudo dos Anões", "raridade": "Épica", "chance": 10},
        {"nome": "Fúria de Durin", "raridade": "Lendária", "chance": 5},
    ],
    # Adicione os outros personagens aqui depois
}

def tentar_drop(personagem_nome):
    chance_geral = 40  # % de chance de ter um drop
    resultado = random.randint(1, 100)

    if resultado <= chance_geral:
        print("\n🎉 Você ganhou uma recompensa!")

        pool = recompensas_por_personagem.get(personagem_nome, [])
        chances = [c["chance"] for c in pool]
        cartas = [c["nome"] for c in pool]

        carta_ganha = random.choices(cartas, weights=chances, k=1)[0]
        print(f"🏅 Nova Carta: {carta_ganha} adicionada ao seu deck!")
    else:
        print("\nNenhuma carta dropada desta vez... continue tentando nas próximas fases!")
