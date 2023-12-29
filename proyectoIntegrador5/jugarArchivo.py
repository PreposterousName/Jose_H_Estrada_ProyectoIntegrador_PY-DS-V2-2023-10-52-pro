import os
import random
from typing import List, Tuple
from claseJuego import Juego

class JuegoArchivo(Juego):
    """Clase que gestiona la lectura de mapas desde archivos."""

    def __init__(self) -> None:
        """Inicializa el juego leyendo un archivo de laberinto al azar."""
        self.mapa, self.inicio, self.final = self.obtener_mapa()
        
    def obtener_mapa(self) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
        """Lee un archivo aleatorio de una carpeta de mapas.

        :return: Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]] - Mapa, coordenadas de inicio y final.
        """
        path_a_mapas = "./mapas"  # Relative PATH de mapas dentro del directorio ../proyectoIntegrador5
        archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = f"{path_a_mapas}/{nombre_archivo}"

        try:
            with open(path_completo, 'r') as file:
                lineas = file.readlines()

                coordenadas = lineas[0].split()
                inicio = (int(coordenadas[0]), int(coordenadas[1]))
                final = (int(coordenadas[3]), int(coordenadas[2]))

                laberinto = ''.join(lineas[1:])
                matriz_laberinto = self.mapa_a_matriz(laberinto)

                return matriz_laberinto, inicio, final
        except:
            print("El archivo no fue encontrado.")
            exit(1)

if __name__ == "__main__":
    juego = JuegoArchivo()
    juego.main_loop()


