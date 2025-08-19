# converter_molduras_webp.py
import os
from PIL import Image
import shutil

# Caminho das molduras
PASTA_MOLDURAS = os.path.join("interface_pygame", "assets", "molduras")
PASTA_PNG = os.path.join(PASTA_MOLDURAS, "png")

# Cria subpasta png/ se não existir
os.makedirs(PASTA_PNG, exist_ok=True)

# Lista de arquivos PNG na pasta principal
arquivos_png = [f for f in os.listdir(PASTA_MOLDURAS) if f.lower().endswith(".png")]

for arquivo in arquivos_png:
    caminho_origem = os.path.join(PASTA_MOLDURAS, arquivo)
    caminho_destino_png = os.path.join(PASTA_PNG, arquivo)

    # Move o PNG para a subpasta
    shutil.move(caminho_origem, caminho_destino_png)
    print(f"✅ Movido {arquivo} para png/")

    # Abre o PNG e converte para WebP
    with Image.open(caminho_destino_png) as img:
        caminho_webp = os.path.join(PASTA_MOLDURAS, arquivo.replace(".png", ".webp"))
        img.save(caminho_webp, "WEBP", quality=80)
        print(f"✅ Convertido {arquivo} → {arquivo.replace('.png', '.webp')}")
