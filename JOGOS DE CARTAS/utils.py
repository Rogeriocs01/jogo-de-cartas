

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione Enter para continuar...")

def exibir_mao(jogador):
    print(f"\n🖐️ Mão de {jogador.nome}:")
    for i, carta in enumerate(jogador.mao):
        if carta:
            print(f"  [{i}] {carta.nome} (ATK: {carta.ataque}, DEF: {carta.defesa}, Mana: {carta.custo_mana})")
        else:
            print(f"  [{i}] Vazio")

def exibir_campo(jogador, inimigo):
    print("\n🎯 Campo de Batalha:")
    print(f"{jogador.nome}:")
    for i, carta in enumerate(jogador.campo):
        if carta:
            print(f"  🧙 Slot {i}: {carta.nome} (ATK: {carta.ataque}, DEF: {carta.defesa})")
        else:
            print(f"  🧙 Slot {i}: Vazio")

    print(f"\n{inimigo.nome}:")
    for i, carta in enumerate(inimigo.campo):
        if carta:
            print(f"  👹 Slot {i}: {carta.nome} (ATK: {carta.ataque}, DEF: {carta.defesa})")
        else:
            print(f"  👹 Slot {i}: Vazio")

def exibir_status(jogador, inimigo):
    print("\n❤️ Status dos Jogadores:")
    print(f"{jogador.nome}: Vida = {jogador.vida} | Mana = {jogador.mana}")
    print(f"{inimigo.nome}: Vida = {inimigo.vida} | Mana = {inimigo.mana}")
