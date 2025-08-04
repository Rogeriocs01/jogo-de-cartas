# 🃏 Jogo de Cartas PvE com Campanha, Heróis e Decks Personalizados

Projeto em Python de um jogo de cartas tático com progressão por fases, heróis jogáveis, IA inimiga, montagem de decks e foco futuro em interface gráfica com Pygame (modo paisagem para Android). Arquitetura escalável para futura integração com motores como Unity.

---

## 🗂️ Estrutura de Diretórios (Atualizado)

📁 **batalha/** – Sistema de batalha (principal)
- `motor.py` – Loop principal de combate
- `turno_jogador.py`, `turno_inimigo.py` – Ações dos turnos
- `jogador.py` – Classe base do jogador (vida, mana, campo etc.)
- `habilidade_cartas.py`, `habilidade_heroi.py` – Execução de habilidades

📁 **cartas/** – Sistema de cartas
- `card_repository.py` – Base de dados com todas as cartas
- `carta.py` – Classe `Carta` (estrutura e comportamento)

📁 **campanha/** – Fases da campanha
- `controlador.py` – Executa as fases
- `fases.py` – Dados das fases (dificuldade, inimigos)
- `inimigos.py` – Atributos dos personagens inimigos
- `recompensas_por_fase.py` – Recompensas fixas por progresso
- `progresso_fases.py` – Mapa visual das fases

📁 **dados/** – Componentes informativos
- `painel_progresso.py` – Exibe XP, níveis e progresso
- `status_heroi.py` – Mostra status do herói após vitórias

📁 **gerenciamento/** – Sistema de controle do jogo
- `inventario_jogador.py` – Inventário global de cartas
- `jogador_global.py` – Dados do jogador (moedas, nome)
- `drops_personagens.py` – Drops específicos por personagem
- `deck_manager.py` – Montagem de decks automática e manual

📁 **herois/** – Estrutura e carregamento dos heróis
- `gerenciador_heroi.py` – Classe Heroi, compra, invocação, ataques
- `progresso_heroi.py` – XP, níveis e fases por herói

📁 **imagens/** – Ilustrações das cartas (usadas no Pygame)

📁 **interface/** (em breve) – Componentes visuais com Pygame

📁 **raiz/**
- `main.py` – Execução no terminal
- `main_pygame.py` – Execução com interface visual
- `menu_inicial.py` – Menu principal de entrada
- `personagens_data.py` – Lista com dados dos heróis
- `recompensas_cartas.py` – Sorteio aleatório após vitórias
- `loja.py` – Sistema de compras de cartas/baús com moedas

---

## 🔮 Roadmap Atual

### ✅ Etapa 1: Sistema de fases e dificuldade
- Heróis inimigos escalam em vida/deck (fácil, médio, difícil)

### ✅ Etapa 2: Sistema global de jogador
- Moedas e inventário globais
- Heróis com XP, níveis e progresso individual

### ✅ Etapa 3: Inventário e loja
- Inventário com múltiplas cópias
- Recompensas variadas e loja funcional

### ✅ Etapa 4: Decks personalizados
- Montagem automática e manual
- Restrições por nível e quantidade

---

## 🖼️ Etapa 5 (Atual): Interface com Pygame

- Início da interface gráfica (modo paisagem, Android)
- Mostrar mão, campo, botões de ação e status
- Permitir clique, hover, seleção e animações simples

---

## 📦 Requisitos

- Python 3.10+
- Pygame → `pip install pygame`
- Pastas `dados/`, `imagens/` e arquivos JSON válidos

---

## 🚀 Como Executar

```bash
python menu_inicial.py
