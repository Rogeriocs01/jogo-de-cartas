# interface_pygame/menu_pygame.py
import pygame
# Adiciona o diretório raiz do projeto ao sys.path
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from interface_pygame.deck_builder_pygame import abrir_deckbuilder_pygame


class MenuInicialPygame:
    def __init__(self, screen):
        self.screen = screen
        self.largura = screen.get_width()
        self.altura = screen.get_height()
        self.fonte = pygame.font.SysFont("arial", 28)

        self.botoes = [
            "Selecionar Herói",
            "Editar Deck Manualmente",
            "Iniciar Campanha",
            "Ver Inventário",
            "Ver Painel de Progresso",
            "Ver Mapa da Campanha",
            "Acessar Loja",
            "Ver Status do Jogador",
            "Sair"
        ]
        self.botoes_rects = []

    def desenhar(self):
        self.screen.fill((20, 20, 20))
        titulo = self.fonte.render("Menu Principal", True, (255, 255, 255))
        self.screen.blit(titulo, (self.largura // 2 - titulo.get_width() // 2, 40))
        self.botoes_rects = []

        for i, texto in enumerate(self.botoes):
            x = self.largura // 2 - 200
            y = 100 + i * 60
            rect = pygame.Rect(x, y, 400, 50)
            pygame.draw.rect(self.screen, (70, 70, 70), rect, border_radius=8)
            pygame.draw.rect(self.screen, (255, 255, 255), rect, 2, border_radius=8)

            texto_render = self.fonte.render(texto, True, (255, 255, 255))
            self.screen.blit(texto_render, (x + 20, y + 10))
            self.botoes_rects.append((rect, texto))

    def verificar_clique(self, pos):
        for rect, texto in self.botoes_rects:
            if rect.collidepoint(pos):
                print(f"🖱️ Botão clicado: {texto}")
                return texto
        return None

