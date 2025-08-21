# interface_pygame/gerar_carta/conversor.py
import os
from PIL import Image
import shutil

# Caminhos base
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
INTERFACE_DIR = os.path.abspath(os.path.join(THIS_DIR, ".."))
ASSETS_DIR = os.path.join(INTERFACE_DIR, "assets")
TERRENOS_DIR = os.path.join(ASSETS_DIR, "molduras", "terrenos")
TERRENOS_PNG_DIR = os.path.join(TERRENOS_DIR, "png")

def converter_terrenos_png_para_webp(qualidade=80, mover_png=True):
    os.makedirs(TERRENOS_DIR, exist_ok=True)
    os.makedirs(TERRENOS_PNG_DIR, exist_ok=True)

    arquivos = [f for f in os.listdir(TERRENOS_DIR) if f.lower().endswith(".png")]
    if not arquivos:
        print("Nenhum .png direto em molduras/terrenos/ para converter (ok se já moveu antes).")
        return

    for nome in arquivos:
        origem = os.path.join(TERRENOS_DIR, nome)
        destino_webp = os.path.join(TERRENOS_DIR, os.path.splitext(nome)[0] + ".webp")

        with Image.open(origem).convert("RGBA") as img:
            img.save(destino_webp, "WEBP", quality=qualidade, method=6)
        print(f"✅ Convertido {nome} → {os.path.basename(destino_webp)}")

        if mover_png:
            shutil.move(origem, os.path.join(TERRENOS_PNG_DIR, nome))
            print(f"↪️  Movido PNG para {TERRENOS_PNG_DIR}")

if __name__ == "__main__":
    converter_terrenos_png_para_webp()
