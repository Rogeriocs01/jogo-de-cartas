# Define o nível de poder das cartas baseado no ID

def obter_nivel_da_carta(carta_id):
    id_num = int(carta_id.replace("Carta_", ""))

    if 1 <= id_num <= 20:
        return "Básica"
    elif 21 <= id_num <= 40:
        return "Média"
    elif 41 <= id_num <= 60:
        return "Forte"
    elif 61 <= id_num <= 80:
        return "Muito Forte"
    else:
        return "Desconhecida"
