import pygame
import os
import sys
import json

# Adiciona o diretório raiz ao sys.path antes de qualquer importação de módulos do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cartas.card_repository import get_carta_by_id, get_carta_by_nome

CAMINHO_JSON = os.path.join(os.path.dirname(__file__), "jogador", "inventario.json")

try:
    with open(CAMINHO_JSON, "r") as f:
        inventario = json.load(f)
except FileNotFoundError:
    print("Arquivo inventario.json não encontrado.")
    inventario = {}



# Inicializa o Pygame
pygame.init()

# Configurações da janela
LARGURA_TELA = 1000
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Visualizar Cartas do Inventário")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Fonte
fonte = pygame.font.SysFont(None, 24)

# Caminho das imagens
CAMINHO_IMAGENS = "imagens"

def carregar_imagem_carta(nome_carta):
    """Carrega a imagem da carta com base no nome do arquivo."""
    nome_arquivo = f"{nome_carta}.png"
    caminho_completo = os.path.join(CAMINHO_IMAGENS, nome_arquivo)
    if os.path.exists(caminho_completo):
        return pygame.image.load(caminho_completo)
    print(f"Imagem não encontrada: {nome_arquivo}")
    return None

def carregar_inventario():
    """Carrega o inventário do arquivo JSON."""
    try:
        with open("inventario.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo inventario.json não encontrado.")
        return {}

def preparar_cartas():
    """Prepara a lista de cartas com imagens com base no inventário."""
    inventario = carregar_inventario()
    cartas = []

    for carta_id, quantidade in inventario.items():
        dados_carta = get_carta_by_id(carta_id)
        if dados_carta:
            imagem = carregar_imagem_carta(dados_carta["nome"])
            if imagem:
                for _ in range(quantidade):
                    cartas.append((imagem, dados_carta["nome"]))
            else:
                print(f"Imagem não encontrada para {dados_carta['nome']}")
        else:
            print(f"Carta não encontrada no repositório: {carta_id}")

    return cartas

def main():
    cartas = preparar_cartas()
    cartas_por_linha = 5
    espacamento = 20
    largura_carta = 150
    altura_carta = 220

    clock = pygame.time.Clock()
    executando = True

    while executando:
        tela.fill(BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        # Exibe as cartas em grade
        for i, (imagem_carta, nome_carta) in enumerate(cartas):
            linha = i // cartas_por_linha
            coluna = i % cartas_por_linha
            x = espacamento + coluna * (largura_carta + espacamento)
            y = espacamento + linha * (altura_carta + espacamento)

            carta_redimensionada = pygame.transform.scale(imagem_carta, (largura_carta, altura_carta))
            tela.blit(carta_redimensionada, (x, y))

            # Desenhar o nome da carta abaixo da imagem
            texto = fonte.render(nome_carta, True, PRETO)
            texto_rect = texto.get_rect(center=(x + largura_carta // 2, y + altura_carta + 10))
            tela.blit(texto, texto_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
