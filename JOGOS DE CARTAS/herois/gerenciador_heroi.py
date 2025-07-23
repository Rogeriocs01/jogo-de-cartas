# herois/gerenciador_heroi.py


from personagens_data import herois_disponiveis


class Heroi:
    def __init__(self, nome, terreno, habilidade_especial, custo_habilidade):
        self.nome = nome
        self.vida = 20
        self.mana = 0
        self.mao = []
        self.campo = [None] * 5
        self.deck = []
        self.habilidade_especial = habilidade_especial
        self.custo_habilidade = custo_habilidade

def carregar_heroi(nome):
    for p in personagens:
        if p["nome"] == nome:
            return Heroi(
                nome=p["nome"],
                terreno=p["terreno"],
                habilidade_especial=p["habilidade_especial"],
                custo_habilidade=p["custo_habilidade"]
            )
    raise ValueError(f"Herói {nome} não encontrado.")
