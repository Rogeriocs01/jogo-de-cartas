# 🃏 Jogo de Cartas PvE com Campanha e Heróis

Projeto em Python de um jogo de cartas tático com foco em batalhas PvE, progressão de heróis, habilidades, e futuramente uma interface gráfica com Pygame.

---

## 🗂️ Estrutura do Projeto

📁 batalha/ ← Lógica de batalha entre jogador e inimigo
│ ├── motor.py ← Loop principal da batalha (turnos e vitória)
│ ├── turno_jogador.py ← Ações e opções do jogador
│ ├── turno_inimigo.py ← IA do inimigo
│ ├── habilidade_cartas.py ← Ativação das habilidades das cartas
│ └── habilidade_heroi.py ← Ativação da habilidade especial do herói

📁 campanha/ ← Gerenciamento da campanha e progressão
│ ├── controlador.py ← Executa as fases da campanha
│ ├── fases.py ← Define dados de cada fase
│ ├── inimigos.py ← Dados dos inimigos por nome
│ ├── progresso.py ← Salvamento do progresso da campanha
│ └── drops_personagens.py ← Drop aleatório de cartas por inimigo

📁 dados/ ← Salvamento e exibição de dados
│ ├── save.py ← Funções de salvar e carregar progresso (JSON)
│ └── status_heroi.py ← Exibe informações do herói atual

📁 habilidades/ ← Definição de efeitos das habilidades
│ ├── comuns.py ← Habilidades genéricas (cura, dano, etc)
│ ├── executores.py ← Mapeia efeitos por carta
│ └── habilidades_heroi.py ← Define as habilidades especiais dos heróis

📁 raiz do projeto
├── main_pygame.py ← Interface visual (início da versão com Pygame)
├── menu_inicial.py ← Menu principal (inicia campanha, exibe status)
├── mapa.py ← Seleção de fases na campanha
├── personagens_data.py ← Dados dos heróis (nome, terreno, habilidade)
├── progresso_heroi.py ← Sistema de XP e evolução
├── recompensa_cartas.py ← Geração de recompensas por fase
├── card_repository.py ← Banco de dados de todas as cartas
├── carta.py ← Classe base das cartas
├── deck_builder.py ← Montagem manual de decks
├── deck_personalizado.py ← Geração automática de deck por herói
├── efeitos_cartas.py ← Efeitos especiais para magias/feitiços
├── executar_habilidade.py ← Executa a lógica da habilidade da carta
├── balanceamento_cartas.py ← Avalia o poder das cartas
├── batalha_v8.py ← Modo de batalha mais atual (com mana/campo)
├── campanha_v1.py ← Executa campanha com lógica separada
├── drop_personagem.py ← [❌ Obsoleto] sistema antigo de drop
├── batalha.py ← [❌ Obsoleto] versão antiga do sistema de combate

yaml
Copiar
Editar

---

## 🔮 Futuras Etapas Planejadas

- ✅ Exibir status do herói antes das batalhas
- ✅ Salvar progresso da campanha
- 🔄 Recompensas por marcos (fase 5, 10, etc.)
- 🧪 Sistema de moedas e inventário
- 🛍️ Loja/NPC para troca de cartas
- 💾 Evolução de cartas por uso
- 🖼️ Implementação completa com interface Pygame

---

## 💡 Sobre o projeto

Esse projeto foi pensado para evoluir modularmente:
- Funciona em terminal no início
- Mas já está pronto para expansão gráfica
- Mantém lógica separada de interface para facilitar testes e evolução

---

## 👨‍💻 Requisitos

- Python 3.10+
- Pygame (`pip install pygame`)
- json, random, etc. (bibliotecas padrão)

---

## 🚀 Como iniciar

```bash
python menu_inicial.py