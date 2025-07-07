# campanha/recompensas_por_fase.py

from inventario_jogador import adicionar_carta

recompensas_fixas = {
    5: "Carta_91",
    10: "Carta_92",
    15: "Carta_93",
    20: "Carta_94",
    25: "Carta_95",
    30: "Carta_96",
    35: "Carta_97",
    40: "Carta_98",
    45: "Carta_99",
    50: "Carta_100",
}

def verificar_recompensa(fase, nome_heroi):
    if fase in recompensas_fixas:
        carta_id = recompensas_fixas[fase]
        print(f"\n🎁 Recompensa desbloqueada por vencer a Fase {fase}!")
        print(f"🃏 Nova carta adicionada ao seu inventário: {carta_id}")
        adicionar_carta(carta_id, nome_heroi)
