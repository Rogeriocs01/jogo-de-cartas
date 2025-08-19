# 🃏 Jogo de Cartas PvE com Campanha, Heróis e Decks Personalizados

Projeto em **Python** de um jogo de cartas tático inspirado em *Card Wars* e *Magic*, com:
- Progressão por **fases de campanha PvE**
- **Heróis jogáveis** com evolução de nível
- **Inventário global** de cartas
- **Decks personalizados por herói**
- Protótipo em **Pygame** (foco futuro em Android)

---

## 📂 Estrutura do Projeto

JOGOS_DE_CARTAS/
│── batalha/ # Sistema de batalha (código definitivo)
│ ├── jogador.py
│ ├── motor.py
│ └── ...
│
│── cartas/ # Repositório e lógica de cartas
│ ├── card_repository.py # Todas as cartas do jogo
│ └── habilidades_cartas.py
│
│── dados/ # Dados persistentes
│ ├── herois/ # Progresso individual de cada herói
│ ├── inventario.json # Inventário global de cartas
│ ├── jogador_global.py # Moedas, xp global etc.
│ └── escolha_heroi.json # Último herói selecionado
│
│── herois/ # Definições e gerenciador de heróis
│ └── gerenciador_heroi.py
│
│── interface_pygame/ # Protótipo em Pygame
│ ├── main_pygame.py # Loop principal
│ ├── menu_pygame.py # Menu inicial
│ ├── selecao_heroi_pygame.py
│ ├── deck_builder_pygame.py
│ └── assets/
│ └── cartas/ # Imagens .webp das cartas
│
│── .gitignore
│── README.md # (este arquivo)

yaml
Copiar
Editar

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone <url-do-repo>
   cd JOGOS_DE_CARTAS
Crie um ambiente virtual e instale as dependências:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
Execute o jogo no Pygame:

bash
Copiar
Editar
python interface_pygame/main_pygame.py
📦 Dependências
pygame → interface gráfica do protótipo

json / os / sys → persistência de dados e organização de arquivos

Pillow (futuro) → manipulação de imagens (para molduras e camadas visuais das cartas)

🛠️ Roadmap de Desenvolvimento
✅ Etapa 1 – Sistema de heróis e progressão
✅ Etapa 2 – Sistema de inventário global
✅ Etapa 3 – Inimigos com decks e HP escaláveis
✅ Etapa 4 – Separação entre inventário e deck por herói
✅ Etapa 5 – Protótipo em Pygame (menu, seleção de herói, deckbuilder)
🔜 Etapa 6 – Interface visual das cartas (molduras + atributos em camadas)
🔜 Etapa 7 – Sistema de batalha no Pygame
🔜 Etapa 8 – Loja e economia do jogo
🔜 Etapa 9 – Port para Android (PygameCE ou Kivy)
🔜 Etapa 10 – Futuro port para Unity (versão comercial, com artes avançadas estilo Senhor dos Anéis + Magic)

📌 Observações
As cartas no card_repository.py têm dois nomes:

nome → usado para exibição no jogo (ex: "Dragão de Lava")

arquivo → usado para buscar a imagem (dragao_de_lava.webp)

As imagens foram convertidas para WebP (512px altura, qualidade 80%) para reduzir o peso e melhorar a performance.

O jogo ainda está em protótipo. Próximos passos incluem renderização das cartas com molduras e a implementação do sistema de batalha no Pygame.

✍️ Desenvolvido em colaboração com IA para auxiliar na organização, automação e geração de conteúdo.

yaml
Copiar
Editar

---

👉 Agora, o próximo passo é **criar o resumo do projeto** (um “prompt base”) para iniciarmos no **novo chat sem perder nada da lógica atual**.  

Quer que eu já prepare esse **prompt base** para usarmos no próximo chat?







Perguntar ao ChatGPT
