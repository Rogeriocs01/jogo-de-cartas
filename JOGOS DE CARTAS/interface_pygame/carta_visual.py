import pygame
import os

pygame.init()

# --- Caminhos ---
CAMINHO_IMAGENS = os.path.join("interface_pygame", "assets", "cartas")
CAMINHO_MOLDURAS = os.path.join("interface_pygame", "assets", "molduras")

# --- Dimensões da carta ---
CARD_WIDTH = 100
CARD_HEIGHT = 140

# --- Layout relativo ---
LAYOUT = {
    "nome_y": 0.02, "nome_size": 0.08,   # Nome menor
    "atk_y":  0.78, "atk_size": 0.10,    # ATK
    "def_y":  0.78, "def_size": 0.10,    # DEF
    "mana_y": 0.90, "mana_size": 0.09,   # Mana
    "hab_y":  0.93, "hab_size": 0.07,    # Habilidade
}

# --- Função para carregar arte da carta ---
def carregar_imagem(nome_arquivo):
    caminho = os.path.join(CAMINHO_IMAGENS, nome_arquivo)
    print(f"🎴 Tentando carregar arte: {caminho}")  # Debug no console

    if os.path.exists(caminho):
        return pygame.transform.scale(pygame.image.load(caminho), (CARD_WIDTH, CARD_HEIGHT))
    else:
        print(f"⚠️ Arte não encontrada: {caminho}")
        imagem = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        imagem.fill((60, 60, 60))
        fonte_debug = pygame.font.SysFont("arial", 12)
        texto = fonte_debug.render("Sem Img", True, (255, 255, 255))
        imagem.blit(texto, (5, 60))
        return imagem

# --- Função para carregar moldura ---
def carregar_moldura(raridade):
    nome_arquivo = f"{raridade.lower()}.webp"
    caminho = os.path.join(CAMINHO_MOLDURAS, nome_arquivo)

    if os.path.exists(caminho):
        return pygame.transform.scale(pygame.image.load(caminho), (CARD_WIDTH, CARD_HEIGHT))
    else:
        print(f"⚠️ Moldura não encontrada: {caminho}")
        s = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
        s.fill((200, 200, 200, 100))
        return s

# --- Desenhar carta normal ---
def desenhar_carta(screen, carta, x, y, width=CARD_WIDTH, height=CARD_HEIGHT):
    carta_surf = pygame.Surface((width, height), pygame.SRCALPHA)

    # Arte
    carta_surf.blit(pygame.transform.scale(carta["arte"], (width, height)), (0, 0))

    # Moldura
    carta_surf.blit(pygame.transform.scale(carta["moldura"], (width, height)), (0, 0))

    # Nome
    fonte_nome = pygame.font.SysFont("arial", int(height * LAYOUT["nome_size"]), bold=True)
    texto_nome = fonte_nome.render(carta["nome"], True, (255, 255, 255))
    carta_surf.blit(texto_nome, (5, int(height * LAYOUT["nome_y"])))

    # Atributos
    fonte_attr = pygame.font.SysFont("arial", int(height * 0.10), bold=True)

    texto_atk = fonte_attr.render(str(carta.get("atk", 0)), True, (255, 0, 0))
    carta_surf.blit(texto_atk, (5, int(height * LAYOUT["atk_y"] * height)))

    texto_def = fonte_attr.render(str(carta.get("def", 0)), True, (0, 0, 255))
    carta_surf.blit(texto_def, (width - 20, int(height * LAYOUT["def_y"] * height)))

    texto_mana = fonte_attr.render(str(carta.get("mana", 0)), True, (0, 255, 255))
    carta_surf.blit(texto_mana, (5, int(height * LAYOUT["mana_y"] * height)))

    # Habilidade
    if "habilidade" in carta:
        fonte_hab = pygame.font.SysFont("arial", int(height * LAYOUT["hab_size"]))
        texto_hab = fonte_hab.render(carta["habilidade"], True, (200, 200, 200))
        carta_surf.blit(texto_hab, (5, int(height * LAYOUT["hab_y"] * height)))

    screen.blit(carta_surf, (x, y))
    return pygame.Rect(x, y, width, height)

# --- Desenhar carta em zoom ---
def desenhar_carta_zoom(screen, carta):
    zoom_w, zoom_h = 300, 420
    x = (screen.get_width() - zoom_w) // 2
    y = (screen.get_height() - zoom_h) // 2

    fundo = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    fundo.fill((0, 0, 0, 180))
    screen.blit(fundo, (0, 0))

    desenhar_carta(screen, carta, x, y, zoom_w, zoom_h)
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type in (pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                esperando = False
