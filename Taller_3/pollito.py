import re

# Letra de la canción "El Pollito Pío"
letra = """
En la radio, hay un pollito
En la radio, hay un pollito
El pollito pío, el pollito pío
El pollito pío, el pollito pío
El pollito pío, el pollito pío

En la radio, hay una gallina
En la radio, hay una gallina
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un gallo
En la radio, hay también un gallo
Y el gallo corococo, y la gallina coo
Y el pollito pío, el pollito pío
El pollito pío, el pollito pío

En la radio, hay un pavo
En la radio, hay un pavo
Y el pavo glugluglu, y el gallo corococo
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una paloma
En la radio, hay una paloma
Y la paloma ruuu, el pavo glugluglu
El gallo corococo, y la gallina coo
El pollito pío, el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un gato
En la radio, hay también un gato
Y el gato miao, la paloma ruuu
El pavo glugluglu, el gallo corococo
Y la gallina coo, y el pollito pío
El pollito pío, y el pollito pío

En la radio, hay también un perro
En la radio, hay también un perro
Y el perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una cabra
En la radio, hay una cabra
Y la cabra mee, el perro guau guau
El gato miao, y la paloma ruu
El pavo glugluglu, el gallo cocoroco
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay un cordero
En la radio, hay un cordero
Y el cordero bee, y la cabra mee
El perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una vaca
En la radio, hay una vaca
Y la vaca moo, y el cordero bee
Y la cabra mee, el perro guau guau
El gato miao, y la paloma ruu
El pavo glugluglu, el gallo cocoroco
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un toro
En la radio, hay también un toro
Y el toro muu, y la vaca moo
Y el cordero bee, y la cabra mee
El perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay un tractor
En la radio, hay un tractor
Y el tractor brum, y el tractor brum
Y el tractor brum y el pollito oh-oh
"""

# Función para contar palabras totales y ocurrencias de "pío" y "pollito"
def contar_palabras(letra):
    palabras = re.findall(r'\w+', letra)  # \w+ busca palabras formadas por letras o números
    total_palabras = len(palabras)

    # Contar cuántas veces aparece "pío"
    pio_count = sum(1 for palabra in palabras if palabra.lower() == "pío")

    # Contar cuántas veces aparece "pollito"
    pollito_count = sum(1 for palabra in palabras if palabra.lower() == "pollito")

    return total_palabras, pio_count, pollito_count, palabras

# Mostrar los resultados iniciales
total_palabras, pio_count, pollito_count, palabras = contar_palabras(letra)

# Imprimir los resultados
print(f"\nTotal de palabras en la canción: {total_palabras}")
print(f"Veces que aparece 'pío': {pio_count}")
print(f"Veces que aparece 'pollito': {pollito_count}")

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
