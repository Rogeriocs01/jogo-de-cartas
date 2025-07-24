import random
from gerenciamento.inventario_jogador import adicionar_carta


drops_por_personagem = {
    "Thorin, o Bravo": [
        {"id": "Carta_01", "raridade": "Comum"},
        {"id": "Carta_02", "raridade": "Comum"},
        {"id": "Carta_03", "raridade": "Incomum"},
        {"id": "Carta_04", "raridade": "Rara"},
    ],
    "Elora, a Arqueira Élfica": [
        {"id": "Carta_06", "raridade": "Comum"},
        {"id": "Carta_07", "raridade": "Incomum"},
        {"id": "Carta_08", "raridade": "Rara"},
        {"id": "Carta_09", "raridade": "Lendária"},
    ],
    # Adicione os outros personagens aqui depois...
}

probabilidades = {
    "Comum": 0.6,
    "Incomum": 0.3,
    "Rara": 0.08,
    "Lendária": 0.02,
}

def tentar_drop(nome_inimigo):
    if nome_inimigo not in drops_por_personagem:
        print("Nenhuma carta disponível para drop deste inimigo.")
        return

    cartas_possiveis = drops_por_personagem[nome_inimigo]

    for carta in cartas_possiveis:
        chance = probabilidades.get(carta["raridade"], 0)
        if random.random() <= chance:
            print(f"\n🎉 Você ganhou uma nova carta: {carta['id']} ({carta['raridade']})!")
            adicionar_carta(carta["id"])
            return  # Só uma carta dropa por vez
    print("\nNenhuma carta dropada desta vez...")