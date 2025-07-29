import pygame
import os
import sys
import unicodedata
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from cartas.card_repository import get_carta_by_id, get_carta_by_nome, card_repository

todas_as_cartas = list(card_repository.values())  # Se ainda não tiver 'todas_as_cartas'

pygame.init()
tela = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Visualizar Cartas")
fonte = pygame.font.SysFont(None, 24)

CAMINHO_IMAGENS = os.path.join("interface_pygame", "assets", "cartas")

def carregar_imagem(nome_arquivo):
    caminho = os.path.join(CAMINHO_IMAGENS, f"{nome_arquivo}.png")
    if not os.path.exists(caminho):
        print(f"[ERRO] Imagem não encontrada: {caminho}")
        return None
    return pygame.image.load(caminho)

cartas = []
for carta in todas_as_cartas:
    nome_formatado = carta["nome"].replace(" ", "_").replace("ã", "a").replace("ç", "c").replace("é", "e").replace("ô", "o")
    imagem = carregar_imagem(nome_formatado)
    if imagem:
        cartas.append((imagem, carta["nome"]))

# Organiza as cartas na tela
tela.fill((30, 30, 30))
x, y = 20, 20
espaco = 10
largura_maxima = 1100

for imagem, nome in cartas:
    tela.blit(imagem, (x, y))
    texto = fonte.render(nome, True, (255, 255, 255))
    tela.blit(texto, (x, y + imagem.get_height() + 5))
    x += imagem.get_width() + espaco
    if x > largura_maxima:
        x = 20
        y += imagem.get_height() + 50

pygame.display.flip()

# Espera fechar janela
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

pygame.quit()
