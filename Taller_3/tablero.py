import random

def generar_tablero(filas, columnas, letra_1, letra_2):
   
    tablero = [[letra_1 for i in range(columnas)] for j in range(filas)]

    num_posiciones = random.randint(1, filas * columnas - 1)
    posiciones = random.sample(range(filas * columnas), num_posiciones)

    
    for pos in posiciones:
        fila = pos // columnas
        columna = pos % columnas
        tablero[fila][columna] = letra_2

    return tablero

def mostrar_tablero(tablero):
    
    for fila in tablero:
        print(" ".join(fila))

def main():
  
    filas = int(input("Ingrese el número de filas: ") or 5)
    columnas = int(input("Ingrese el número de columnas: ") or 5)
    letra_1 = input("Ingrese la primera letra: ") or '0'
    letra_2 = input("Ingrese la segunda letra: ") or '8'

   
    tablero_creado = generar_tablero(filas, columnas, letra_1, letra_2)
    mostrar_tablero(tablero_creado)

if __name__ == "__main__":
    main()
