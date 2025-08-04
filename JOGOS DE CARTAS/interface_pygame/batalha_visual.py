import pygame
import os
import sys
import json

# Caminhos e inicialização
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cartas.card_repository import get_carta_by_id
from batalha.jogador import Jogador
from herois.gerenciador_heroi import carregar_heroi

pygame.init()

# Configurações de tela
LARGURA_TELA, ALTURA_TELA = 1280, 720
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Batalha - Modo Pygame")
FONTE = pygame.font.SysFont("arial", 24)

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (50, 50, 50)
VERDE = (0, 200, 0)
AZUL = (0, 150, 255)
VERMELHO = (200, 0, 0)

# Caminho das imagens
CAMINHO_IMAGENS = os.path.join("interface_pygame", "assets", "cartas")


# Função para carregar imagens das cartas
def carregar_imagem(nome_carta):
    nome_arquivo = nome_carta.lower().replace(" ", "_").replace("ã", "a").replace("ç", "c").replace("é", "e").replace("ô", "o").replace("á", "a").replace("í", "i").replace("ó", "o").replace("ú", "u")
    caminho = os.path.join(CAMINHO_IMAGENS, f"{nome_arquivo}.png")
    if os.path.exists(caminho):
        return pygame.transform.scale(pygame.image.load(caminho), (120, 180))
    return None

# Exibe as cartas da mão
def mostrar_mao(jogador):
    x_inicial = 50
    y = ALTURA_TELA - 200
    espacamento = 130
    for i, carta in enumerate(jogador.mao):
        imagem = carregar_imagem(carta.nome)
        if imagem:
            TELA.blit(imagem, (x_inicial + i * espacamento, y))
            texto = FONTE.render(carta.nome, True, BRANCO)
            TELA.blit(texto, (x_inicial + i * espacamento, y + 185))


# Exibe informações básicas dos heróis
def mostrar_status_herois(jogador, inimigo):
    pygame.draw.rect(TELA, CINZA, (0, 0, LARGURA_TELA, 50))
    texto_jogador = FONTE.render(f"{jogador.nome} | Vida: {jogador.vida} | Mana: {jogador.mana}", True, BRANCO)
    texto_inimigo = FONTE.render(f"{inimigo.nome} | Vida: {inimigo.vida} | Mana: {inimigo.mana}", True, BRANCO)
    TELA.blit(texto_jogador, (20, 10))
    TELA.blit(texto_inimigo, (800, 10))


def main():
    clock = pygame.time.Clock()
    rodando = True

    # Jogador e inimigo fictícios para teste
    heroi = carregar_heroi("Thorin")  # você pode trocar pelo nome de qualquer herói existente
    jogador = Jogador(heroi)
    inimigo = Jogador(carregar_heroi("Inimigo_Teste"))

    # Compra de cartas inicial
    for _ in range(5):
        jogador.comprar_carta()

    while rodando:
        TELA.fill((30, 30, 30))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        mostrar_status_herois(jogador, inimigo)
        mostrar_mao(jogador)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
