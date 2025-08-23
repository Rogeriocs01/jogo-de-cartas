# interface_pygame/deck_builder_pygame.py

import pygame
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cartas.card_repository import card_repository
from interface_pygame.carta_visual import (
    desenhar_carta,
    desenhar_carta_zoom
)

pygame.init()

CAMINHO_IMAGENS = os.path.join("interface_pygame", "assets", "cartas")
CAMINHO_MOLDURAS = os.path.join("interface_pygame", "assets", "molduras")
CAMINHO_TERRRENOS = os.path.join("interface_pygame", "assets", "molduras", "terrenos")
CAMINHO_DADOS_HEROIS = os.path.join("dados", "herois")
CAMINHO_DECKS = "dados"
CAMINHO_INVENTARIO = os.path.join("interface_pygame", "inventario.json")

CARD_WIDTH = 100
CARD_HEIGHT = 140
CARD_MARGIN = 15

fonte = pygame.font.SysFont("arial", 22)


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
            cartas_para_exibir.append({
                "id": carta_id,
                "dados": dados,
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
            rect = desenhar_carta(screen, carta["dados"], x, y, CARD_WIDTH, CARD_HEIGHT)

            qtd_no_deck = deck.count(carta["id"])
            texto_qtd = fonte.render(f"({qtd_no_deck}/{carta['quantidade']})", True, (255, 255, 255))
            screen.blit(texto_qtd, (x, y + CARD_HEIGHT + 5))
            carta["rect"] = rect

            x += CARD_WIDTH + CARD_MARGIN
            if x + CARD_WIDTH > screen.get_width():
                x = 20
                y += CARD_HEIGHT + 50

        texto_deck = fonte.render(f"Deck: {len(deck)} / {limite_cartas}", True, (255, 255, 0))
        screen.blit(texto_deck, (20, screen.get_height() - 40))

        botao_salvar = pygame.Rect(screen.get_width() - 150, screen.get_height() - 50, 130, 40)
        pygame.draw.rect(screen, (0, 200, 0), botao_salvar)
        txt_salvar = fonte.render("Salvar Deck", True, (0, 0, 0))
        screen.blit(txt_salvar, (botao_salvar.x + 10, botao_salvar.y + 8))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                selecionando = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if evento.button == 1:  # clique esquerdo -> adicionar ao deck
                    for carta in cartas_para_exibir:
                        if carta["rect"].collidepoint(pos):
                            qtd_atual = deck.count(carta["id"])
                            if qtd_atual < carta["quantidade"] and len(deck) < limite_cartas:
                                deck.append(carta["id"])

                    if botao_salvar.collidepoint(pos):
                        salvar_deck(nome_heroi, deck)
                        print(f"✅ Deck salvo para {nome_heroi} com {len(deck)} cartas.")
                        selecionando = False

                elif evento.button == 3:  # clique direito -> zoom da carta
                    for carta in cartas_para_exibir:
                        if carta["rect"].collidepoint(pos):
                            desenhar_carta_zoom(screen, carta["dados"])

    return
