# Definimos el menú inicial
Menu = [
    ['ID004', "entrada", "ensalada"],
    ['ID008', "entrada", "sopa de tomate"],
    ['ID005', "entrada", "sopa de cebolla"],
    ['ID011', "bebida", "Jugo de Fresa"],
    ['ID012', "bebida", "Limonada Natural"],
    ['ID102', "plato fuerte", "pasta"],
    ['ID106', "plato fuerte", "lassagna"],
]

# 1.1 Función para filtrar por categoría
def filter_by_category(menu, category):
    return [item for item in menu if item[1] == category]

# 1.2 Función para filtrar por subcadena
def filter_by_substring(menu, substring):
    return [item[2] for item in menu if substring.lower() in item[2].lower()]

# 1.3 Función para mapear menú por tipo de plato
def map_menu_by_category(menu):
    menu_dict = {}
    for item in menu:
        category = item[1]
        dish = item[2]
        if category not in menu_dict:
            menu_dict[category] = []
        menu_dict[category].append(dish)
    return menu_dict

# Menú interactivo con opciones para el usuario
def display_menu():
    print("""
    Ingrese la opción que desea realizar:
    1. Visualizar la información del menú
    2. Agregar nuevos elementos al menú
    3. Filtrar por una categoría
    4. Buscar por un nombre
    5. Visualizar nombres en categorías
    6. Salir
    """)

def interactive_menu():
    while True:
        # Mostrar el menú de opciones
        display_menu()
        option = input("Elija una opción (1-6): ").strip()

        if option == "1":
            # Mostrar el menú completo
            print("\nInformación del menú:")
            for item in Menu:
                print(f"{item[0]} - {item[1]} - {item[2]}")

        elif option == "2":
            # Agregar nuevos elementos al menú
            id_ = input("Ingrese el ID: ").strip()
            category = input("Ingrese la categoría (entrada, bebida, plato fuerte): ").strip()
            dish = input("Ingrese el nombre del plato: ").strip()
            Menu.append([id_, category, dish])
            print(f"{dish} ha sido agregado al menú.")

        elif option == "3":
            # Filtrar por categoría
            category = input("Ingrese la categoría a filtrar (entrada, bebida, plato fuerte): ").strip()
            filtered_menu = filter_by_category(Menu, category)
            print(f"\nPlatos en la categoría {category}:")
            for item in filtered_menu:
                print(f"{item[2]}")

        elif option == "4":
            # Buscar por subcadena
            substring = input("Ingrese la subcadena a buscar: ").strip()
            filtered_items = filter_by_substring(Menu, substring)
            print(f"\nPlatos que contienen '{substring}':")
            for item in filtered_items:
                print(item)

        elif option == "5":
            # Visualizar nombres por categoría
            mapped_menu = map_menu_by_category(Menu)
            print("\nPlatos por categoría:")
            for category, dishes in mapped_menu.items():
                print(f"{category.capitalize()}: {', '.join(dishes)}")

        elif option == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor elija entre 1 y 6.")

# Llamamos al menú interactivo
interactive_menu()
