# herois/gerenciador_heroi.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.personagens_data import herois_disponiveis
from cartas.card_repository import get_carta_by_id



class Heroi:
    def __init__(self, nome, terreno, habilidade_especial, custo_habilidade):
        self.nome = nome
        self.vida = 20
        self.mana = 0
        self.mao = []
        self.campo = [None] * 5
        self.deck = []
        self.terreno = terreno
        self.habilidade_especial = habilidade_especial
        self.custo_habilidade = custo_habilidade

    def comprar_carta(self):
        if self.deck:
            carta_id = self.deck.pop(0)
            carta = get_carta_by_id(carta_id)
            self.mao.append(carta)
            print(f"{self.nome} comprou uma carta: {carta.nome}")
        else:
            print(f"{self.nome} não tem mais cartas para comprar.")

    def invocar_carta(self):
        if not self.mao:
            print("❌ Você não tem cartas na mão.")
            input("Pressione ENTER para continuar...")
            return

        print("\n🃏 Sua mão:")
        for i, carta in enumerate(self.mao):
            print(f"[{i}] {carta.nome} (ATK: {carta.ataque}, DEF: {carta.defesa}, Mana: {carta.custo_mana})")

        try:
            escolha = int(input("Escolha o número da carta para invocar: "))
            carta = self.mao[escolha]
        except (ValueError, IndexError):
            print("❌ Escolha inválida.")
            input("Pressione ENTER para continuar...")
            return

        if self.mana < carta.custo_mana:
            print("❌ Mana insuficiente.")
            input("Pressione ENTER para continuar...")
            return

        for i in range(len(self.campo)):
            if self.campo[i] is None:
                self.campo[i] = carta
                self.mao.remove(carta)
                self.mana -= carta.custo_mana
                print(f"✅ {carta.nome} foi invocada para o campo no slot {i}.")
                input("Pressione ENTER para continuar...")
                return

        print("⚠️ Todos os slots do campo estão ocupados.")
        input("Pressione ENTER para continuar...")

    def atacar(self, inimigo):
        print("\n🎯 Suas cartas no campo:")
        cartas_ativas = [(i, c) for i, c in enumerate(self.campo) if c is not None]

        if not cartas_ativas:
            print("❌ Você não tem cartas no campo para atacar.")
            input("Pressione ENTER para continuar...")
            return

        for i, carta in cartas_ativas:
            print(f"[{i}] {carta.nome} (ATK: {carta.ataque}, DEF: {carta.defesa})")

        try:
            slot_atacante = int(input("Escolha o número da carta para atacar: "))
            atacante = self.campo[slot_atacante]
        except (ValueError, IndexError):
            print("❌ Escolha inválida.")
            input("Pressione ENTER para continuar...")
            return

        print("\n🎯 Campo inimigo:")
        for i, carta in enumerate(inimigo.campo):
            if carta:
                print(f"[{i}] {carta.nome} (DEF: {carta.defesa})")
            else:
                print(f"[{i}] Vazio")

        try:
            slot_alvo = int(input("Escolha o slot do inimigo para atacar: "))
            alvo = inimigo.campo[slot_alvo]
        except (ValueError, IndexError):
            print("❌ Escolha inválida.")
            input("Pressione ENTER para continuar...")
            return

        if alvo:
            print(f"⚔️ {atacante.nome} (ATK {atacante.ataque}) ataca {alvo.nome} (DEF {alvo.defesa})!")
            if atacante.ataque >= alvo.defesa:
                print(f"💥 {alvo.nome} foi destruída!")
                inimigo.campo[slot_alvo] = None
            else:
                print(f"🛡️ {alvo.nome} resistiu ao ataque.")
        else:
            print(f"⚔️ {atacante.nome} atacou diretamente o inimigo!")
            inimigo.vida -= atacante.ataque
            print(f"💔 Vida do inimigo reduzida para {inimigo.vida}.")

        input("Pressione ENTER para continuar...")


def carregar_heroi(nome_heroi):
    for h in herois_disponiveis:
        if h["nome"] == nome_heroi:
            return Heroi(
                nome=h["nome"],
                terreno=h["terreno"],
                habilidade_especial=h["habilidade_especial"],
                custo_habilidade=h["custo_habilidade"]
            )
    raise ValueError(f"Herói '{nome_heroi}' não encontrado na lista.")

def carregar_herois():
    herois = []
    for h in herois_disponiveis:
        herois.append({
            "nome": h["nome"],
            "terreno": h["terreno"],
            "habilidade_especial": h["habilidade_especial"],
            "custo_habilidade": h["custo_habilidade"]
        })
    return herois
