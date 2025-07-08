# dados/painel_progresso.py

from progresso_heroi import carregar_progresso
from inventario_jogador import carregar_inventario

def exibir_painel_progresso():
    progresso = carregar_progresso()
    inventario = carregar_inventario()

    if not progresso:
        print("\n📉 Nenhum progresso encontrado.")
        return

    print("\n=== PAINEL DE PROGRESSO DOS HERÓIS ===")

    for nome_heroi, dados in progresso.items():
        nivel = dados.get("nivel", 1)
        xp = dados.get("xp", 0)
        moedas = dados.get("moedas", 0)
        cartas = inventario.get(nome_heroi, {})
        qtd_cartas = len(cartas)

        xp_prox_nivel = 100 + (nivel - 1) * 50

        print(f"\n🧝‍♂️ {nome_heroi}")
        print(f"   🔹 Nível: {nivel}")
        print(f"   🔸 XP: {xp}/{xp_prox_nivel}")
        print(f"   💰 Moedas: {moedas}")
        print(f"   📦 Cartas desbloqueadas: {qtd_cartas}")
    print("========================================\n")
