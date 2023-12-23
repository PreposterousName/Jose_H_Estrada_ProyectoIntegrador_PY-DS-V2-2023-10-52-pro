# Nombre: proyecto_integrador_4.py
# Proposito: Juego laberinto 4ta iteracion
# Author: Jose Hernan Estrada (Cohorte 52 PROtalento)
# Fecha: 11/12/2023

import os
from typing import List, Tuple
from readchar import readkey


def main() -> None:
    
    # Laberinto
    laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

    jugador = input("Hola, Ingrese su nombre: ")
    print(f"Bienvenido, {jugador}")

    # Convertir el mapa a una matriz
    matriz_laberinto = mapa_a_matriz(laberinto)

    # Coordenadas inicial y final
    inicio = (0, 0)
    final = (len(matriz_laberinto) - 1, len(matriz_laberinto[0]) - 1)

    # Ejecutar el juego
    if (main_loop(matriz_laberinto, inicio, final)):
        print(f"Ganaste!, Felicidades {jugador}")


def mapa_a_matriz(mapa: str) -> List[List[str]]:
    """Convierte la cadena del laberinto en una matriz de caracteres.

    :param mapa: str - cadena que representa el laberinto.
    :return: List[List[str]] - matriz de caracteres que representa el laberinto.
    """
    return [list(fila) for fila in mapa.split("\n")]

def limpiar_mostrar(mapa: List[List[str]]) -> None:
    """Limpia la pantalla y muestra el laberinto representado por la matriz.

    :param mapa: List[List[str]] - matriz que representa el laberinto.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    [print("".join(fila)) for fila in mapa]
       

def main_loop(mapa: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]) -> bool:
    """Implementa el bucle principal del juego.

    :param mapa: List[List[str]] - matriz que representa el laberinto.
    :param inicio: Tuple[int, int] - coordenadas de inicio.
    :param final: Tuple[int, int] - coordenadas finales.
    :return: bool - Si el jugador gano regresa verdadero a main
    """
    px, py = inicio
    mapa[px][py] = 'P'
    limpiar_mostrar(mapa)

    while (px, py) != final:
        tecla = readkey()
        nueva_px, nueva_py = px, py

        if tecla == '\x1b[A':  # Flecha arriba
            nueva_px = px - 1
        elif tecla == '\x1b[B':  # Flecha abajo
            nueva_px = px + 1
        elif tecla == '\x1b[C':  # Flecha derecha
            nueva_py = py + 1
        elif tecla == '\x1b[D':  # Flecha izquierda
            nueva_py = py - 1

        if 0 <= nueva_px < len(mapa) and 0 <= nueva_py < len(mapa[0]) and mapa[nueva_px][nueva_py] != '#':
            mapa[px][py] = '.'
            px, py = nueva_px, nueva_py
            mapa[px][py] = 'P'

        limpiar_mostrar(mapa)
    return (px, py) == final

if __name__ == "__main__":
    main()
