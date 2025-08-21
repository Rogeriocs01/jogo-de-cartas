# interface_pygame/gerar_carta/gerar_carta.py
import os, sys, json, argparse
from PIL import Image, ImageDraw
from utils import carregar_fonte, desenhar_texto_com_contorno, quebrar_texto_por_largura

# === Caminhos base ===
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
INTERFACE_DIR = os.path.abspath(os.path.join(THIS_DIR, ".."))
ASSETS_DIR = os.path.join(INTERFACE_DIR, "assets")
FONTES_DIR = os.path.join(ASSETS_DIR, "fontes")
MOLDURAS_DIR = os.path.join(ASSETS_DIR, "molduras")
TERRENOS_DIR = os.path.join(MOLDURAS_DIR, "terrenos")
CARTAS_SAIDA = os.path.join(INTERFACE_DIR, "cartas")           # saída final .webp
CARTAS_ARTE = os.path.join(INTERFACE_DIR, "cartas")            # artes em .webp (já existentes)
CARTAS_ORIGINAIS = os.path.join(INTERFACE_DIR, "carta_originais")  # se quiser converter PNG → usar depois

# Importa card_repository se desejar usar --id
ROOT_DIR = os.path.abspath(os.path.join(INTERFACE_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)
try:
    from cartas.card_repository import card_repository
except Exception:
    card_repository = {}

def carregar_layout_config():
    cfg_path = os.path.join(THIS_DIR, "configs", "criaturas.json")
    with open(cfg_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def escolher_moldura_por_raridade(raridade: str):
    """
    Suporta molduras em: interface_pygame/assets/molduras/{comum,incomum,raro}.webp
    """
    r = (raridade or "comum").lower()
    nome = f"{r}.webp"  # comum.webp, incomum.webp, raro.webp
    caminho = os.path.join(MOLDURAS_DIR, nome)
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Moldura não encontrada: {caminho}")
    return caminho

def carregar_arte(arquivo_slug: str, altura_alvo: int):
    """
    Carrega a arte da carta (webp) e redimensiona proporcionalmente para a altura desejada.
    Espera arquivo em interface_pygame/cartas/{slug}.webp
    """
    caminho = os.path.join(CARTAS_ARTE, f"{arquivo_slug}.webp")
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arte não encontrada: {caminho}")
    img = Image.open(caminho).convert("RGBA")
    w, h = img.size
    if h != altura_alvo:
        nova_largura = int((altura_alvo / h) * w)
        img = img.resize((nova_largura, altura_alvo), Image.LANCZOS)
    return img

def carregar_terreno(terreno_slug: str, tamanho: tuple[int,int]):
    """
    Carrega o ícone de terreno em WEBP: interface_pygame/assets/molduras/terrenos/{slug}.webp
    Redimensiona para o tamanho especificado em config.
    """
    if not terreno_slug:
        return None
    caminho = os.path.join(TERRENOS_DIR, f"{terreno_slug}.webp")
    if not os.path.exists(caminho):
        print(f"⚠️ Terreno '{terreno_slug}' não encontrado em {caminho} (ignorando).")
        return None
    img = Image.open(caminho).convert("RGBA")
    return img.resize(tamanho, Image.LANCZOS)

def aplicar_layout(carta_img: Image.Image, moldura_img: Image.Image, terreno_img, layout: dict,
                   nome: str, atk: int, defe: int, mana: int, raridade: str, habilidade: str):
    """
    Compoe arte + moldura + terreno + textos.
    """
    # Basear tamanho final na moldura
    frame_w, frame_h = moldura_img.size
    # Se a arte não tiver mesma altura, centraliza no eixo X e recorta/extrapola
    base = Image.new("RGBA", (frame_w, frame_h), (0,0,0,0))

    # Centraliza arte na largura da moldura
    art_x = (frame_w - carta_img.size[0]) // 2
    base.paste(carta_img, (max(0, art_x), 0), carta_img)

    # Cola moldura por cima
    base.alpha_composite(moldura_img, (0, 0))

    draw = ImageDraw.Draw(base)
    dcfg = layout["default"]

    # fontes
    f_nome = carregar_fonte(FONTES_DIR, dcfg["fonte_nome"]["arquivo"], dcfg["fonte_nome"]["tamanho"])
    f_stats = carregar_fonte(FONTES_DIR, dcfg["fonte_stats"]["arquivo"], dcfg["fonte_stats"]["tamanho"])
    f_rar = carregar_fonte(FONTES_DIR, dcfg["fonte_raridade"]["arquivo"], dcfg["fonte_raridade"]["tamanho"])
    f_hab = carregar_fonte(FONTES_DIR, dcfg["fonte_habilidade"]["arquivo"], dcfg["fonte_habilidade"]["tamanho"])

    cor_texto = tuple(dcfg.get("cor_texto", [255,255,255,255]))
    cor_cont = tuple(dcfg.get("cor_contorno", [0,0,0,255]))
    contorno_px = int(dcfg.get("contorno_px", 2))

    # Terreno
    if terreno_img is not None:
        tx, ty = dcfg["pos_terreno"]
        base.alpha_composite(terreno_img, (tx, ty))

    # Nome (quebra se necessário)
    nx, ny = dcfg["pos_nome"]
    nome_larg = int(dcfg["largura_nome"])
    linhas = quebrar_texto_por_largura(draw, nome, f_nome, nome_larg)
    for i, linha in enumerate(linhas[:2]):  # 2 linhas no máximo
        desenhar_texto_com_contorno(draw, (nx, ny + i*(f_nome.size+2)), linha, f_nome, cor_texto, cor_cont, contorno_px)

    # Stats
    desenhar_texto_com_contorno(draw, tuple(dcfg["pos_atk"]), str(atk), f_stats, cor_texto, cor_cont, contorno_px)
    desenhar_texto_com_contorno(draw, tuple(dcfg["pos_def"]), str(defe), f_stats, cor_texto, cor_cont, contorno_px)
    desenhar_texto_com_contorno(draw, tuple(dcfg["pos_mana"]), str(mana), f_stats, cor_texto, cor_cont, contorno_px)

    # Raridade (texto curto, ex: Comum / Incomum / Raro)
    desenhar_texto_com_contorno(draw, tuple(dcfg["pos_raridade"]), str(raridade).title(), f_rar, cor_texto, cor_cont, contorno_px)

    # Habilidade (texto corrido)
    if habilidade:
        ax, ay, aw = dcfg["area_habilidade"]
        linhas = quebrar_texto_por_largura(draw, habilidade, f_hab, aw)
        for i, linha in enumerate(linhas[:4]):  # 4 linhas máx. por segurança
            desenhar_texto_com_contorno(draw, (ax, ay + i*(f_hab.size+2)), linha, f_hab, cor_texto, cor_cont, contorno_px)

    return base

def aplicar_overrides(layout_cfg: dict, carta_id: str):
    """Mescla overrides específicos da carta com o default."""
    d = json.loads(json.dumps(layout_cfg["default"]))  # deep copy simples
    ov = layout_cfg.get("overrides", {}).get(carta_id)
    if ov:
        for k, v in ov.items():
            d[k] = v
    return d

def gerar_para_card(id_carta=None, arquivo_slug=None, nome=None, raridade="comum",
                    atk=0, defe=0, mana=0, terreno=None, habilidade="",
                    saida_path=None):
    cfg = carregar_layout_config()
    altura = int(cfg.get("tamanho_saida", 512))

    # Resolve dados via card_repository se houver id_carta
    if id_carta and id_carta in card_repository:
        data = card_repository[id_carta]
        arquivo_slug = arquivo_slug or data.get("arquivo")
        nome = nome or data.get("nome", id_carta)
        raridade = (data.get("raridade") or raridade or "comum").lower()
        atk = data.get("atk", atk)
        defe = data.get("def", defe)
        mana = data.get("mana", mana)
        terreno = data.get("terreno", terreno)
        habilidade = data.get("habilidade_desc", habilidade or "")

    if not arquivo_slug:
        raise ValueError("É necessário informar 'arquivo' (slug da arte) ou fornecer um id_carta válido no card_repository.")

    # Carrega partes
    moldura_path = escolher_moldura_por_raridade(raridade)
    moldura_img = Image.open(moldura_path).convert("RGBA")
    # Ajusta base pela altura desejada
    if moldura_img.size[1] != altura:
        ratio = altura / moldura_img.size[1]
        moldura_img = moldura_img.resize((int(moldura_img.size[0]*ratio), altura), Image.LANCZOS)

    arte_img = carregar_arte(arquivo_slug, moldura_img.size[1])

    # Aplica overrides de layout por carta (se existir)
    layout_cfg = carregar_layout_config()
    layout_cfg["default"] = aplicar_overrides(layout_cfg, id_carta or "")

    terreno_tam = tuple(layout_cfg["default"]["tam_terreno"])
    terreno_img = carregar_terreno(terreno, terreno_tam) if terreno else None

    # Compor
    final_img = aplicar_layout(
        carta_img=arte_img, moldura_img=moldura_img, terreno_img=terreno_img,
        layout=layout_cfg, nome=nome, atk=atk, defe=defe, mana=mana,
        raridade=raridade, habilidade=habilidade
    )

    # Salvar
    os.makedirs(CARTAS_SAIDA, exist_ok=True)
    out_name = f"{arquivo_slug}_final.webp"
    destino = os.path.join(CARTAS_SAIDA, out_name) if not saida_path else saida_path
    final_img.save(destino, "WEBP", quality=80, method=6)
    print(f"✅ Carta gerada: {destino}")

def main():
    ap = argparse.ArgumentParser(description="Gerar carta de batalha com moldura, terreno e atributos.")
    ap.add_argument("--id", dest="id_carta", help="ID da carta no card_repository (ex: Carta_7)")
    ap.add_argument("--arquivo", dest="arquivo_slug", help="slug da arte (ex: dragao_de_lava)")
    ap.add_argument("--nome")
    ap.add_argument("--raridade", default="comum", choices=["comum","incomum","raro","épico","epico","lendario","lendário"])
    ap.add_argument("--atk", type=int, default=0)
    ap.add_argument("--defe", type=int, default=0)
    ap.add_argument("--mana", type=int, default=0)
    ap.add_argument("--terreno", help="slug do terreno (arquivo em assets/molduras/terrenos/<slug>.webp)")
    ap.add_argument("--habilidade", default="", help="texto da habilidade para exibir")
    ap.add_argument("--saida", help="caminho de saída opcional .webp")

    args = ap.parse_args()
    gerar_para_card(
        id_carta=args.id_carta,
        arquivo_slug=args.arquivo_slug,
        nome=args.nome,
        raridade=args.raridade,
        atk=args.atk,
        defe=args.defe,
        mana=args.mana,
        terreno=args.terreno,
        habilidade=args.habilidade,
        saida_path=args.saida
    )

if __name__ == "__main__":
    main()
