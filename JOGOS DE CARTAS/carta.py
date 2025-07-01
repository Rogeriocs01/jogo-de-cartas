class Carta:
    def __init__(
        self,
        nome: str,
        custo_mana: int,
        ataque: int,
        defesa: int,
        habilidade: str,
        custo_habilidade: int,
        tipo_terreno: str,
        raridade: str
    ):
        self.nome = nome
        self.custo_mana = custo_mana
        self.ataque = ataque
        self.defesa = defesa
        self.habilidade = habilidade
        self.custo_habilidade = custo_habilidade
        self.tipo_terreno = tipo_terreno
        self.raridade = raridade
        self.habilidade_usada = False  # <- ESSENCIAL

    def __str__(self):
        return (
            f"{self.nome} | Custo: {self.custo_mana} | ATK: {self.ataque} | DEF: {self.defesa} | "
            f"Habilidade: {self.habilidade} | Terreno: {self.tipo_terreno} | Raridade: {self.raridade}"
        )
