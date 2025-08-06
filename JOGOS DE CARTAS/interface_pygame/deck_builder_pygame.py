import pygame
import json
import os
pygame.init()
CAMINHO_IMAGENS = os.path.join("interface_pygame", "assets", "cartas")
CAMINHO_DADOS_HEROIS = os.path.join("dados", "herois")
CAMINHO_DECKS = "dados"
CAMINHO_INVENTARIO = os.path.join("interface_pygame", "inventario.json")

CARD_WIDTH = 100
CARD_HEIGHT = 140
CARD_MARGIN = 15

fonte = pygame.font.SysFont("arial", 22)


def carregar_imagem(nome_arquivo):
    caminho = os.path.join(CAMINHO_IMAGENS, f"{nome_arquivo}.png")
    if not os.path.exists(caminho):
        print(f"[ERRO] Imagem não encontrada: {caminho}")
        return None
    return pygame.transform.scale(pygame.image.load(caminho), (CARD_WIDTH, CARD_HEIGHT))


def carregar_inventario():
    with open(CAMINHO_INVENTARIO, "r", encoding="utf-8") as f:
        return json.load(f)


def carregar_nivel_heroi(nome_heroi):
    caminho = os.path.join(CAMINHO_DADOS_HEROIS, f"{nome_heroi}.json")
    if not os.path.exists(caminho):
        return 1  # padrão caso herói não exista ainda
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
        return dados.get("nivel", 1)


def salvar_deck(nome_heroi, deck):
    caminho = os.path.join(CAMINHO_DECKS, f"deck_{nome_heroi}.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(deck, f, indent=4, ensure_ascii=False)


def abrir_deckbuilder_pygame(screen, nome_heroi):
    inventario = carregar_inventario()
    nivel_heroi = carregar_nivel_heroi(nome_heroi)
    limite_cartas = 10 + nivel_heroi * 2

    deck = []  # lista de nomes

    cartas = []
    for nome, qtd in inventario.items():
        nome_formatado = nome.replace(" ", "_").replace("ã", "a").replace("ç", "c").replace("é", "e").replace("ê", "e").replace("á", "a").replace("ó", "o").replace("ô", "o").replace("í", "i").replace("ú", "u").replace("â", "a").replace("õ", "o")
        imagem = carregar_imagem(nome_formatado)
        if imagem:
            cartas.append({"nome": nome, "imagem": imagem, "quantidade": qtd})

    clock = pygame.time.Clock()
    selecionando = True

    while selecionando:
        screen.fill((15, 15, 15))

        y = 20
        x = 20

        for carta in cartas:
            screen.blit(carta["imagem"], (x, y))
            qtd_no_deck = deck.count(carta["nome"])
            texto = fonte.render(f"{carta['nome']} ({qtd_no_deck}/{carta['quantidade']})", True, (255, 255, 255))
            screen.blit(texto, (x, y + CARD_HEIGHT + 5))

            carta["rect"] = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

            x += CARD_WIDTH + CARD_MARGIN
            if x + CARD_WIDTH > screen.get_width():
                x = 20
                y += CARD_HEIGHT + 50

        # Mostrar status
        texto_deck = fonte.render(f"Deck: {len(deck)} / {limite_cartas}", True, (255, 255, 0))
        screen.blit(texto_deck, (20, screen.get_height() - 40))

        # Botão salvar
        botao_salvar = pygame.Rect(screen.get_width() - 150, screen.get_height() - 50, 130, 40)
        pygame.draw.rect(screen, (0, 200, 0), botao_salvar)
        txt_salvar = fonte.render("Salvar Deck", True, (0, 0, 0))
        screen.blit(txt_salvar, (botao_salvar.x + 10, botao_salvar.y + 8))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                selecionando = False

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = pygame.mouse.get_pos()

                # Clique nas cartas
                for carta in cartas:
                    if carta["rect"].collidepoint(pos):
                        qtd_atual = deck.count(carta["nome"])
                        if qtd_atual < carta["quantidade"] and len(deck) < limite_cartas:
                            deck.append(carta["nome"])

                # Clique em salvar
                if botao_salvar.collidepoint(pos):
                    salvar_deck(nome_heroi, deck)
                    print(f"✅ Deck salvo para {nome_heroi} com {len(deck)} cartas.")
                    selecionando = False

    return
