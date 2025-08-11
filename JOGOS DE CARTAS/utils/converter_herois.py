from PIL import Image
import os

# Pasta com as imagens originais
pasta_entrada = "interface_pygame/assets/herois"
# Pasta onde salvará as imagens convertidas
pasta_saida = "interface_pygame/assets/herois_webp"

ALTURA_DESEJADA = 512
QUALIDADE = 80

os.makedirs(pasta_saida, exist_ok=True)

for arquivo in os.listdir(pasta_entrada):
    if arquivo.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        caminho_entrada = os.path.join(pasta_entrada, arquivo)
        
        img = Image.open(caminho_entrada).convert("RGBA")
        
        largura_original, altura_original = img.size
        proporcao = largura_original / altura_original
        nova_largura = int(ALTURA_DESEJADA * proporcao)
        
        img_redimensionada = img.resize((nova_largura, ALTURA_DESEJADA), Image.Resampling.LANCZOS)
        
        nome_base = os.path.splitext(arquivo)[0]
        caminho_saida = os.path.join(pasta_saida, f"{nome_base}.webp")
        
        img_redimensionada.save(caminho_saida, "WEBP", quality=QUALIDADE)

        print(f"✅ Convertido: {arquivo} → {caminho_saida}")

print("\n🎯 Conversão de HERÓIS finalizada!")
