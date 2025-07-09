# 🃏 Jogo de Cartas PvE com Campanha e Heróis

Projeto em Python de um jogo de cartas tático com foco em batalhas PvE, progressão de heróis, habilidades, e futuramente uma interface gráfica com Pygame.

---

## 🗂️ Estrutura do Projeto

📁 batalha/ ← Lógica de batalha entre jogador e inimigo  
│ ├── motor.py ← Loop principal da batalha (turnos e vitória)  
│ ├── turno_jogador.py ← Ações e opções do jogador (invocar, atacar, usar habilidades)  
│ ├── turno_inimigo.py ← IA do inimigo (compra, invoca, ataca, usa mana com lógica)  
│ ├── habilidade_cartas.py ← Ativação das habilidades das cartas  
│ ├── habilidade_heroi.py ← Ativação da habilidade especial do herói  
│ └── jogador.py ← Classe do jogador (vida, mana, campo, mão, deck etc)

📁 campanha/ ← Gerenciamento da campanha e progressão  
│ ├── controlador.py ← Executa as fases da campanha (início ao fim)  
│ ├── fases.py ← Define dados de cada fase (inimigo, terreno, dificuldade)  
│ ├── inimigos.py ← Dados dos inimigos por nome  
│ ├── progresso.py ← Salvamento do progresso da campanha  
│ └── recompensas_por_fase.py ← Drop e recompensas por marcos da campanha

📁 dados/ ← Salvamento e exibição de dados  
│ ├── save.py ← Funções de salvar e carregar progresso (JSON)  
│ └── status_heroi.py ← Exibe informações do herói atual após vitórias

📁 habilidades/ ← Definição de efeitos das habilidades  
│ ├── comuns.py ← Habilidades genéricas (cura, dano, boost)  
│ ├── executores.py ← Mapeia efeitos por carta  
│ └── habilidades_heroi.py ← Define as habilidades especiais dos heróis

📁 raiz do projeto  
├── main_pygame.py ← Interface visual (início da versão com Pygame)  
├── menu_inicial.py ← Menu principal (inicia campanha, exibe status e inventário)  
├── personagens_data.py ← Dados dos heróis jogáveis (nome, terreno, habilidade)  
├── progresso_heroi.py ← Sistema de XP e evolução de heróis  
├── recompensas_cartas.py ← Geração e aplicação de recompensas por vitória  
├── inventario_jogador.py ← Armazena e mostra as cartas por herói  
├── card_repository.py ← Banco de dados de todas as cartas (por ID)  
├── carta.py ← Classe base das cartas (nome, ataque, defesa, custo, etc)  
├── deck_personalizado.py ← Geração automática de decks por personagem  
├── executar_habilidade.py ← Executa os efeitos ativados das habilidades  
├── efeitos_cartas.py ← Efeitos especiais únicos de algumas cartas  
├── balanceamento_cartas.py ← Ferramenta para avaliar e balancear as cartas  

📁 arquivos obsoletos:  
├── batalha_v8.py ← [❌ Obsoleto] sistema antigo, mantido apenas para testes locais  
├── campanha_v1.py ← [❌ Obsoleto] sistema antigo de campanha  
├── drop_personagem.py ← [❌ Obsoleto] versão anterior de drops  
├── batalha.py ← [❌ Obsoleto] versão inicial do sistema de combate

---

## 🔮 Futuras Etapas Planejadas

- ✅ Exibir status do herói após vitórias
- ✅ Salvar progresso da campanha
- ✅ Geração de decks personalizados por herói
- ✅ Sistema de inventário por herói
- ✅ Geração de recompensas por vitória
- ✅ Loja de cartas vinculada ao progresso
- ✅ Correção de compra de cartas/mão/mana
- ✅ Substituição do sistema `batalha_v8.py` por `batalha/`
- 🔄 Recompensas especiais por marcos (fases 5, 10, 20...)
- 💰 Sistema de moedas para loja
- 🧪 Evolução de cartas por uso
- 🖼️ Implementação gráfica com interface Pygame

---

## 💡 Sobre o projeto

Esse projeto foi pensado para evoluir modularmente:  
- Totalmente funcional em terminal no estágio atual  
- Toda lógica já separada para facilitar uso com Pygame  
- Estrutura robusta para heróis, campanha, inventário e IA  
- Planejado para expansão com loja, economia e multiplayer PvP

---

## 👨‍💻 Requisitos

- Python 3.10+  
- Pygame (`pip install pygame`)  
- json, random, os, etc. (bibliotecas padrão)

---

## 🚀 Como iniciar

```bash
python menu_inicial.py
