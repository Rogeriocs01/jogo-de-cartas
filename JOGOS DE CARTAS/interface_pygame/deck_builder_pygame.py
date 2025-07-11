# interface_pygame/deck_builder_pygame.py
import pygame
import sys
from inventario_jogador import carregar_inventario
from deck_manager import salvar_deck_personalizado
from card_repository import get_carta_by_id
from progresso_heroi import carregar_progresso

# Provisório: calcula o tamanho máximo do deck com base no nível
def get_tamanho_maximo_deck(nivel):
    return 10 + (nivel - 1) * 2

class DeckBuilderPygame:
    def __init__(self, heroi):
        pygame.init()
        self.heroi = heroi
        self.nome_heroi = heroi["nome"]
        self.inventario = carregar_inventario()
        self.deck = []
        self.cartas_por_tipo = {}

        progresso = carregar_progresso()
        nivel = progresso.get(self.nome_heroi, {}).get("nivel", 1)
        self.tamanho_max = get_tamanho_maximo_deck(nivel)
        self.limite_por_carta = 3

        self.LARGURA = 1000
        self.ALTURA = 700
        self.screen = pygame.display.set_mode((self.LARGURA, self.ALTURA))
        pygame.display.set_caption("Montar Deck - Pygame")

        self.fonte = pygame.font.SysFont("arial", 22)
        self.clock = pygame.time.Clock()

        self.botoes_inventario = []
        self.botoes_deck = []

        self.executar()

    def desenhar_texto(self, texto, x, y, cor=(255, 255, 255)):
        img = self.fonte.render(texto, True, cor)
        self.screen.blit(img, (x, y))

    def executar(self):
        rodando = True
        while rodando:
            self.screen.fill((20, 20, 20))
            self.botoes_inventario = []
            self.botoes_deck = []

            self.desenhar_texto(f"Montando deck de: {self.nome_heroi}", 30, 20)
            self.desenhar_texto(f"Cartas no deck: {len(self.deck)} / {self.tamanho_max}", 30, 50)

            # INVENTARIO
            y_offset = 100
            self.desenhar_texto("INVENTÁRIO:", 30, y_offset)
            y_offset += 30
            for i, (cid, qtd) in enumerate(self.inventario.items()):
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
            for i, carta in enumerate(self.deck):
                nome = carta.nome
                if nome in tipos_adicionados:
                    tipos_adicionados[nome] += 1
                else:
                    tipos_adicionados[nome] = 1
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
                    rodando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    pos = pygame.mouse.get_pos()

                    for rect, cid in self.botoes_inventario:
                        if rect.collidepoint(pos):
                            if len(self.deck) < self.tamanho_max and self.deck.count(get_carta_by_id(cid)) < min(self.inventario[cid], self.limite_por_carta):
                                self.deck.append(get_carta_by_id(cid))

                    for rect, nome in self.botoes_deck:
                        if rect.collidepoint(pos):
                            for carta in self.deck:
                                if carta.nome == nome:
                                    self.deck.remove(carta)
                                    break

                    if salvar_rect.collidepoint(pos):
                        salvar_deck_personalizado(self.nome_heroi, self.deck)
                        print("\n💾 Deck salvo com sucesso!")
                        rodando = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    heroi_exemplo = {"nome": "Thorin"}
    DeckBuilderPygame(heroi_exemplo)
