# -------------------------UNIENDO DF2 Y DF3
# --------------------GAME_LOGIC: SAMANTHA MENDEZ

print("======MODO DE JUEGO======")  # RF-10: selección del modo solitario
print("=== 1. SOLITARIO ===")
print("=== 2. MULTIJUGADOR ===")

# RF-10: validar la selección del modo.
# RF-01: ofrecer la opción multijugador; la conexión LAN se implementa después.
modo_de_juego = input("INGRESE SU ELECCIÓN (1-2): ").strip()

while not modo_de_juego.isdigit() or int(modo_de_juego) not in (1, 2):
    print("Modo de juego inválido")
    modo_de_juego = input("INGRESE SU ELECCIÓN (1-2): ").strip()

modo_de_juego = int(modo_de_juego)

# RF-05: movimientos comunes y restricciones físicas.
jugadas_comunes = (
    "avanzar",
    "saltar",
    "retroceder",
    "agacharse",
)

# RF-13: habilidades propias de cada personaje.
jugadas_explorador = (
    "detectar",
    "iluminar",
)

jugadas_ingeniero = (
    "activar interruptor",
    "reparar",
    "desbloquear puerta",
)

todas_las_jugadas = jugadas_comunes + jugadas_explorador + jugadas_ingeniero

# Estado de ejemplo para DF2: 1 = sí, 0 = no.
suelo = 1
pared = 0


# ------------------------- MODO DE JUEGO SOLITARIO
if modo_de_juego == 1:
    print("MODO DE JUEGO: SOLITARIO")

    # RF-13: el Jugador 1 es el Explorador.
    for jugada in jugadas_comunes + jugadas_explorador:
        print(jugada)

    valida = "no"

    # RF-05: validar salto y avance frente a paredes.

    while valida == "no":
        jugada_solitario = input("Ingrese su jugada: ").strip().lower()

        if jugada_solitario not in todas_las_jugadas:
            print("Jugada inválida, intenta de nuevo.")

        elif jugada_solitario == "saltar" and suelo == 0:
            print("No puedes saltar en el aire.")

        elif jugada_solitario == "avanzar" and pared == 1:
            print("No puedes atravesar paredes.")

        else:
            valida = "si"
            print("Jugada aceptada: " + jugada_solitario)

    # RF-11: validar vidas y tiempo para la derrota en modo solitario.
    vidas = input("Ingrese su numero de vidas (0-3): ").strip()

    while not vidas.isdigit() or int(vidas) not in (0, 1, 2, 3):
        print("Vidas inválidas")
        vidas = input("Ingrese su numero de vidas (0-3): ").strip()

    vidas = int(vidas)

    tiempo = input("Ingrese su tiempo (0-300): ").strip()

    while not tiempo.isdigit() or int(tiempo) not in range(301):
        print("Tiempo inválido")
        tiempo = input("Ingrese su tiempo (0-300): ").strip()

    tiempo = int(tiempo)

    # RF-11: finalizar el modo solitario si se acaban las vidas o el tiempo.
    if tiempo == 0 or vidas == 0:
        print("Derrota: La partida a finalizado")

        if vidas == 0:
            print("Vidas insuficientes")
        else:
            print("tiempo insuficiente")

    else:
        estado_de_nivel = input(
            "Ha terminado el nivel Si(escriba 1) / No(escriba 0): "
        ).strip()

        while estado_de_nivel not in ("0", "1"):
            print("Estado de nivel inválido")
            estado_de_nivel = input(
                "Ha terminado el nivel Si(escriba 1) / No(escriba 0): "
            ).strip()

        if estado_de_nivel == "1":
            print("Victoria! nivel finalizado.")
        else:
            print("Continuando la partida")


# ------------------------- MODO MULTIJUGADOR
else:
    print("MODO DE JUEGO: MULTIJUGADOR")

    # RF-04: mostrar quién realiza esta jugada de prueba.
    # RF-13: el Jugador 1 es el Explorador.
    for jugada in jugadas_comunes + jugadas_explorador:
        print(jugada)

    valida = "no"

    # RF-05: validar salto y avance frente a paredes.
    # RF-13: impedir que el Explorador use habilidades del Ingeniero.
    while valida == "no":
        jugada_jugador_1 = (
            input("Jugador 1 (Explorador), ingrese su jugada: ").strip().lower()
        )

        if jugada_jugador_1 not in todas_las_jugadas:
            print("Jugada inválida, intenta de nuevo.")

        elif jugada_jugador_1 in jugadas_ingeniero:
            print("Esa habilidad es del Ingeniero.")

        elif jugada_jugador_1 == "saltar" and suelo == 0:
            print("No puedes saltar en el aire.")

        elif jugada_jugador_1 == "avanzar" and pared == 1:
            print("No puedes atravesar paredes.")

        else:
            valida = "si"
            print("Jugada aceptada: " + jugada_jugador_1)

    # RF-04: mostrar el turno del Jugador 2.
    # RF-13: el Jugador 2 es el Ingeniero.
    for jugada in jugadas_comunes + jugadas_ingeniero:
        print(jugada)

    valida = "no"

    # RF-05: validar salto y avance frente a paredes.
    # RF-13: impedir que el Ingeniero use habilidades del Explorador.
    while valida == "no":
        jugada_jugador_2 = (
            input("Jugador 2 (Ingeniero), ingrese su jugada: ").strip().lower()
        )

        if jugada_jugador_2 not in todas_las_jugadas:
            print("Jugada inválida, intenta de nuevo.")

        elif jugada_jugador_2 in jugadas_explorador:
            print("Esa habilidad es del Explorador.")

        elif jugada_jugador_2 == "saltar" and suelo == 0:
            print("No puedes saltar en el aire.")

        elif jugada_jugador_2 == "avanzar" and pared == 1:
            print("No puedes atravesar paredes.")

        else:
            valida = "si"
            print("Jugada aceptada: " + jugada_jugador_2)

    # RF-12: validar las vidas de ambos jugadores.
    vidas_jugador_1 = input("Ingrese su numero de vidas (0-3), Jugador 1: ").strip()

    while not vidas_jugador_1.isdigit() or int(vidas_jugador_1) not in (0, 1, 2, 3):
        print("Vidas inválidas")
        vidas_jugador_1 = input("Ingrese su numero de vidas (0-3), Jugador 1: ").strip()

    vidas_jugador_1 = int(vidas_jugador_1)

    vidas_jugador_2 = input("Ingrese su numero de vidas (0-3), Jugador 2: ").strip()

    while not vidas_jugador_2.isdigit() or int(vidas_jugador_2) not in (0, 1, 2, 3):
        print("Vidas inválidas")
        vidas_jugador_2 = input("Ingrese su numero de vidas (0-3), Jugador 2: ").strip()

    vidas_jugador_2 = int(vidas_jugador_2)

    # RF-09: validar que el tiempo esté entre 0 y 300 segundos.
    tiempo_jugador_1 = input("Ingrese su tiempo (0-300), Jugador 1: ").strip()

    while not tiempo_jugador_1.isdigit() or int(tiempo_jugador_1) not in range(301):
        print("Tiempo inválido")
        tiempo_jugador_1 = input("Ingrese su tiempo (0-300), Jugador 1: ").strip()

    tiempo_jugador_1 = int(tiempo_jugador_1)

    # RF-09: validar el tiempo del Jugador 2 con su propia variable.
    tiempo_jugador_2 = input("Ingrese su tiempo (0-300), Jugador 2: ").strip()

    while not tiempo_jugador_2.isdigit() or int(tiempo_jugador_2) not in range(301):
        print("Tiempo inválido")
        tiempo_jugador_2 = input("Ingrese su tiempo (0-300), Jugador 2: ").strip()

    tiempo_jugador_2 = int(tiempo_jugador_2)

    # RF-09 y RF-12: si se acaba el tiempo o uno pierde todas sus vidas,
    # hay derrota cooperativa para ambos.
    if (
        vidas_jugador_1 == 0
        or vidas_jugador_2 == 0
        or tiempo_jugador_1 == 0
        or tiempo_jugador_2 == 0
    ):
        print("Derrota cooperativa: el equipo perdió la partida.")

        if vidas_jugador_1 == 0 or vidas_jugador_2 == 0:
            print("Vidas insuficientes")

        if tiempo_jugador_1 == 0 or tiempo_jugador_2 == 0:
            print("Se acabó el tiempo")

    else:
        estado_niveles = input(
            "Han terminado todos los niveles? Si(escribe:1) / No(escribe:0): "
        ).strip()

        while estado_niveles not in ("0", "1"):
            print("Estado de nivel inválido")
            estado_niveles = input(
                "Han terminado todos los niveles? Si(escribe:1) / No(escribe:0): "
            ).strip()

        # RF-08: declarar victoria conjunta al completar todos los niveles.
        if estado_niveles == "1":
            print("Victoria cooperativa: ambos jugadores han ganado la partida.")
        else:
            print("Continuando la partida")
