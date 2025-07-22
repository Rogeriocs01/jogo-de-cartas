import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from habilidades import habilidades_cartas_efeito as efeitos
from testes.jogador_teste import JogadorTeste

jogador = JogadorTeste(nome='Jogador Teste', vida=20, mana=5)
inimigo = JogadorTeste(nome='Inimigo Teste', vida=20, mana=5)
campo = [None, None, None, None, None]

print("\n--- Teste de Cartas de Efeito ---")

cartas_teste = ['Carta_81', 'Carta_85', 'Carta_89', 'Carta_93', 'Carta_97']

for carta_id in cartas_teste:
    print(f"\nTestando efeito da {carta_id}:")
    efeitos.executar_efeito(carta_id, jogador, inimigo, campo)
    print(f"Vida do jogador: {jogador.vida}")
    print(f"Vida do inimigo: {inimigo.vida}")
    print(f"Cartas na mão do jogador: {len(jogador.mao)}")
    print(f"Campo do jogador: {jogador.campo}")
    print(f"Campo do inimigo: {inimigo.campo}")

print("\n--- Testes finalizados ---")
