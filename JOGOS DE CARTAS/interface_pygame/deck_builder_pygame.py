# interface_pygame/deck_builder_pygame.py

import pygame
import json
import os
import sys
import unicodedata

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cartas.card_repository import card_repository

pygame.init()

# Caminhos
CAMINHO_IMAGENS = os.path.join("interface_pygame", "assets", "cartas")
CAMINHO_MOLDURAS = os.path.join("interface_pygame", "assets", "molduras")
CAMINHO_TERRENOS = os.path.join(CAMINHO_MOLDURAS, "terrenos")
CAMINHO_DADOS_HEROIS = os.path.join("dados", "herois")
CAMINHO_DECKS = "dados"
CAMINHO_INVENTARIO = os.path.join("interface_pygame", "inventario.json")

# Tamanho das miniaturas no Deck Builder
CARD_WIDTH = 100
CARD_HEIGHT = 140
CARD_MARGIN = 15

# ===== Ajustes globais (padrões) =====
FONTE_NOME_TAM_PADRAO = 18
FONTE_ATRIB_TAM_PADRAO = 16

POS_PADRAO = {
    "terreno_pos": (5, 5),        # canto superior esquerdo
    "terreno_tam": (24, 24),

    "nome_pos": (28, 5),          # ao lado do terreno
    "atk_pos": (CARD_WIDTH - 22, 5),              # canto sup. direito
    "def_pos": (CARD_WIDTH - 22, CARD_HEIGHT - 22),  # canto inf. direito
    "mana_pos": (5, CARD_HEIGHT - 22),            # canto inf. esquerdo
    "raridade_pos": (30, CARD_HEIGHT - 22),       # inferior centro-esq
}

# ===== Ajustes finos por carta (opcional) =====
# Edite aqui para mover/trocar tamanhos de uma carta específica
# Exemplo:
# "Carta_1": {"nome_pos": (32, 6), "atk_pos": (CARD_WIDTH - 24, 6), "fonte_atrib_tam": 17}
AJUSTES_POR_CARTA = {
    # "Carta_1": {"nome_pos": (32, 6), "atk_pos": (CARD_WIDTH - 24, 6), "fonte_atrib_tam": 17}
}

# ===== Normalização / mapeamentos =====
def normalizar_token(s: str) -> str:
    if not isinstance(s, str):
        return ""
    return unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode("ASCII").strip().lower()

# Mapeia valores variados de raridade -> arquivo da moldura
RARIDADE_MAP = {
    "comum": "comum.webp",
    "incomum": "incomum.webp",
    "raro": "raro.webp",
    "rara": "raro.webp",     # sinônimo comum
    "epico": "raro.webp",    # provisório até ter moldura própria
    "lendario": "raro.webp"  # provisório até ter moldura própria
}

# Mapeia 'tipo' -> nome do arquivo do terreno (sem extensão)
# Ajuste livremente conforme seu conjunto de terrenos
MAPA_TERRENO = {
    "fogo": "fogo",
    "lava": "fogo",
    "agua": "agua",
    "floresta": "floresta",
    "selva": "floresta",
    "montanha": "montanha",
    "rocha": "montanha",
    "pantano": "pantano",
    "luz": "luz",
    "sagrado": "luz",
    "sombras": "sombras",
    "trevas": "sombras"
}

# ===== Fontes (com re-criação por carta quando necessário) =====
def criar_fontes(fonte_nome_tam, fonte_atrib_tam):
    return (
        pygame.font.SysFont("arial", fonte_nome_tam),
        pygame.font.SysFont("arial", fonte_atrib_tam)
    )

# ===== Caches simples =====
_cache_arte = {}
_cache_moldura = {}
_cache_terreno = {}

def carregar_imagem_arte(nome_arquivo):
    if nome_arquivo in _cache_arte:
        return _cache_arte[nome_arquivo]
    caminho = os.path.join(CAMINHO_IMAGENS, nome_arquivo)
    if os.path.exists(caminho):
        img = pygame.transform.scale(pygame.image.load(caminho), (CARD_WIDTH, CARD_HEIGHT))
    else:
        print(f"⚠️ Imagem não encontrada: {caminho}")
        img = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        img.fill((60, 60, 60))
        fonte_tmp = pygame.font.SysFont("arial", 16)
        img.blit(fonte_tmp.render("Sem Img", True, (255, 255, 255)), (5, 60))
    _cache_arte[nome_arquivo] = img
    return img

def carregar_moldura(raridade):
    rar_norm = normalizar_token(raridade)
    arquivo = RARIDADE_MAP.get(rar_norm, "comum.webp")
    if arquivo in _cache_moldura:
        return _cache_moldura[arquivo]
    caminho = os.path.join(CAMINHO_MOLDURAS, arquivo)
    if os.path.exists(caminho):
        img = pygame.transform.scale(pygame.image.load(caminho), (CARD_WIDTH, CARD_HEIGHT))
    else:
        print(f"⚠️ Moldura não encontrada: {caminho}")
        img = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
        img.fill((200, 200, 200, 85))
    _cache_moldura[arquivo] = img
    return img

def carregar_terreno_por_tipo(tipo):
    tipo_norm = normalizar_token(tipo)
    chave = MAPA_TERRENO.get(tipo_norm, tipo_norm)  # se não estiver no mapa, tenta direto
    arquivo = f"{chave}.webp"
    if arquivo in _cache_terreno:
        return _cache_terreno[arquivo]
    caminho = os.path.join(CAMINHO_TERRENOS, arquivo)
    if os.path.exists(caminho):
        img = pygame.image.load(caminho)
    else:
        print(f"⚠️ Terreno não encontrado: {caminho}")
        _cache_terreno[arquivo] = None
        return None
    _cache_terreno[arquivo] = img
    return img

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

def _layout_para_carta(carta_id):
    """Mescla defaults com ajustes finos por carta."""
    ajustes = AJUSTES_POR_CARTA.get(carta_id, {})
    layout = POS_PADRAO.copy()
    layout.update(ajustes)
    fonte_nome_tam = ajustes.get("fonte_nome_tam", FONTE_NOME_TAM_PADRAO)
    fonte_atrib_tam = ajustes.get("fonte_atrib_tam", FONTE_ATRIB_TAM_PADRAO)
    return layout, fonte_nome_tam, fonte_atrib_tam

def abrir_deckbuilder_pygame(screen, nome_heroi):
    inventario = carregar_inventario()
    nivel_heroi = carregar_nivel_heroi(nome_heroi)
    limite_cartas = 10 + nivel_heroi * 2

    deck = []
    cartas_para_exibir = []

    # Monta lista de cartas a partir do repositório + inventário
    for carta_id, qtd in inventario.items():
        if carta_id not in card_repository:
            print(f"⚠️ Carta {carta_id} não encontrada no card_repository.")
            continue

        dados = card_repository[carta_id]
        arte = carregar_imagem_arte(dados["arquivo"])
        raridade = dados.get("raridade", "comum")
        moldura = carregar_moldura(raridade)

        # Usa campos em PT (ataque/defesa/mana); fallback para 'atk'/'def'
        ataque = dados.get("ataque", dados.get("atk", 0))
        defesa = dados.get("defesa", dados.get("def", 0))
        mana = dados.get("mana", 0)
        tipo = dados.get("tipo", "")  # terreno vem aqui

        terreno_img = None
        if tipo:
            terreno_img = carregar_terreno_por_tipo(tipo)

        cartas_para_exibir.append({
            "id": carta_id,
            "nome": dados["nome"],
            "arte": arte,
            "moldura": moldura,
            "ataque": ataque,
            "defesa": defesa,
            "mana": mana,
            "raridade": raridade,
            "terreno_img": terreno_img,
            "quantidade": qtd
        })

    clock = pygame.time.Clock()
    selecionando = True

    while selecionando:
        screen.fill((15, 15, 15))
        y = 20
        x = 20

        for carta in cartas_para_exibir:
            layout, fonte_nome_tam, fonte_atrib_tam = _layout_para_carta(carta["id"])
            fonte_nome, fonte_atrib = criar_fontes(fonte_nome_tam, fonte_atrib_tam)

            carta_surf = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
            carta_surf.blit(carta["arte"], (0, 0))
            carta_surf.blit(carta["moldura"], (0, 0))

            # Ícone do terreno (escala e posição ajustáveis)
            if carta["terreno_img"]:
                w, h = layout["terreno_tam"]
                icone = pygame.transform.smoothscale(carta["terreno_img"], (w, h))
                carta_surf.blit(icone, layout["terreno_pos"])

            # Nome
            texto_nome = fonte_nome.render(carta["nome"], True, (255, 255, 255))
            carta_surf.blit(texto_nome, layout["nome_pos"])

            # Atributos numéricos (números ao lado dos ícones já existentes na moldura)
            texto_atk = fonte_atrib.render(f"{carta['ataque']}", True, (255, 255, 255))
            carta_surf.blit(texto_atk, layout["atk_pos"])

            texto_def = fonte_atrib.render(f"{carta['defesa']}", True, (255, 255, 255))
            carta_surf.blit(texto_def, layout["def_pos"])

            texto_mana = fonte_atrib.render(f"{carta['mana']}", True, (255, 255, 255))
            carta_surf.blit(texto_mana, layout["mana_pos"])

            # Raridade (texto simples, já que a moldura é por raridade)
            rar_txt = str(carta["raridade"])
            texto_rar = fonte_atrib.render(rar_txt, True, (255, 215, 0))
            carta_surf.blit(texto_rar, layout["raridade_pos"])

            screen.blit(carta_surf, (x, y))

            qtd_no_deck = deck.count(carta["id"])
            texto_qtd = fonte_nome.render(f"({qtd_no_deck}/{carta['quantidade']})", True, (255, 255, 255))
            screen.blit(texto_qtd, (x, y + CARD_HEIGHT + 5))
            carta["rect"] = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

            x += CARD_WIDTH + CARD_MARGIN
            if x + CARD_WIDTH > screen.get_width():
                x = 20
                y += CARD_HEIGHT + 50

        texto_deck = pygame.font.SysFont("arial", 18).render(
            f"Deck: {len(deck)} / {limite_cartas}", True, (255, 255, 0)
        )
        screen.blit(texto_deck, (20, screen.get_height() - 40))

        botao_salvar = pygame.Rect(screen.get_width() - 150, screen.get_height() - 50, 130, 40)
        pygame.draw.rect(screen, (0, 200, 0), botao_salvar)
        txt_salvar = pygame.font.SysFont("arial", 18).render("Salvar Deck", True, (0, 0, 0))
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
