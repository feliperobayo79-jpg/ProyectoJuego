# juego.py / Punto de entrada / The Last Platform (equipo ROR)
# Traduce el DF1 (menú principal y nicknames) de la Fase 2.
# Requisitos que cubre: RF-10 (menú), RF-02 (nicknames)
# En la Fase 3 la opción "Jugar" solo muestra un mensaje; la partida va en la Fase 4.

# DF1: salir := 0
salir = 0

# DF1: bucle "salir = 1"
while salir != 1:
    # DF1: opcion := 0
    opcion = ""

    # DF1: bucle de validación de la opción (1, 2 o 3)
    while not (opcion == "1" or opcion == "2" or opcion == "3"):
        print("1 Solitario | 2 Cooperativo | 3 Salir")
        opcion = input("Elige una opción: ")
        if not (opcion == "1" or opcion == "2" or opcion == "3"):
            print("Opción no válida. Elige 1, 2 o 3.")

    if opcion == "3":
        # DF1: salir := 1
        salir = 1
    else:
        # DF1: modo := opcion
        modo = int(opcion)

        # DF1: nickname del Jugador 1 (1 a 12 caracteres)
        nick_j1 = ""
        while not (len(nick_j1) >= 1 and len(nick_j1) <= 12):
            nick_j1 = input("Nickname del Jugador 1: ")
            if not (len(nick_j1) >= 1 and len(nick_j1) <= 12):
                print("Nickname no válido: usa de 1 a 12 caracteres.")

        # DF1: solo en modo cooperativo, nickname del Jugador 2
        if modo == 2:
            nick_j2 = ""
            while not (len(nick_j2) >= 1 and len(nick_j2) <= 12 and nick_j2 != nick_j1):
                nick_j2 = input("Nickname del Jugador 2: ")
                if nick_j2 == nick_j1:
                    print("El nickname debe ser distinto al del Jugador 1.")
                elif not (len(nick_j2) >= 1 and len(nick_j2) <= 12):
                    print("Nickname no válido: usa de 1 a 12 caracteres.")

        # Por ahora "Jugar" solo muestra un mensaje (la partida es de la Fase 4)
        print("La partida se programa en la Fase 4.")
