import random

def juego_extendido():
    # Opciones y sus interacciones
    elementos = {
        "roca": ["fuego", "tijera", "esponja"],
        "fuego": ["tijera", "papel", "esponja"],
        "tijera": ["aire", "papel", "esponja"],
        "esponja": ["papel", "aire", "agua"],
        "papel": ["aire", "roca", "agua"],
        "aire": ["fuego", "roca", "agua"],
        "agua": ["fuego", "tijera", "esponja"]
    }

    # Inicializar marcador
    marcador_usuario = 0
    marcador_computadora = 0

    print("¡Bienvenido al juego extendido de Piedra, Papel o Tijera!")
    print("Nuevos elementos: roca, fuego, tijera, esponja, papel, aire, agua")

    while True:
        # Mostrar menú
        print("\nMenú:")
        print("1. Jugar")
        print("2. Ver marcador")
        print("3. Salir")

        # Entrada del usuario
        opcion_menu = input("Selecciona una opción del menú: ").strip()

        if opcion_menu == "1":  # Opción de jugar
            # Elección oculta de la computadora
            eleccion_computadora = random.choice(list(elementos.keys()))

            # Solicitar la entrada del usuario
            print("\nElige tu jugada: roca, fuego, tijera, esponja, papel, aire o agua.")
            eleccion_usuario = input("Tu elección: ").strip().lower()

            # Validar entrada del usuario
            if eleccion_usuario not in elementos:
                print("Opción no válida. Intenta de nuevo.")
                continue

            # Mostrar la elección de la computadora
            print(f"Computadora eligió: {eleccion_computadora}")

            # Determinar el resultado del juego
            if eleccion_usuario == eleccion_computadora:
                print("¡Es un empate!")
            elif eleccion_computadora in elementos[eleccion_usuario]:
                print("¡Ganaste! 🎉")
                marcador_usuario += 1
            else:
                print("Perdiste 😢")
                marcador_computadora += 1

        elif opcion_menu == "2":  # Opción de ver marcador
            print("\n--- Marcador ---")
            print(f"Usuario: {marcador_usuario}")
            print(f"Computadora: {marcador_computadora}")

        elif opcion_menu == "3":  # Opción de salir
            print("\n¡Gracias por jugar!")
            break

        else:  # Manejo de entrada no válida
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

# Iniciar el juego
juego_extendido()
