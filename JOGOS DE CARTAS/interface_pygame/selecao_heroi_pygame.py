# interface_pygame/selecao_heroi_pygame.py
import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from personagens_data import personagens


class SelecaoHeroiPygame:
    def __init__(self, screen):
        self.screen = screen
        self.largura = screen.get_width()
        self.altura = screen.get_height()
        self.fonte = pygame.font.SysFont("arial", 22)
        self.herois = personagens
        self.heroi_selecionado = None
        self.botoes = []

    def desenhar(self):
        self.screen.fill((15, 15, 15))
        titulo = self.fonte.render("Selecione seu Herói", True, (255, 255, 255))
        self.screen.blit(titulo, (self.largura // 2 - titulo.get_width() // 2, 20))
        self.botoes = []

        colunas = 3
        espacamento_x = 300
        espacamento_y = 130
        margem_x = 60
        margem_y = 70

        for i, heroi in enumerate(self.herois):
            col = i % colunas
            lin = i // colunas

            x = margem_x + col * espacamento_x
            y = margem_y + lin * espacamento_y
            rect = pygame.Rect(x, y, 260, 100)

            pygame.draw.rect(self.screen, (50, 50, 50), rect, border_radius=8)
            pygame.draw.rect(self.screen, (255, 255, 255), rect, 2, border_radius=8)

            nome = self.fonte.render(f"Nome: {heroi['nome']}", True, (255, 255, 255))
            terreno = self.fonte.render(f"Terreno: {heroi['terreno']}", True, (180, 180, 180))
            habilidade = self.fonte.render(f"Habilidade: {heroi['habilidade_especial'] or 'N/A'}", True, (180, 180, 180))

            self.screen.blit(nome, (x + 10, y + 10))
            self.screen.blit(terreno, (x + 10, y + 35))
            self.screen.blit(habilidade, (x + 10, y + 60))

            self.botoes.append((rect, heroi))

        self.botao_voltar = pygame.Rect(20, self.altura - 60, 150, 40)
        pygame.draw.rect(self.screen, (100, 100, 100), self.botao_voltar, border_radius=6)
        texto_voltar = self.fonte.render("← Voltar", True, (255, 255, 255))
        self.screen.blit(texto_voltar, (self.botao_voltar.x + 20, self.botao_voltar.y + 8))

    def verificar_clique(self, pos):
        for rect, heroi in self.botoes:
            if rect.collidepoint(pos):
                print(f"✅ Herói selecionado: {heroi['nome']}")
                self.heroi_selecionado = heroi
                return heroi

        if self.botao_voltar.collidepoint(pos):
            return "voltar"

        return None
