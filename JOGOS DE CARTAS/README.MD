
---

## ⚔️ Sistema de Campanha PvE

- 60 fases progressivas.
- Cada inimigo é enfrentado 3x com dificuldade crescente (fácil → médio → difícil).
- Derrotar o inimigo pela 3ª vez desbloqueia ele como **herói jogável** (começando no nível 1).
- Recompensas: XP, moedas, cartas fixas e aleatórias.

---

## 🎒 Inventário e Progressão

- O jogador possui um **inventário global** de cartas.
- Moedas também são globais (não por herói).
- Cada herói tem seu **nível e XP próprios**, mas usam as cartas do inventário geral.
- Decks podem ser montados com as cartas adquiridas.
- Níveis desbloqueiam mais mana, cartas na mão, e tamanho de deck.

---

## 📈 Estrutura de Crescimento por Nível

| Nível | Cartas na Mão | Tamanho do Deck | Máx. Repetição | Vida Extra | Mana |
|-------|----------------|------------------|----------------|------------|------|
| 1     | 3              | 10               | 2              | 0          | 3    |
| 5     | 4              | 12               | 2              | +2         | 4    |
| 10    | 5              | 15               | 3              | +5         | 5    |

---

## 🛠️ Roadmap de Desenvolvimento

### ✅ Etapa 0 — Sistema Básico (Pronto)
- Inventário global.
- Heróis com XP e níveis.
- Campanha com IA, campo de batalha e habilidades.

### 🔄 Etapa 1 — Estrutura Completa de Decks (📍Atual)
- Jogador compra cartas do **deck**, não do inventário.
- Decks são **pré-montados** e podem ser editados.
- Cada herói possui um deck base.
- Limite de repetições por carta no deck.
- Deck e mão crescem com o nível.

### 📊 Etapa 2 — IA e Dificuldade
- Vida dos inimigos escala por dificuldade.
- IA toma decisões melhores em modos médio/difícil.
- Cada inimigo tem um conjunto de cartas por dificuldade.

### 🧙 Etapa 3 — Recompensas Avançadas
- Derrotar inimigo 3x libera ele como herói jogável.
- Novo herói começa com nível 1, mas usa o inventário do jogador.
- Deck é montado a partir das cartas adquiridas.

### 🖼️ Etapa 4 — Interface Pygame
- Exibição visual do campo, cartas e status.
- Mapa clicável, deck editor visual, cliques em cartas.
- Interface pensada para mobile.

### 📱 Etapa 5 — Versão Mobile
- Foco exclusivo no Android.
- Controles por toque e responsividade.
- Geração de APK via Buildozer ou Kivy.

### 🛍️ Etapa 6 — Monetização
- Baús com raridades.
- Recompensas diárias.
- Venda de moedas via PIX/cartão (opcional).
- Torneios ou desafios especiais semanais.

---

## 💡 Requisitos

- Python 3.10+
- Pygame (`pip install pygame`)
- json, random, os (já inclusos na biblioteca padrão)

---

## 🚀 Como Iniciar

```bash
python menu_inicial.py
