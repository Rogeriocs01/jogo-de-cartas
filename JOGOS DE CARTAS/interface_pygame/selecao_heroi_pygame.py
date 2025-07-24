# interface_pygame/selecao_heroi_pygame.py
import pygame
import os
import sys
import json

# Adiciona raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jogador.gerenciador_herois import carregar_herois

class SelecaoHeroiPygame:
    def __init__(self, screen):
        self.screen = screen
        self.herois = carregar_herois()
        self.fonte = pygame.font.SysFont("arial", 24)
        self.botoes = []

    def desenhar(self):
        self.screen.fill((30, 30, 30))
        titulo = self.fonte.render("Selecione seu Herói", True, (255, 255, 255))
        self.screen.blit(titulo, (self.screen.get_width() // 2 - titulo.get_width() // 2, 40))
        self.botoes = []

        for i, heroi in enumerate(self.herois):
            nome = heroi["nome"]
            y = 100 + i * 70
            rect = pygame.Rect(100, y, 400, 50)
            pygame.draw.rect(self.screen, (60, 60, 60), rect, border_radius=6)
            pygame.draw.rect(self.screen, (255, 255, 255), rect, 2, border_radius=6)

            texto = self.fonte.render(nome, True, (255, 255, 255))
            self.screen.blit(texto, (120, y + 10))
            self.botoes.append((rect, nome))

    def verificar_clique(self, pos):
        for rect, nome in self.botoes:
            if rect.collidepoint(pos):
                self.salvar_heroi_escolhido(nome)
                print(f"✅ Herói selecionado: {nome}")
                return True
        return False

    def salvar_heroi_escolhido(self, nome_heroi):
        caminho = os.path.join("dados", "escolha_heroi.json")
        with open(caminho, "w") as f:
            json.dump({"heroi_escolhido": nome_heroi}, f)
