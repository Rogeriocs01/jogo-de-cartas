import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
from interface_pygame.menu_pygame import MenuInicialPygame
from interface_pygame.selecao_heroi_pygame import SelecaoHeroiPygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interface Jogo de Cartas")
clock = pygame.time.Clock()

# Controlador de estado de tela
tela_atual = "menu"
menu = MenuInicialPygame(screen)
selecao = SelecaoHeroiPygame(screen)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if tela_atual == "menu":
                escolha = menu.verificar_clique(event.pos)
                if escolha == "Selecionar Herói":
                    tela_atual = "selecao_heroi"
            elif tela_atual == "selecao_heroi":
                if selecao.verificar_clique(event.pos):
                    tela_atual = "menu"  # volta ao menu após escolher

    if tela_atual == "menu":
        menu.desenhar()
    elif tela_atual == "selecao_heroi":
        selecao.desenhar()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
