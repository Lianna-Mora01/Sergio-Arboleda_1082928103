import random

victorias_usuario = 0
victorias_maquina = 0

opciones = ["piedra", "papel", "tijera"]

while True:

    usuario = input("Elige piedra, papel o tijera (o escribe salir): ").lower()

    if usuario == "salir":
        print("Juego terminado")
        print("Victorias usuario:", victorias_usuario)
        print("Victorias máquina:", victorias_maquina)
        break

    if usuario not in opciones:
        print("Opción inválida")
        continue

    maquina = random.choice(opciones)

    print("La máquina eligió:", maquina)

    if usuario == maquina:
        print("Empate")

    elif (usuario == "piedra" and maquina == "tijera") or \
         (usuario == "tijera" and maquina == "papel") or \
         (usuario == "papel" and maquina == "piedra"):

        print("Ganaste")
        victorias_usuario += 1

    else:
        print("Gana la máquina")
        victorias_maquina += 1

    print("Marcador:")
    print("Usuario:", victorias_usuario)
    print("Máquina:", victorias_maquina)