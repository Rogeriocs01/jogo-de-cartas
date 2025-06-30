# executar_habilidade.py

def habilidade_cura_jogador(jogador, quantidade=2):
    jogador.vida += quantidade
    print(f"✨ {jogador.nome} recupera {quantidade} de vida! Vida atual: {jogador.vida}")

def habilidade_dano_direto(inimigo, quantidade=2):
    inimigo.vida -= quantidade
    print(f"🔥 O jogador {inimigo.nome} recebeu {quantidade} de dano direto! Vida restante: {inimigo.vida}")

def habilidade_buff_aliado(carta, quantidade=1):
    carta.ataque += quantidade
    print(f"💪 {carta.nome} recebe +{quantidade} de ATK temporariamente! Novo ATK: {carta.ataque}")

# Mapeia IDs de cartas às funções de execução
habilidades_implementadas = {
    "Carta_2": lambda carta, jogador, inimigo: habilidade_cura_jogador(jogador, 2),  # Regenerar
    "Carta_4": lambda carta, jogador, inimigo: habilidade_dano_direto(inimigo, 2),   # Explosão
    "Carta_1": lambda carta, jogador, inimigo: habilidade_buff_aliado(carta, 1),     # Investida
}

def executar_habilidade(carta_id, carta_obj, jogador, inimigo):
    """
    Executa a habilidade da carta com base no seu ID.
    """
    funcao = habilidades_implementadas.get(carta_id)
    if funcao:
        print(f"\n🔮 Ativando habilidade de {carta_obj.nome}: {carta_obj.habilidade}")
        funcao(carta_obj, jogador, inimigo)
    else:
        print(f"\n⚠️ A carta {carta_obj.nome} ainda não tem habilidade implementada.")
