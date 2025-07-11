# 🃏 Jogo de Cartas PvE com Campanha, Heróis e Decks Personalizados

Projeto em Python de um jogo de cartas tático com progressão por fases, heróis jogáveis, IA inimiga, montagem de decks e foco futuro em interface gráfica com Pygame para Android.

---

## 🗂️ Estrutura do Projeto

📁 **batalha/** – Lógica de batalha
- `motor.py` – Loop principal de combate
- `turno_jogador.py`, `turno_inimigo.py` – Lógica dos turnos
- `jogador.py` – Classe base do jogador (deck, mão, mana etc.)

📁 **campanha/** – Sistema de fases
- `controlador.py` – Executa a campanha
- `fases.py` – Define a dificuldade e inimigos por fase
- `inimigos.py` – Dados dos personagens inimigos
- `recompensas_por_fase.py` – Geração de recompensa fixa em marcos
- `progresso_fases.py` – Exibição do mapa de fases com status

📁 **dados/** – Dados auxiliares
- `status_heroi.py` – Mostra status do herói após vitória
- `painel_progresso.py` – XP, níveis e progresso de todos os heróis

📁 **habilidades/** – Habilidades de cartas e heróis
- `comuns.py`, `executores.py`, `habilidades_heroi.py`

📁 **imagens/** – Imagens das cartas para a interface Pygame

📁 **raiz/**
- `main.py` – (foco atual: terminal)
- `main_pygame.py` – (início da versão gráfica)
- `menu_inicial.py` – Menu principal
- `personagens_data.py` – Lista de heróis e seus dados
- `card_repository.py` – Base de dados de cartas
- `carta.py` – Classe base das cartas
- `efeitos_cartas.py`, `executar_habilidade.py`, `balanceamento_cartas.py`

🟡 **Sistema de Inventário e Progresso**
- `jogador_global.py` – Dados do jogador (moedas, nome)
- `inventario_jogador.py` – Inventário global de cartas
- `progresso_heroi.py` – XP, nível e fase atual dos heróis

🟢 **Decks**
- `deck_manager.py` – Montagem automática e manual de decks por herói

🛍️ **Loja**
- `loja.py` – Compra de cartas específicas e baús com moedas

🎁 **Recompensas**
- `recompensas_cartas.py` – Sorteio de cartas após vitória

---

## 🔮 Roadmap Atual

### ✅ Etapa 1: Sistema de fases e dificuldades
- ✔️ Cada herói inimigo aparece 3x (fácil, médio, difícil)
- ✔️ Vida e tamanho do deck aumentam com a dificuldade

### ✅ Etapa 2: Sistema global de jogador
- ✔️ Inventário e moedas são globais
- ✔️ Heróis guardam apenas XP e progresso

### ✅ Etapa 3: Inventário, recompensas e loja
- ✔️ Inventário permite múltiplas cópias de cartas
- ✔️ Recompensas aleatórias e fixas por marco
- ✔️ Loja funcional com compra direta e baús

### ✅ Etapa 4: Decks personalizados por herói
- ✔️ Deck automático baseado no herói
- ✔️ Deck manual (limite de cópias por carta, tamanho escalável)
- ✔️ Preparado para edição de deck antes da batalha

---

## 🖼️ Etapa 5 (Próxima): Interface Gráfica com Pygame
- Começar desenvolvimento da interface visual
- Foco em Android (modo paisagem)
- Suporte a clique, toques, visual de cartas e botões

---

## ✅ Requisitos

- Python 3.10+
- Pygame (`pip install pygame`)
- Pastas `dados/`, `imagens/` e arquivos `*.json`

---

## 🚀 Como executar

```bash
python menu_inicial.py
