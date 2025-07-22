# testes/jogador_teste.py

class JogadorTeste:
    def __init__(self, nome='Jogador Teste', vida=20, mana=5):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.mao = []
        self.campo = [None] * 5  # Simula 5 slots no campo de batalha

    def comprar_carta(self):
        print(f"{self.nome} comprou uma carta (simulação).")
