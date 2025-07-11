# interface_pygame/main_pygame.py
import pygame
import sys
from menu_pygame import MenuInicialPygame
from selecao_heroi_pygame import SelecaoHeroiPygame




# Inicialização do Pygame
pygame.init()

# Configurações da janela
LARGURA = 1000
ALTURA = 700
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Cartas")

# Controle de estados do jogo
estado = "menu"  # estados: menu, selecao_heroi, etc.
menu_visual = MenuInicialPygame(screen)
selecao_heroi = SelecaoHeroiPygame(screen)
heroi_atual = None

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            if estado == "menu":
                acao = menu_visual.verificar_clique(pos)
                if acao == "Selecionar Herói":
                    estado = "selecao_heroi"
                elif acao == "Sair":
                    running = False
                elif acao:
                    print(f"🖱️ Menu: {acao}")

            elif estado == "selecao_heroi":
                resultado = selecao_heroi.verificar_clique(pos)
                if isinstance(resultado, dict):
                    heroi_atual = resultado
                    print(f"🎮 Herói ativo: {heroi_atual['nome']}")
                    estado = "menu"
                elif resultado == "voltar":
                    estado = "menu"

    # Desenhar a tela atual
    if estado == "menu":
        menu_visual.desenhar()
    elif estado == "selecao_heroi":
        selecao_heroi.desenhar()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
