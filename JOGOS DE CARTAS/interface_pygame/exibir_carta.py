# interface_pygame/exibir_carta.py
import pygame
import os
import sys

# Inicialização
pygame.init()
largura, altura = 400, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Visualização da Carta")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
DOURADO = (218, 165, 32)
AZUL = (30, 144, 255)

# Fonte
fonte_grande = pygame.font.SysFont("arial", 32)
fonte_pequena = pygame.font.SysFont("arial", 24)

# Dados da carta de exemplo (você pode automatizar depois com card_repository)
carta = {
    "nome": "Dragão de Lava",
    "tipo": "Lava",
    "raridade": "Raro",
    "ataque": 7,
    "defesa": 5,
    "mana": 6,
    "custo_habilidade": 3,
}

# Caminho da imagem
nome_arquivo = carta["nome"].lower().replace(" ", "_") + ".png"
caminho_imagem = os.path.join("interface_pygame", "assets", "cartas", nome_arquivo)

# Carrega imagem da carta
imagem_carta = pygame.image.load(caminho_imagem)
imagem_carta = pygame.transform.scale(imagem_carta, (300, 450))

def desenhar_carta():
    tela.fill(BRANCO)
    tela.blit(imagem_carta, (50, 50))

    # Sobreposição de texto (camadas)
    pygame.draw.rect(tela, PRETO, (50, 510, 300, 80))  # Fundo preto para atributos

    # Nome e raridade
    nome_texto = fonte_grande.render(carta["nome"], True, BRANCO)
    raridade_cor = DOURADO if carta["raridade"] == "Raro" else AZUL
    raridade_texto = fonte_pequena.render(carta["raridade"], True, raridade_cor)
    tela.blit(nome_texto, (60, 460))
    tela.blit(raridade_texto, (60, 495))

    # Atributos
    atributos = f"ATK: {carta['ataque']}  DEF: {carta['defesa']}  Mana: {carta['mana']}"
    atributos_texto = fonte_pequena.render(atributos, True, BRANCO)
    tela.blit(atributos_texto, (60, 520))

# Loop
def loop_visualizacao():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        desenhar_carta()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    loop_visualizacao()
