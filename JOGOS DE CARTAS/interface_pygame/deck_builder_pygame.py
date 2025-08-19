# interface_pygame/deck_builder_pygame.py

import pygame
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cartas.card_repository import card_repository

pygame.init()

CAMINHO_IMAGENS = os.path.join("interface_pygame", "assets", "cartas")
CAMINHO_MOLDURAS = os.path.join("interface_pygame", "assets", "molduras")
CAMINHO_DADOS_HEROIS = os.path.join("dados", "herois")
CAMINHO_DECKS = "dados"
CAMINHO_INVENTARIO = os.path.join("interface_pygame", "inventario.json")

CARD_WIDTH = 100
CARD_HEIGHT = 140
CARD_MARGIN = 15

fonte_nome = pygame.font.SysFont("arial", 18)
fonte_atrib = pygame.font.SysFont("arial", 16)

def carregar_imagem(nome_arquivo):
    caminho = os.path.join(CAMINHO_IMAGENS, nome_arquivo)
    if os.path.exists(caminho):
        return pygame.transform.scale(pygame.image.load(caminho), (CARD_WIDTH, CARD_HEIGHT))
    else:
        print(f"⚠️ Imagem não encontrada: {caminho}")
        imagem = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        imagem.fill((60, 60, 60))
        texto = fonte_nome.render("Sem Img", True, (255, 255, 255))
        imagem.blit(texto, (5, 60))
        return imagem

def carregar_moldura(raridade):
    nome_arquivo = f"{raridade.lower()}.webp"  # comum.webp, incomum.webp, raro.webp
    caminho = os.path.join(CAMINHO_MOLDURAS, nome_arquivo)
    if os.path.exists(caminho):
        return pygame.transform.scale(pygame.image.load(caminho), (CARD_WIDTH, CARD_HEIGHT))
    else:
        print(f"⚠️ Moldura não encontrada: {caminho}")
        s = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
        s.fill((200, 200, 200, 100))
        return s

def carregar_inventario():
    with open(CAMINHO_INVENTARIO, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_nivel_heroi(nome_heroi):
    caminho = os.path.join(CAMINHO_DADOS_HEROIS, f"{nome_heroi}.json")
    if not os.path.exists(caminho):
        return 1
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

    deck = []

    cartas_para_exibir = []
    for carta_id, qtd in inventario.items():
        if carta_id in card_repository:
            dados = card_repository[carta_id]
            arte = carregar_imagem(dados["arquivo"])
            moldura = carregar_moldura(dados.get("raridade", "comum"))
            cartas_para_exibir.append({
                "id": carta_id,
                "nome": dados["nome"],
                "arte": arte,
                "moldura": moldura,
                "atk": dados.get("atk", 0),
                "def": dados.get("def", 0),
                "mana": dados.get("mana", 0),
                "quantidade": qtd
            })
        else:
            print(f"⚠️ Carta {carta_id} não encontrada no card_repository.")

    clock = pygame.time.Clock()
    selecionando = True

    while selecionando:
        screen.fill((15, 15, 15))
        y = 20
        x = 20

        for carta in cartas_para_exibir:
            # Criar superfície final da carta
            carta_surf = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
            carta_surf.blit(carta["arte"], (0, 0))
            carta_surf.blit(carta["moldura"], (0, 0))

            # Desenhar atributos
            texto_nome = fonte_nome.render(carta["nome"], True, (255, 255, 255))
            carta_surf.blit(texto_nome, (5, 5))
            texto_atk = fonte_atrib.render(f"ATK: {carta['atk']}", True, (255, 0, 0))
            carta_surf.blit(texto_atk, (5, CARD_HEIGHT - 50))
            texto_def = fonte_atrib.render(f"DEF: {carta['def']}", True, (0, 0, 255))
            carta_surf.blit(texto_def, (CARD_WIDTH - 50, CARD_HEIGHT - 50))
            texto_mana = fonte_atrib.render(f"Mana: {carta['mana']}", True, (0, 255, 255))
            carta_surf.blit(texto_mana, (5, CARD_HEIGHT - 30))

            screen.blit(carta_surf, (x, y))

            qtd_no_deck = deck.count(carta["id"])
            texto_qtd = fonte_nome.render(f"({qtd_no_deck}/{carta['quantidade']})", True, (255, 255, 255))
            screen.blit(texto_qtd, (x, y + CARD_HEIGHT + 5))
            carta["rect"] = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

            x += CARD_WIDTH + CARD_MARGIN
            if x + CARD_WIDTH > screen.get_width():
                x = 20
                y += CARD_HEIGHT + 50

        texto_deck = fonte_nome.render(f"Deck: {len(deck)} / {limite_cartas}", True, (255, 255, 0))
        screen.blit(texto_deck, (20, screen.get_height() - 40))

        botao_salvar = pygame.Rect(screen.get_width() - 150, screen.get_height() - 50, 130, 40)
        pygame.draw.rect(screen, (0, 200, 0), botao_salvar)
        txt_salvar = fonte_nome.render("Salvar Deck", True, (0, 0, 0))
        screen.blit(txt_salvar, (botao_salvar.x + 10, botao_salvar.y + 8))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                selecionando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = pygame.mouse.get_pos()
                for carta in cartas_para_exibir:
                    if carta["rect"].collidepoint(pos):
                        qtd_atual = deck.count(carta["id"])
                        if qtd_atual < carta["quantidade"] and len(deck) < limite_cartas:
                            deck.append(carta["id"])
                if botao_salvar.collidepoint(pos):
                    salvar_deck(nome_heroi, deck)
                    print(f"✅ Deck salvo para {nome_heroi} com {len(deck)} cartas.")
                    selecionando = False

    return
