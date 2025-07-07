# dados/status_heroi.py

from dados.save import carregar_progresso
from personagens_data import personagens  # ✅ Corrigido aqui

def exibir_status_heroi(nome):
    progresso = carregar_progresso()
    
    if nome not in progresso:
        print(f"Herói '{nome}' não encontrado no progresso salvo.")
        return

    dados_heroi = progresso[nome]

    nivel = dados_heroi.get("nivel", 1)
    xp = dados_heroi.get("xp", 0)
    cartas = dados_heroi.get("cartas", [])

    # XP necessário para o próximo nível
    xp_proximo_nivel = 100 + (nivel - 1) * 50

    # Busca info do personagem para mostrar terreno e habilidade
    personagem_info = next((p for p in personagens if p["nome"] == nome), None)

    print("\n=== STATUS DO HERÓI ===")
    print(f"Nome: {nome}")
    print(f"Nível: {nivel}")
    print(f"XP: {xp} / {xp_proximo_nivel}")
    print(f"Cartas desbloqueadas: {len(cartas)}")

    if personagem_info:
        print(f"Terreno Favorito: {personagem_info['terreno']}")
        print(f"Habilidade Especial: {personagem_info['habilidade_especial']} (Custo: {personagem_info['custo_habilidade']})")
    print("========================\n")
