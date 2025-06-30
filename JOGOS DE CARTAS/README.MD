# 🃏 Jogo de Cartas Tático

Um jogo de cartas estilo *Card Wars*, com campanha, heróis, terrenos, decks personalizados e sistema de habilidades estratégicas. Desenvolvido em Python, com foco em mecânicas acessíveis e expansíveis.

## 🔹 Recursos principais

- 🌍 Campanha com 60 fases e múltiplos níveis de dificuldade
- 🤙 20 heróis jogáveis, cada um com terreno favorito e habilidade especial
- 🃏 Sistema de deck personalizado com verificação de mana
- ⚔️ Campo de batalha com turnos, ataque direto e invocação
- ✨ Habilidades únicas por carta, com execução real durante a batalha
- 🔄 Modularização de lógica e habilidades para fácil manutenção

## 🚀 Como executar o jogo

1. Instale o Python (versão 3.10 ou superior)
2. Clone este repositório:
   ```bash
   git clone https://github.com/Rogeriocs01/jogo-de-cartas.git
   ```
3. Navegue até a pasta do projeto:
   ```bash
   cd jogo-de-cartas
   ```
4. Execute o menu principal:
   ```bash
   python menu_inicial.py
   ```

## 📁 Estrutura do projeto

```
JOGOS DE CARTAS/
├── menu_inicial.py
├── batalha_v8.py
├── carta.py
├── card_repository.py
├── habilidades_cartas.py
├── habilidades/
│   ├── __init__.py
│   ├── comuns.py
│   └── executores.py
├── campanha_v1.py
├── personagens_data.py
├── deck_personalizado.py
└── ...
```

## 📌 Planejamento futuro

- [ ] Implementar habilidades com gatilhos automáticos (ao morrer, ao atacar)
- [ ] Criar efeitos persistentes por turno
- [ ] Interface gráfica (versão futura com Pygame)
- [ ] Sistema de progressão de herói

---

## ⚖️ Licença

Em desenvolvimento pessoal — não distribuído publicamente ainda.