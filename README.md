# The Last Platform

Juego de plataformas por turnos con modo solitario y cooperativo, pensado para jugarse en red LAN con arquitectura cliente-servidor (Jugador 1 = servidor, Jugador 2 = cliente).

**Proyecto integrador · Lógica de Programación · UIDE**

**Equipo:** ROR · **Paralelo:** B

## Integrantes

| Integrante | Rol |
|---|---|
| Adrián Reyes | Traducción de DF1 a `juego.py` (menú y nicknames) |
| Samantha Mendez | Traducción de DF2 y DF3 a `game_logic.py` |
| Felipe Robayo | Repositorio de GitHub, `README.md` y `LICENSE` |

## Estructura del repositorio

```
ProyectoJuego/
├── juego.py        ← punto de entrada: menú que se repite hasta «Salir» (parte de DF1)
├── game_logic.py   ← validación de la jugada (DF2) y fin de la partida (DF3)
├── server.py       ← servidor, Jugador 1 (por ahora, un comentario)
├── client.py       ← cliente, Jugador 2 (por ahora, un comentario)
├── diseno/         ← diagramas de RAPTOR de la Fase 2
│   ├── DF1_partida.json
│   ├── DF2_validacion.rap
│   └── DF3_fin.json
├── LICENSE
└── README.md
```

## Cómo ejecutarlo

Requisitos: Python 3.10 o superior. No se necesitan librerías externas.

```bash
git clone https://github.com/feliperobayo79-jpg/ProyectoJuego.git
cd ProyectoJuego
python juego.py        # menú principal (1 Solitario | 2 Cooperativo | 3 Salir)
python game_logic.py   # validación de la jugada (DF2) y fin de la partida (DF3)
```

En esta fase, la opción «Jugar» del menú solo muestra un mensaje. La partida completa y los sockets se programan en la Fase 4.

## Tabla Diagrama de la Fase 2 → Código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió |
|---|---|---|
| DF1 · Menú y nicknames (`diseno/DF1_partida.json`) | `juego.py`, líneas 7–46 | Los Loop del menú, de la opción y de los nicknames pasaron a `while`; las Selections (`opcion = 3`, `modo = 2`) pasaron a `if`; Input y Output pasaron a `input()` y `print()`. «Jugar» solo muestra un mensaje. |
| DF2 · Validación de la jugada, modo solitario (`diseno/DF2_validacion.rap`) | `game_logic.py`, líneas 53–71 | El Loop VALIDACIÓN pasó a `while valida == "no"`; las Selections de formato y de reglas pasaron a una cadena `if / elif / else`. El estado de ejemplo (`suelo`, `pared`) se asigna al inicio, en las líneas 40–42. |
| DF2 · Validación de la jugada, Jugador 1 y Jugador 2 (`diseno/DF2_validacion.rap`) | `game_logic.py`, líneas 120–178 | Igual que arriba, pero con la regla de habilidades: el Explorador no usa las del Ingeniero y viceversa (RF-13). |
| DF3 · Fin de la partida, modo solitario (`diseno/DF3_fin.json`) | `game_logic.py`, líneas 73–114 | Las Selections de derrota (vidas o tiempo en 0), victoria y continuar pasaron a `if / else`. Los valores de vidas, tiempo y nivel se piden con `input()` y se validan con `while`. |
| DF3 · Fin de la partida, modo cooperativo (`diseno/DF3_fin.json`) | `game_logic.py`, líneas 180–246 | Igual que arriba, con las vidas y el tiempo de ambos jugadores. No hay empate porque el juego es cooperativo. |

## Video explicativo

[Ver video (máx. 5 min)](PEGAR-ENLACE-AQUI)

Muestra el menú, la validación con una jugada inválida, el fin de la partida y cómo se tradujo un diagrama de la Fase 2 a código.

## Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Ver el archivo [LICENSE](LICENSE).

## Créditos

- **Código de terceros:** ninguno.
- **Librerías:** solo la biblioteca estándar de Python.
- **Recursos visuales:** ninguno.
- **Diagramas:** hechos por el equipo en RAPTOR.
- **Herramientas de IA:**
  - ChatGPT: organización y división del trabajo del equipo.
  - Claude: investigación sobre el diagrama de arquitectura, comprensión de conceptos y apoyo con la documentación del repositorio. El equipo revisó y adaptó todo el contenido a su proyecto.
