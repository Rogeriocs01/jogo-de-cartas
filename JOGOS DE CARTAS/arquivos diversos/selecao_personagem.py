def escolher_personagem():
    personagens_disponiveis = [
        "Thorin, o Bravo",
        "Elora, a Arqueira Élfica",
        "Balgor, o Orc Sanguinário",
        "Luthien, a Maga da Luz",
        "Dargul, o Senhor dos Túneis",
        "Mirael, a Feiticeira Sombria",
        "Rogar, o Bárbaro do Norte",
        "Elenor, a Protetora da Floresta",
        "Karguk, o Rei Goblin",
        "Sirius, o Invocador de Feras",
        "Velaria, a Dama das Sombras",
        "Grumak, o Demônio da Rocha",
        "Thalia, a Curandeira de Elmswood",
        "Volgath, o Senhor dos Dragões",
        "Feyra, a Caçadora de Almas",
        "Gorim, o Guerreiro Anão",
        "Neriah, a Encantadora",
        "Zarok, o Necromante",
        "Kael, o General de Gondren",
        "Sylara, a Rainha dos Espíritos",
    ]

    print("\nEscolha seu personagem:")
    for idx, nome in enumerate(personagens_disponiveis, start=1):
        print(f"{idx}. {nome}")

    while True:
        try:
            escolha = int(input("\nDigite o número do personagem desejado: "))
            if 1 <= escolha <= len(personagens_disponiveis):
                personagem_escolhido = personagens_disponiveis[escolha - 1]
                print(f"\n✅ Você escolheu: {personagem_escolhido}!")
                return personagem_escolhido
            else:
                print("Opção inválida. Escolha um número entre 1 e 20.")
        except ValueError:
            print("Por favor, digite um número válido.")
