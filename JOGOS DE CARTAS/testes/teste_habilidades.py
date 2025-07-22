# teste_habilidades.py

from habilidades import habilidades_cartas_unitarias as habilidades
from jogador_teste import JogadorTeste, InimigoTeste

jogador = JogadorTeste()
inimigo = InimigoTeste()
campo = []  # Lista vazia ou populada conforme necessidade do teste

# Liste aqui as cartas que deseja testar
cartas_para_testar = [
    'Carta_1', 'Carta_5', 'Carta_10', 'Carta_15', 'Carta_20',
    'Carta_30', 'Carta_40', 'Carta_50', 'Carta_60', 'Carta_70', 'Carta_80'
]

for carta_id in cartas_para_testar:
    print(f"\nTestando habilidade da {carta_id}:")
    habilidades.executar(carta_id, jogador, inimigo, campo)
    print(f"Vida do jogador: {jogador.vida}")
    print(f"Vida do inimigo: {inimigo.vida}")
    print(f"Campo jogador: {jogador.campo}")
    print(f"Campo inimigo: {inimigo.campo}")

print("\n--- Testes finalizados ---")
