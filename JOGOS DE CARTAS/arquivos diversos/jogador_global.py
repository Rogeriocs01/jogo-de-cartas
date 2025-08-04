#jogador_global

import json
import os

CAMINHO_ARQUIVO = "jogador.json"

# 🔁 Carrega os dados existentes ou cria padrão
def carregar_jogador():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        dados = {
            "nome": "Jogador1",
            "moedas": 0
        }
        salvar_jogador(dados)
        return dados

# 💾 Salva os dados no arquivo
def salvar_jogador(dados):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

# 💰 Retorna o total de moedas
def get_moedas():
    jogador = carregar_jogador()
    return jogador.get("moedas", 0)

# ➕ Adiciona moedas ao jogador
def adicionar_moedas(qtd):
    jogador = carregar_jogador()
    jogador["moedas"] = jogador.get("moedas", 0) + qtd
    salvar_jogador(jogador)

# ➖ Remove moedas (retorna True se conseguir, False se não tiver saldo)
def remover_moedas(qtd):
    jogador = carregar_jogador()
    if jogador.get("moedas", 0) >= qtd:
        jogador["moedas"] -= qtd
        salvar_jogador(jogador)
        return True
    else:
        return False

# 🧾 Mostra status atual (debug ou info)
def exibir_status_jogador():
    jogador = carregar_jogador()
    print(f"\n🎮 Jogador: {jogador.get('nome', 'Desconhecido')}")
    print(f"💰 Moedas: {jogador.get('moedas', 0)}")
