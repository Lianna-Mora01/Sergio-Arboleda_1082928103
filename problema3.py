import random

while True:

    longitud = int(input("Ingrese la longitud de la contraseña (8 - 20): "))

    if longitud < 8 or longitud > 20:
        print("Longitud inválida. Debe estar entre 8 y 20.")
        continue

    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiales = "!@#$%"

    todos = mayusculas + minusculas + numeros + especiales

    contraseña = ""

    for i in range(longitud):
        contraseña = contraseña + random.choice(todos)

    print("Contraseña generada:", contraseña)

    otra = input("¿Quieres generar otra contraseña? (s/n): ")

    if otra.lower() != "s":
        print("Programa terminado.")
        break