# comuns.py

def curar_jogador(jogador, quantidade=2):
    jogador.vida += quantidade
    print(f"✨ {jogador.nome} recupera {quantidade} de vida! Vida atual: {jogador.vida}")

def dano_direto(inimigo, quantidade=2):
    inimigo.vida -= quantidade
    print(f"🔥 {inimigo.nome} recebeu {quantidade} de dano direto! Vida restante: {inimigo.vida}")

def buff_ataque_temporario(carta, quantidade=1):
    carta.ataque += quantidade
    print(f"💪 {carta.nome} recebe +{quantidade} de ATK temporariamente! Novo ATK: {carta.ataque}")

def curar_aliado(jogador, quantidade=2):
    for carta in jogador.campo:
        if carta and carta.defesa < 10:  # limite arbitrário, pode ser ajustado
            carta.defesa += quantidade
            print(f"🩹 {carta.nome} foi curada em {quantidade}. Nova DEF: {carta.defesa}")
            break

def dano_em_area(inimigo, quantidade=1):
    print("💥 Erupção! Todas as cartas inimigas sofrem dano.")
    for carta in inimigo.campo:
        if carta:
            carta.defesa -= quantidade
            print(f"⚡ {carta.nome} perdeu {quantidade} de DEF (agora {carta.defesa})")
            if carta.defesa <= 0:
                print(f"☠️ {carta.nome} foi destruída!")
                index = inimigo.campo.index(carta)
                inimigo.campo[index] = None

def buff_floresta(jogador, quantidade=1):
    print("🌲 Ira Selvagem: todas as cartas do tipo 'Floresta' ganham +1 ATK.")
    for carta in jogador.campo:
        if carta and carta.tipo_terreno.lower() == "floresta":
            carta.ataque += quantidade
            print(f"🌿 {carta.nome} recebeu +{quantidade} ATK! Novo ATK: {carta.ataque}")