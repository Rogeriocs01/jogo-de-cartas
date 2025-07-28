import pygame

class CartaVisual:
    def __init__(self, carta_data, imagem_arte, moldura_img, fontes):
        self.dados = carta_data
        self.imagem_arte = imagem_arte
        self.moldura = moldura_img
        self.fontes = fontes

    def desenhar(self, surface, posicao):
        x, y = posicao
        surface.blit(self.imagem_arte, (x + 50, y + 100))  # ajuste conforme tamanho
        surface.blit(self.moldura, (x, y))

        nome_render = self.fontes['grande'].render(self.dados["nome"], True, (255, 255, 255))
        surface.blit(nome_render, (x + 110, y + 30))  # nome no topo

        ataque = self.fontes['media'].render(str(self.dados["ataque"]), True, (255, 0, 0))
        defesa = self.fontes['media'].render(str(self.dados["defesa"]), True, (0, 0, 255))
        mana = self.fontes['media'].render(str(self.dados["mana"]), True, (0, 255, 255))

        surface.blit(ataque, (x + 370, y + 50))   # ajuste conforme ícone
        surface.blit(defesa, (x + 370, y + 460))
        surface.blit(mana, (x + 40, y + 460))

        # Habilidade ou descrição
        if self.dados.get("descricao"):
            descricao = self.fontes['pequena'].render(self.dados["descricao"], True, (255, 255, 255))
            surface.blit(descricao, (x + 40, y + 520))

