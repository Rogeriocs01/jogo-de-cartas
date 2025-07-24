# herois/gerenciador_heroi.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cartas.card_repository import get_carta_by_id
from personagens_data import herois_disponiveis

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
            from cartas.card_repository import get_carta_by_id
            carta_id = self.deck.pop(0)
            carta = get_carta_by_id(carta_id)
            self.mao.append(carta)
            print(f"{self.nome} comprou uma carta: {carta.nome}")

        else:
            print(f"{self.nome} não tem mais cartas para comprar.")

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
