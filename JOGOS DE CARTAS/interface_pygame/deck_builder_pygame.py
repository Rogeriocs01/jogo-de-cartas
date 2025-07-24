# interface_pygame/deck_builder_pygame.py

import pygame
import sys
import os

# Ajuste o sys.path para importar corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gerenciamento', 'deck')))

from gerenciamento.deck.deck_manager import montar_deck_manual, salvar_deck_personalizado, get_tamanho_maximo_deck
from gerenciamento.inventario_jogador import carregar_inventario
from cartas.card_repository import get_carta_by_id

def abrir_deckbuilder_pygame(screen, nome_heroi):
    class DeckBuilderPygame:
        def __init__(self):
            self.heroi_nome = nome_heroi
            self.inventario = carregar_inventario()
            self.deck = montar_deck_manual(self.heroi_nome)
            self.tamanho_max = get_tamanho_maximo_deck(self.heroi_nome)
            self.limite_por_carta = 3

            self.screen = screen
            self.fonte = pygame.font.SysFont("arial", 22)
            self.clock = pygame.time.Clock()

            self.botoes_inventario = []
            self.botoes_deck = []

        def desenhar_texto(self, texto, x, y, cor=(255, 255, 255)):
            img = self.fonte.render(texto, True, cor)
            self.screen.blit(img, (x, y))

        def contar_ocorrencias(self, carta_nome):
            return sum(1 for c in self.deck if c.nome == carta_nome)

        def executar(self):
            rodando = True
            while rodando:
                self.screen.fill((20, 20, 20))
                self.botoes_inventario = []
                self.botoes_deck = []

                self.desenhar_texto(f"Montando deck de: {self.heroi_nome}", 30, 20)
                self.desenhar_texto(f"Cartas no deck: {len(self.deck)} / {self.tamanho_max}", 30, 50)

                # INVENTÁRIO
                y_offset = 100
                self.desenhar_texto("INVENTÁRIO:", 30, y_offset)
                y_offset += 30
                for cid, qtd in self.inventario.items():
                    if qtd == 0:
                        continue
                    texto = f"{cid} (x{qtd})"
                    self.desenhar_texto(texto, 40, y_offset)
                    botao_rect = pygame.Rect(300, y_offset, 30, 25)
                    pygame.draw.rect(self.screen, (0, 200, 0), botao_rect)
                    self.desenhar_texto("+", botao_rect.x + 8, botao_rect.y + 2, (0, 0, 0))
                    self.botoes_inventario.append((botao_rect, cid))
                    y_offset += 30

                # DECK
                y_offset = 100
                self.desenhar_texto("DECK:", 550, y_offset)
                y_offset += 30

                tipos_adicionados = {}
                for carta in self.deck:
                    nome = carta.nome
                    tipos_adicionados[nome] = tipos_adicionados.get(nome, 0) + 1

                for nome, qtd in tipos_adicionados.items():
                    self.desenhar_texto(f"{nome} (x{qtd})", 560, y_offset)
                    botao_rect = pygame.Rect(850, y_offset, 30, 25)
                    pygame.draw.rect(self.screen, (200, 0, 0), botao_rect)
                    self.desenhar_texto("-", botao_rect.x + 8, botao_rect.y + 2, (0, 0, 0))
                    self.botoes_deck.append((botao_rect, nome))
                    y_offset += 30

                # Botão Salvar
                salvar_rect = pygame.Rect(400, 640, 200, 40)
                pygame.draw.rect(self.screen, (100, 200, 255), salvar_rect, border_radius=10)
                self.desenhar_texto("Salvar Deck", salvar_rect.x + 40, salvar_rect.y + 8, (0, 0, 0))

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                        pos = pygame.mouse.get_pos()

                        # Adicionar carta
                        for rect, cid in self.botoes_inventario:
                            if rect.collidepoint(pos):
                                qtd_no_deck = self.contar_ocorrencias(cid)
                                qtd_no_inventario = self.inventario.get(cid, 0)
                                if (len(self.deck) < self.tamanho_max and 
                                    qtd_no_deck < min(qtd_no_inventario, self.limite_por_carta)):
                                    try:
                                        carta = get_carta_by_id(cid)
                                        self.deck.append(carta)
                                    except ValueError:
                                        pass

                        # Remover carta
                        for rect, nome in self.botoes_deck:
                            if rect.collidepoint(pos):
                                for carta in self.deck:
                                    if carta.nome == nome:
                                        self.deck.remove(carta)
                                        break

                        # Salvar
                        if salvar_rect.collidepoint(pos):
                            salvar_deck_personalizado(self.heroi_nome, self.deck)
                            print("\n💾 Deck salvo com sucesso!")
                            rodando = False

                pygame.display.flip()
                self.clock.tick(60)

    # Executa a tela do deck builder
    tela = DeckBuilderPygame()
    tela.executar()
