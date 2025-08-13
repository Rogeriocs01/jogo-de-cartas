import os
from cartas.card_repository import card_repository, _slugify

# Pasta onde estão as imagens das cartas
PASTA_IMAGENS = os.path.join(os.path.dirname(__file__), "imagens", "cartas")

def verificar_imagens():
    total = len(card_repository)
    faltando = []
    ok = 0

    for cid, data in card_repository.items():
        slug = data.get("arquivo") or _slugify(data["nome"])
        caminho = os.path.join(PASTA_IMAGENS, f"{slug}.webp")
        
        if os.path.exists(caminho):
            ok += 1
        else:
            faltando.append((cid, data["nome"], f"{slug}.webp"))

    print(f"✅ Imagens encontradas: {ok}/{total}")
    if faltando:
        print("\n❌ Imagens faltando:")
        for cid, nome, arquivo in faltando:
            print(f"- {cid} | {nome} | arquivo esperado: {arquivo}")

if __name__ == "__main__":
    verificar_imagens()
