inventario = {}

def adicionar_carta(carta_id):
    if carta_id in inventario:
        inventario[carta_id] += 1
    else:
        inventario[carta_id] = 1

def mostrar_inventario():
    print("\n📜 Seu Inventário de Cartas:")
    if not inventario:
        print("Você ainda não possui nenhuma carta.")
    else:
        for carta_id, quantidade in inventario.items():
            print(f"{carta_id} x{quantidade}")
