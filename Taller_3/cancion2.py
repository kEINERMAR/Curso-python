import re

# Letra de la canción "Baby Shark"
letra = """
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!

Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!

Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!

Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!

Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!

Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt!

Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away!

Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last!

It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end!
"""

# Función para contar palabras, "shark" y "doo"
def contar_cancion(letra):
    # Extraemos todas las palabras (cualquier secuencia de letras o números)
    palabras = re.findall(r'\w+', letra)  # \w+ encuentra palabras
    total_palabras = len(palabras)

    # Contamos las veces que aparece "shark" y "doo"
    shark_count = sum(1 for palabra in palabras if palabra.lower() == "shark")
    doo_count = sum(1 for palabra in palabras if palabra.lower() == "doo")

    return total_palabras, shark_count, doo_count, palabras

# Mostrar los resultados iniciales
total_palabras, shark_count, doo_count, palabras = contar_cancion(letra)

# Mostrar los resultados
print(f"Total de palabras en la canción: {total_palabras}")
print(f"Veces que aparece 'shark': {shark_count}")
print(f"Veces que aparece 'doo': {doo_count}")

# Preguntar si el usuario quiere buscar una palabra o frase específica
buscar_opcion = input("\n¿Quieres buscar una palabra o frase específica? (si/no): ").strip().lower()

if buscar_opcion == "si":
    # Solicitar la palabra o frase a buscar
    buscar = input("Ingrese la palabra o frase a buscar: ").strip().lower()

    # Contar cuántas veces aparece la palabra o frase ingresada
    busqueda_count = sum(1 for palabra in palabras if palabra.lower() == buscar)

    # Mostrar los resultados de la búsqueda
    print(f"\nVeces que aparece '{buscar}': {busqueda_count}")
else:
    print("\nNo se realizó ninguna búsqueda adicional.")
