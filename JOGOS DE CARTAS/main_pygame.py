# main_pygame.py
import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da janela
LARGURA = 1000
ALTURA = 700
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Cartas - Campo de Batalha")

# Cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)
AZUL = (0, 150, 255)
CINZA = (80, 80, 80)
AMARELO = (255, 215, 0)

# Fonte para textos
fonte = pygame.font.SysFont("arial", 24)

# Mão do jogador (nomes simulados)
mao_jogador = ["Fúria Bélica", "Poção de Vida", "Centelha de Luz", "Clarividência"]
mensagem = "Clique em uma carta da mão."
carta_clicada_index = None

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))  # fundo cinza escuro
    mao_rects = []

    # 🔁 Criar retângulos da mão do jogador ANTES dos eventos
    for i, nome in enumerate(mao_jogador):
        x = 60 + i * 230
        y = 630
        rect = pygame.Rect(x, y, 180, 50)
        mao_rects.append(rect)

    # Eventos (teclado, mouse, sair do jogo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for i, rect in enumerate(mao_rects):
                if rect.collidepoint(pos):
                    carta_clicada_index = i
                    carta_clicada = mao_jogador[i]
                    print(f"🖱️ Carta clicada: {carta_clicada}")
                    mensagem = f"Você clicou: {carta_clicada}"

    # Desenhar campo do inimigo
    for i in range(5):
        pygame.draw.rect(screen, AZUL, (100 + i*160, 100, 120, 160), border_radius=8)

    # Desenhar campo do jogador
    for i in range(5):
        pygame.draw.rect(screen, VERDE, (100 + i*160, 440, 120, 160), border_radius=8)

    # Mostrar vida/mana
    texto_vida = fonte.render("❤️ Vida: 20", True, BRANCO)
    texto_mana = fonte.render("🔷 Mana: 3", True, BRANCO)
    screen.blit(texto_vida, (20, 20))
    screen.blit(texto_mana, (20, 50))

    # Mostrar mão do jogador (com destaque para a carta clicada)
    for i, rect in enumerate(mao_rects):
        cor = AMARELO if i == carta_clicada_index else CINZA
        pygame.draw.rect(screen, cor, rect, border_radius=6)
        texto_carta = fonte.render(mao_jogador[i], True, PRETO if i == carta_clicada_index else BRANCO)
        screen.blit(texto_carta, (rect.x + 10, rect.y + 10))

    # Mostrar mensagem no topo
    texto_msg = fonte.render(mensagem, True, BRANCO)
    screen.blit(texto_msg, (LARGURA // 2 - texto_msg.get_width() // 2, 580))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
