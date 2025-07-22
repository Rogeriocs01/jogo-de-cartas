# testes/teste_habilidades_heroi.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from testes.jogador_teste import JogadorTeste
from habilidades import habilidades_heroi

print("\n--- Teste de Habilidades de Herói ---\n")

jogador = JogadorTeste(nome='Herói Teste', vida=20, mana=5)
inimigo = JogadorTeste(nome='Inimigo Teste', vida=20, mana=5)

# 1. Curar
print("1. Testando curar:")
habilidades_heroi.curar_heroi(jogador)

# 2. Dano direto
print("\n2. Testando dano direto:")
habilidades_heroi.dano_heroi(jogador, inimigo)

# 3. Comprar cartas
print("\n3. Testando compra de cartas:")
habilidades_heroi.comprar_cartas(jogador)

# 4. Reduzir custo de mana
print("\n4. Testando redução de custo de mana:")
jogador.mao = [type('Carta', (), {'custo_mana': 3})() for _ in range(3)]
habilidades_heroi.reduzir_custo_mana(jogador)
print([c.custo_mana for c in jogador.mao])

# 5. Manipulação de mana
print("\n5. Testando manipulação de mana:")
habilidades_heroi.manipulacao_mana(jogador)

# 6. Reutilizar habilidade
print("\n6. Testando reutilização de habilidades:")
carta_falsa = type('Carta', (), {'habilidade_usada': True})()
jogador.campo[0] = carta_falsa
habilidades_heroi.reutilizar_habilidade(jogador)
print(jogador.campo[0].habilidade_usada)

# 7. Espionagem
print("\n7. Testando espionagem:")
inimigo.mao = [type('Carta', (), {'nome': f"Carta_{i}"})() for i in range(3)]
habilidades_heroi.espionagem(jogador, inimigo)

# 8. Furto temporário
print("\n8. Testando furto temporário:")
carta_para_furto = type('Carta', (), {'nome': "Dragão de Lava"})()
inimigo.campo[0] = carta_para_furto
habilidades_heroi.furto_temporario(jogador, inimigo)

print("\n--- Testes finalizados ---")
