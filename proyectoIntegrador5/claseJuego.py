import os
from typing import List
from readchar import readkey

class Juego:
    """Clase principal del juego."""
    
    def __init__(self) -> None:        
        self.jugador = self.jugador
        self.mapa = []
        self.inicio = ()
        self.final = ()
    
    def jugador_msg(self) -> None:
        """Solicita el nombre del jugador."""

        self.jugador = input("Hola, ingrese su nombre: ")
        print(f"\nBienvenido, {self.jugador}!\n")
        print("Presiona Cualquier tecla para iniciar...")
        readkey()


    def mapa_a_matriz(self, mapa: str) -> List[List[str]]:
        """Convierte la cadena del laberinto en una matriz de caracteres. (Remueve cualquier whitespace innecesario)

        :param mapa: str - cadena que representa el laberinto.
        :return: List[List[str]] - matriz de caracteres que representa el laberinto.
        """
        return [list(fila) for fila in mapa.split("\n") if fila.strip()]

    def limpiar_mostrar(self) -> None:
        """Limpia la pantalla y muestra el laberinto representado por la matriz."""
        
        os.system('cls' if os.name == 'nt' else 'clear')
        [print("".join(fila)) for fila in self.mapa]

    def main_loop(self) -> None:
        """Implementa el bucle principal del juego."""

        self.jugador_msg()
        px, py = self.inicio
        self.mapa[px][py] = 'P'
        self.limpiar_mostrar()

        while (px, py) != self.final:
            tecla = readkey()
            nueva_px, nueva_py = px, py

            if tecla == '\x1b[A':  # Flecha arriba
                nueva_px = max(0, px - 1)
            elif tecla == '\x1b[B':  # Flecha abajo
                nueva_px = min(len(self.mapa) - 1, px + 1)
            elif tecla == '\x1b[C':  # Flecha derecha
                nueva_py = min(len(self.mapa[0]) - 1, py + 1)
            elif tecla == '\x1b[D':  # Flecha izquierda
                nueva_py = max(0, py - 1)

            if self.mapa[nueva_px][nueva_py] != '#':
                self.mapa[px][py] = '.'
                px, py = nueva_px, nueva_py
                self.mapa[px][py] = 'P'

            self.limpiar_mostrar()

        print(f"Ganaste! ¡Felicidades, {self.jugador}!")
