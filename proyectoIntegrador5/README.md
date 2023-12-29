# Laberinto - Juego de consola

Este es un juego de laberinto de consola en Python, donde el objetivo es llegar desde el punto de inicio hasta el punto final del laberinto.

## Requisitos

- Python 3.x
- Biblioteca `readchar` (instalable mediante `pip install readchar`)
- Laberintos `map.txt` (en directorio `./mapas/map*[1-9].txt`)

## Cómo jugar

1. **Ejecutar el juego:**
   - Clonar o descargar el repositorio.
   - Asegúrate de tener Python 3.x instalado.
   - Instala la biblioteca `readchar` con `pip install readchar`.
   - Ejecuta el archivo `jugarArchivo.py`.

2. **Instrucciones:**
   - Al iniciar, el juego te pedirá que ingreses tu nombre.
   - Te dara la bienvenida y pedira que presiones cualquier tecla para inciar el juego.
   - Seleccionará un laberinto aleatorio de una carpeta de mapas.
   - Usa las teclas de flecha para moverte por el laberinto y llegar al punto final.
   - Los `'.'` son el camino, `'#'` paredes y `'P'` el jugador.
   - Al ganar te felicita el juego.

## Estructura del proyecto

- `claseJuego.py`: Clase base para el juego de laberinto.
- `JugarArchivo.py`: Clase que gestiona la lectura de mapas desde archivos (Y donde se ejecuta el juego).
- Carpeta `mapas`: Contiene archivos de texto con diferentes laberintos.

## Cómo añadir mapas 

- Guarda tu archivo de mapa en la carpeta `mapas`.
- Ejecuta el juego y tu mapa estará disponible para jugar.

## Notas

- Este juego se creó como un proyecto de aprendizaje para el cohorte 52 de PROtalento con Ada School y puede tener limitaciones o mejoras pendientes.

## Source

### Creado por:
   -@PreposterousName (Jose Hernan Estrada (Cohorte 52 PROtalento))
