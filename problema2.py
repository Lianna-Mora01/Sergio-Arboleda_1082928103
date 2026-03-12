saldo = 1000

while True:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Tu saldo es:", saldo)

    elif opcion == 2:
        deposito = float(input("¿Cuánto dinero deseas depositar?: "))
        saldo = saldo + deposito
        print("Depósito realizado. Nuevo saldo:", saldo)

    elif opcion == 3:
        retiro = float(input("¿Cuánto dinero deseas retirar?: "))
        if retiro <= saldo:
            saldo = saldo - retiro
            print("Retiro realizado. Nuevo saldo:", saldo)
        else:
            print("No tienes suficiente saldo.")

    elif opcion == 4:
        print("Gracias por usar el cajero.")
        break

    else:
        print("Opción no válida.")