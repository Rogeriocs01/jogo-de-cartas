# interface_terminal.py

def exibir_campo(jogador, inimigo):
    def formatar_carta(carta):
        if not carta:
            return ["(vazio)", "", ""]
        return [
            f"{carta.nome[:14]:14}",
            f"ATK: {carta.ataque:<3}",
            f"DEF: {carta.defesa:<3}"
        ]

    print("\n" + "═" * 60)
    print(f"🤖 {inimigo.nome:20}  ❤️ {inimigo.vida:<2}  🔷 Mana: {inimigo.mana:<2}  🗺️ Terreno: {inimigo.terreno_favorito}")

    for linha in range(3):
        linha_texto = ""
        for carta in inimigo.campo:
            partes = formatar_carta(carta)
            linha_texto += f"│ {partes[linha]:14} "
        print(linha_texto + "│")

    print("─" * 60)
    print(f"👤 {jogador.nome:20}  ❤️ {jogador.vida:<2}  🔷 Mana: {jogador.mana:<2}  🗺️ Terreno: {jogador.terreno_favorito}")

    for linha in range(3):
        linha_texto = ""
        for carta in jogador.campo:
            partes = formatar_carta(carta)
            linha_texto += f"│ {partes[linha]:14} "
        print(linha_texto + "│")
    print("═" * 60)
