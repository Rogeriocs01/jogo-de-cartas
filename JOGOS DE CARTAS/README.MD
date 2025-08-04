
# 🃏 Jogo de Cartas PvE com Campanha, Heróis e Decks Personalizados

Projeto em Python de um jogo de cartas tático com progressão por fases, heróis jogáveis, IA inimiga, montagem de decks e foco futuro em interface gráfica com Pygame (modo paisagem para Android). Arquitetura escalável para futura integração com motores como Unity.

---

## 🗂️ Estrutura de Diretórios (Atualizada)

```plaintext
📦 raiz/
│
├── batalha/                      # Sistema principal de batalhas
│   ├── habilidade_cartas.py
│   ├── habilidade_heroi.py
│   ├── jogador.py
│   ├── motor.py
│   ├── turno_inimigo.py
│   └── turno_jogador.py
│
├── campanha/                     # Progressão da campanha
│   ├── controlador.py
│   ├── fases.py
│   ├── inimigos.py
│   ├── progresso.py
│   ├── progresso_fases.py
│   └── recompensas_por_fase.py
│
├── cartas/                       # Dados e lógica das cartas
│   ├── card_repository.py
│   └── carta.py
│
├── dados/                        # Painel e progresso visual
│   ├── painel_progresso.py
│   ├── save.py
│   └── status_heroi.py
│
├── data/
│   └── personagens_data.py       # Dados de heróis jogáveis
│
├── gerenciamento/                # Inventário e progressão
│   ├── deck/
│   │   └── deck_manager/
│   ├── drops_personagens.py
│   ├── inventario_jogador.py
│   └── progresso_heroi.py
│
├── habilidades/                  # Habilidades unitárias e efeitos
│   ├── comuns/
│   ├── executar_habilidade.py
│   ├── executores.py
│   ├── habilidades_cartas_efeito.py
│   ├── habilidades_cartas_unitarias.py
│   ├── habilidades_heroi.py
│   └── habilidades_utils.py
│
├── herois/
│   └── gerenciador_heroi.py      # Classe e comportamento dos heróis
│
├── interface_pygame/             # Interface gráfica com Pygame
│   ├── assets/
│   │   ├── cartas/
│   │   ├── herois/
│   │   ├── molduras/
│   │   └── vazio/
│   ├── componentes/
│   │   └── carta_visual.py
│   ├── jogador/
│   │   └── inventario.json
│   ├── deck_builder_pygame.py
│   ├── exibir_carta.py
│   ├── main_pygame.py
│   ├── menu_pygame.py
│   ├── selecao_heroi_pygame.py
│   └── testar_cartas.py
│
├── testes/                       # (Reservado para testes futuros)
│
├── utils/
│   └── utils.py
│
├── arquivos diversos (em revisão ou desuso)
│   ├── balanceamento_cartas.py
│   ├── campanha_v1.py
│   ├── carregar_progresso.py
│   ├── efeitos_cartas.py
│   ├── habilidades_cartas.py
│   ├── interface_terminal.py
│   ├── jogador_teste.py
│   ├── jogo_cartas01.py
│   ├── loja.py
│   ├── mapa.py
│   ├── menu_inicial.py
│   ├── recompensas_cartas.py
│   ├── salvar_progresso.py
│   ├── selecao_personagem.py
│   └── selecionar_slots.py
│
└── README.md
```

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
- Arquivo separado por herói (ex: deck_Thorin.json)

---

## 🎮 Etapa 5 (Atual): Interface com Pygame

- Interface visual em desenvolvimento (modo paisagem, Android-friendly)
- Visualização de cartas, decks e inventário
- Uso do módulo `testar_cartas.py` para depuração gráfica
- Compatibilidade com imagens em `assets/cartas/`

---

## 📦 Requisitos

- Python 3.10+
- Instalar dependências com:
```bash
pip install pygame
```

---

## 🚀 Como Executar

```bash
python menu_inicial.py
```
