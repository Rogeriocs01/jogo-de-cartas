# interface_pygame/gerar_carta/utils.py
import os
from PIL import ImageFont, ImageDraw

def carregar_fonte(fontes_dir, nome_arquivo=None, tamanho=24):
    """
    Tenta carregar uma fonte da pasta fontes/. Se não encontrar, usa a default.
    """
    if nome_arquivo:
        caminho = os.path.join(fontes_dir, nome_arquivo)
        if os.path.exists(caminho):
            try:
                return ImageFont.truetype(caminho, tamanho)
            except Exception:
                pass
    # tenta heurísticas comuns
    for candidate in ("arial.ttf", "Arial.ttf", "DejaVuSans.ttf"):
        cand = os.path.join(fontes_dir, candidate)
        if os.path.exists(cand):
            try:
                return ImageFont.truetype(cand, tamanho)
            except Exception:
                continue
    # fallback
    return ImageFont.load_default()

def desenhar_texto_com_contorno(draw: ImageDraw.ImageDraw, xy, texto, fonte, fill=(255,255,255,255), contorno=(0,0,0,255), largura=2):
    x, y = xy
    # contorno
    for dx in (-largura, 0, largura):
        for dy in (-largura, 0, largura):
            if dx == 0 and dy == 0:
                continue
            draw.text((x+dx, y+dy), texto, font=fonte, fill=contorno)
    # texto principal
    draw.text((x, y), texto, font=fonte, fill=fill)

def quebrar_texto_por_largura(draw: ImageDraw.ImageDraw, texto, fonte, largura_max):
    palavras = texto.split()
    linhas, atual = [], ""
    for p in palavras:
        tentativa = (atual + " " + p).strip()
        w, _ = draw.textsize(tentativa, font=fonte)
        if w <= largura_max:
            atual = tentativa
        else:
            if atual:
                linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas
