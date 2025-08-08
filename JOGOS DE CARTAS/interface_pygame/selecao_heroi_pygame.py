# interface_pygame/selecao_heroi_pygame.py
import pygame
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from herois.gerenciador_heroi import carregar_herois

CAMINHO_IMAGENS_HEROIS = os.path.join("interface_pygame", "assets", "herois")

class SelecaoHeroiPygame:
    def __init__(self, screen):
        self.screen = screen
        self.herois = carregar_herois()
        self.fonte = pygame.font.SysFont("arial", 24)
        self.botoes = []
        self.heroi_selecionado = None
        self.scroll_offset = 0
        self.max_scroll = max(0, len(self.herois) * 160 - self.screen.get_height() + 100)
        self.botao_confirmar = None

    def desenhar(self):
        self.screen.fill((30, 30, 30))
        self.botoes = []

        titulo = self.fonte.render("Selecione seu Herói", True, (255, 255, 255))
        self.screen.blit(titulo, (self.screen.get_width() // 2 - titulo.get_width() // 2, 20))

        y_inicial = 80 - self.scroll_offset
        for i, heroi in enumerate(self.herois):
            nome = heroi["nome"]
            y = y_inicial + i * 160

            # Card do herói
            card_rect = pygame.Rect(100, y, 300, 140)
            cor_borda = (255, 255, 0) if self.heroi_selecionado == nome else (255, 255, 255)
            pygame.draw.rect(self.screen, (60, 60, 60), card_rect, border_radius=6)
            pygame.draw.rect(self.screen, cor_borda, card_rect, 3, border_radius=6)

            # Nome
            texto = self.fonte.render(nome, True, (255, 255, 255))
            self.screen.blit(texto, (120, y + 10))

            # Imagem (se existir)
            imagem_path = os.path.join(CAMINHO_IMAGENS_HEROIS, f"{nome}.png")
            if os.path.exists(imagem_path):
                imagem = pygame.image.load(imagem_path)
                imagem = pygame.transform.scale(imagem, (100, 100))
                self.screen.blit(imagem, (120, y + 40))

            self.botoes.append((card_rect, nome))

        # Botão Confirmar
        if self.heroi_selecionado:
            self.botao_confirmar = pygame.Rect(self.screen.get_width() - 220, self.screen.get_height() - 60, 180, 40)
            pygame.draw.rect(self.screen, (0, 200, 0), self.botao_confirmar, border_radius=6)
            texto = self.fonte.render("Confirmar Seleção", True, (0, 0, 0))
            self.screen.blit(texto, (self.botao_confirmar.x + 10, self.botao_confirmar.y + 8))
        else:
            self.botao_confirmar = None

        pygame.display.flip()

    def verificar_clique(self, pos):
        # Verifica botões dos heróis
        for rect, nome in self.botoes:
            if rect.collidepoint(pos):
                self.heroi_selecionado = nome
                print(f"🟡 Herói selecionado visualmente: {nome}")
                return None

        # Verifica botão confirmar
        if self.botao_confirmar and self.botao_confirmar.collidepoint(pos):
            self.salvar_heroi_escolhido(self.heroi_selecionado)
            print(f"✅ Herói confirmado: {self.heroi_selecionado}")
            return {
                "nome": self.heroi_selecionado
            }

        return None

    def salvar_heroi_escolhido(self, nome_heroi):
        caminho = os.path.join("dados", "escolha_heroi.json")
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump({"heroi_escolhido": nome_heroi}, f, ensure_ascii=False)

    def rolar(self, direcao):
        if direcao == "cima":
            self.scroll_offset = max(0, self.scroll_offset - 30)
        elif direcao == "baixo":
            self.scroll_offset = min(self.max_scroll, self.scroll_offset + 30)
